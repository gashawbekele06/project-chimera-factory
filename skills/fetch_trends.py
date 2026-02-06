from typing import Dict, Any, List, Optional
import os
import datetime

try:
    import tweepy
except Exception as e:
    tweepy = None


def _require_tweepy():
    if tweepy is None:
        raise ImportError(
            "tweepy is required to fetch Twitter trends. Install with: pip install tweepy"
        )


def fetch_trends(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Fetch trending topics from Twitter.

    Expects `input_data` keys (optional):
      - platforms: list[str] (defaults to ['twitter'])
      - region: str (ISO country code like 'ET' or a country name)
      - limit: int (max number of trends to return)

    Requires these environment variables to be set for Twitter API v1.1 access:
      - TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

    Returns a dict matching the tests' expected schema:
      {"trends": [{"name": str, "volume": int, "category": Optional[str]}],
       "fetched_at": ISO8601 UTC str,
       "source_platforms": ["twitter"]}
    """
    _require_tweepy()

    platforms: List[str] = input_data.get(
        "platforms", ["twitter"]) or ["twitter"]
    if "twitter" not in [p.lower() for p in platforms]:
        return {"trends": [], "fetched_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z", "source_platforms": []}

    # Read credentials from environment
    consumer_key = os.environ.get(
        "TWITTER_API_KEY") or os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get(
        "TWITTER_API_SECRET") or os.environ.get("TWITTER_CONSUMER_SECRET")
    access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
    access_secret = os.environ.get("TWITTER_ACCESS_SECRET")

    if not all([consumer_key, consumer_secret, access_token, access_secret]):
        raise RuntimeError(
            "Twitter API credentials missing. Set TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET"
        )

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    region = input_data.get("region")
    limit = int(input_data.get("limit", 10) or 10)

    try:
        # Find a location WOEID for the requested region when possible
        woeid = 1  # default global
        try:
            locations = api.trends_available()
            selected = None
            if region:
                for loc in locations:
                    if loc.get("countryCode") == region or loc.get("country") == region or loc.get("name") == region:
                        selected = loc
                        break
                if not selected:
                    for loc in locations:
                        country = (loc.get("country") or "").lower()
                        if region.lower() in country:
                            selected = loc
                            break
            if selected:
                woeid = selected.get("woeid", 1)
        except Exception:
            # If trends_available fails, fall back to global
            woeid = 1

        trends_resp = api.trends_place(woeid)
        raw_trends = trends_resp[0]["trends"] if trends_resp and len(
            trends_resp) > 0 else []

        results: List[Dict[str, Any]] = []
        for t in raw_trends[:limit]:
            name = t.get("name")
            volume = t.get("tweet_volume") or 0
            try:
                volume = int(volume)
            except Exception:
                volume = 0
            results.append({"name": name, "volume": volume, "category": None})

        return {
            "trends": results,
            "fetched_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
            "source_platforms": ["twitter"],
        }
    except Exception as exc:
        raise RuntimeError(f"Error fetching Twitter trends: {exc}") from exc
