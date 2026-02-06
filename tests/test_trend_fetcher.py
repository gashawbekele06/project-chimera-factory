from pydantic import BaseModel
from unittest.mock import patch, MagicMock
from skills.fetch_trends import fetch_trends

# Expected output schema (from specs/skills/fetch_trends/README.md)


class TrendItem(BaseModel):
    name: str
    volume: int
    category: str | None = None


class FetchTrendsOutput(BaseModel):
    trends: list[TrendItem]
    fetched_at: str
    source_platforms: list[str] | None = None


def test_fetch_trends_output_schema_validation():
    """Test that the output schema matches expected format."""
    mock_output = {
        "trends": [
            {"name": "#EthiopiaFashion", "volume": 45000,
             "category": "fashion"},
            {"name": "#AddisStyle", "volume": 32000}
        ],
        "fetched_at": "2026-02-05T10:00:00Z",
        "source_platforms": ["twitter"]
    }

    # Validate mock → should pass (this is just schema check)
    validated = FetchTrendsOutput(**mock_output)
    assert len(validated.trends) == 2
    assert validated.fetched_at is not None


@patch('skills.fetch_trends.tweepy')
def test_fetch_trends_with_mock(mock_tweepy):
    """Test fetch_trends function with mocked Twitter API."""
    # Mock the tweepy API
    mock_api = MagicMock()
    mock_tweepy.API.return_value = mock_api

    # Mock trends_available response
    mock_api.trends_available.return_value = [
        {"woeid": 23424802, "countryCode": "ET",
            "country": "Ethiopia", "name": "Addis Ababa"}
    ]

    # Mock trends_place response
    mock_api.trends_place.return_value = [{
        "trends": [
            {"name": "#EthiopiaFashion", "tweet_volume": 45000},
            {"name": "#AddisStyle", "tweet_volume": 32000},
            {"name": "#CoffeeCulture", "tweet_volume": 28000}
        ]
    }]

    input_data = {
        "platforms": ["twitter"],
        "region": "ET",
        "limit": 10
    }

    result = fetch_trends(input_data)

    # Validate response structure
    validated = FetchTrendsOutput(**result)
    assert isinstance(validated.trends, list)
    assert len(validated.trends) == 3
    assert validated.source_platforms == ["twitter"]
    assert validated.trends[0].name == "#EthiopiaFashion"
    assert validated.trends[0].volume == 45000


@patch('skills.fetch_trends.tweepy')
def test_fetch_trends_global_woeid_fallback(mock_tweepy):
    """Test that global trends are fetched when region not found."""
    mock_api = MagicMock()
    mock_tweepy.API.return_value = mock_api

    # Return empty locations (region not found)
    mock_api.trends_available.return_value = []
    mock_api.trends_place.return_value = [{
        "trends": [
            {"name": "#GlobalTrend", "tweet_volume": 100000}
        ]
    }]

    input_data = {
        "platforms": ["twitter"],
        "region": "UnknownRegion",
        "limit": 5
    }

    result = fetch_trends(input_data)

    # Should still return results using global WOEID (1)
    validated = FetchTrendsOutput(**result)
    assert len(validated.trends) == 1


def test_fetch_trends_non_twitter_platform():
    """Test that non-Twitter platforms return empty trends."""
    input_data = {
        "platforms": ["instagram"],
        "limit": 10
    }

    result = fetch_trends(input_data)

    assert result["trends"] == []
    assert result["source_platforms"] == []
