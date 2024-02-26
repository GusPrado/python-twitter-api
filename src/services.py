from typing import Any, Dict, List
import tweepy
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from src.constants import BRAZIL_WOE_ID
from src.connections import trends_collection

def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """

    auth = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    
    trends = api.get_place_trends(woe_id)

    # for tweet in trends:
    #    print(tweet)

    return trends[0]['trends']

def get_trends() -> List[Dict[str, Any]]:
    """Get treending topics persisted in MongoDB.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    """Get trends topics and save on MongoDB."""
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)