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
        return trends
    except Exception as e:
        print(f"Error fetching Twitter trends: {e}")
        return []
