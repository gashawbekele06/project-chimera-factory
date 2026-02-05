import pytest
from pydantic import BaseModel, ValidationError

# Expected output schema (from specs/skills/fetch_trends/README.md)


class TrendItem(BaseModel):
    name: str
    volume: int
    category: str | None = None


class FetchTrendsOutput(BaseModel):
    trends: list[TrendItem]
    fetched_at: str
    source_platforms: list[str] | None = None

# This test will PASS on mock validation but FAIL on real call (good)


def test_fetch_trends_output_schema_validation():
    mock_output = {
        "trends": [
            {"name": "#EthiopiaFashion", "volume": 45000, "category": "fashion"},
            {"name": "#AddisStyle", "volume": 32000}
        ],
        "fetched_at": "2026-02-05T10:00:00Z",
        "source_platforms": ["twitter"]
    }

    # Validate mock → should pass (this is just schema check)
    validated = FetchTrendsOutput(**mock_output)
    assert len(validated.trends) == 2
    assert validated.fetched_at is not None

# This test MUST fail until fetch_trends is implemented


def test_fetch_trends_function_exists_and_returns_valid_data():
    input_data = {
        "platforms": ["twitter"],
        "region": "ET",
        "limit": 10
    }

    # The real call — this line will raise NameError if function missing
    result = fetch_trends(input_data)  # ← This MUST raise NameError now

    # If it somehow reaches here (impossible now), validate
    validated = FetchTrendsOutput(**result)
    assert isinstance(validated.trends, list)
    assert len(validated.trends) > 0
