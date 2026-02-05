# import os and tweepy for Twitter API access
import os
import tweepy


def fetch_twitter_trends(woeid=1):
    """
    Fetch trending topics from Twitter for a given WOEID (default: 1 for Worldwide).
    Requires Twitter API credentials set as environment variables:
    - TWITTER_API_KEY
    - TWITTER_API_SECRET
    - TWITTER_ACCESS_TOKEN
    - TWITTER_ACCESS_TOKEN_SECRET
    """
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    if not all([api_key, api_secret, access_token, access_token_secret]):
        raise EnvironmentError(
            "Twitter API credentials not set in environment variables.")

    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        trends_result = api.get_place_trends(id=woeid)
        trends = [trend['name'] for trend in trends_result[0]['trends']]
        import os
        from typing import List

        try:
            import tweepy
        except Exception:  # pragma: no cover - import-time fallback
            tweepy = None

        def fetch_twitter_trends(woeid: int = 1) -> List[str]:
            """
            Fetch trending topics from Twitter for a given WOEID (default: 1 for Worldwide).

            Uses Twitter API v1.1 `GET trends/place` via Tweepy. Credentials must be provided
            via environment variables:
              - TWITTER_API_KEY
              - TWITTER_API_SECRET
              - TWITTER_ACCESS_TOKEN
              - TWITTER_ACCESS_TOKEN_SECRET

            Returns a list of trend names. On error, raises an exception.
            """
            if tweepy is None:
                raise RuntimeError(
                    "Tweepy is not installed or failed to import.")

            api_key = os.getenv("TWITTER_API_KEY")
            api_secret = os.getenv("TWITTER_API_SECRET")
            access_token = os.getenv("TWITTER_ACCESS_TOKEN")
            access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

            if not all([api_key, api_secret, access_token, access_token_secret]):
                raise EnvironmentError(
                    "Twitter API credentials not set in environment variables.")

            auth = tweepy.OAuth1UserHandler(
                api_key, api_secret, access_token, access_token_secret)
            api = tweepy.API(auth)

            trends_result = api.get_place_trends(id=woeid)
            if not trends_result or not isinstance(trends_result, (list, tuple)):
                raise ValueError(
                    "Unexpected response from Twitter API when fetching trends")

            try:
                trends = [trend["name"]
                          for trend in trends_result[0].get("trends", [])]
            except Exception as e:
                raise RuntimeError(
                    f"Failed to parse trends response: {e}") from e

            return trends

        if __name__ == "__main__":
            # quick CLI for manual testing
            try:
                print(fetch_twitter_trends(woeid=1))
            except Exception as exc:
                print(f"Error: {exc}")
