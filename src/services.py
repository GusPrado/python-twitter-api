from typing import Any, Dict, List
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy

def get_trends(woe_id: int) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    
    auth = tweepy.Client(consumer_key='5THZPPUSr4iGGzYggbYXTUcOZ', consumer_secret='eJEtAwFrHQVmUuyo7fWBNa3N9dUv1bwQzz59pP5ajkeGRTyDjv', access_token='140272278-vgIp637jceMX7Vrh7LFvAdluRvSYAs3S2mtZlIJ2', access_token_secret='OYXxcGYxTlIMOCquAV14sSzCsQnssjKOoZfYfJqb666zm')

    api = tweepy.API(auth)
    
    trends = api.get_place_trends(id=woe_id)

    # for tweet in trends:
    #    print(tweet)

    return [trend for trend in trends]