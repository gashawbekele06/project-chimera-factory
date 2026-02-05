import os


def test_fetch_twitter_trends_v1_monkeypatched(monkeypatch):
    # Provide fake credentials
    monkeypatch.setenv("TWITTER_API_KEY", "key")
    monkeypatch.setenv("TWITTER_API_SECRET", "secret")
    monkeypatch.setenv("TWITTER_ACCESS_TOKEN", "token")
    monkeypatch.setenv("TWITTER_ACCESS_TOKEN_SECRET", "tokensecret")

    # Create a dummy API object
    class DummyAPI:
        def get_place_trends(self, id):
            return [{"trends": [{"name": "#one"}, {"name": "#two"}]}]

    # Monkeypatch tweepy classes used in the module
    import types

    dummy_tweepy = types.SimpleNamespace()
    dummy_tweepy.OAuth1UserHandler = lambda a, b, c, d: None
    dummy_tweepy.API = lambda auth: DummyAPI()

    monkeypatch.setitem(__import__("sys").modules, "tweepy", dummy_tweepy)

    from skills.fetch_trends import fetch_twitter_trends

    trends = fetch_twitter_trends(woeid=1)
    assert trends == ["#one", "#two"]
