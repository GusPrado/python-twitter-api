from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import uvicorn
import tweepy
from pymongo import MongoClient
from fastapi import FastAPI

BRAZIL_WOE_ID = 23424768



def get_trends(woe_id: int):
    auth = tweepy.Client(consumer_key='5THZPPUSr4iGGzYggbYXTUcOZ', consumer_secret='eJEtAwFrHQVmUuyo7fWBNa3N9dUv1bwQzz59pP5ajkeGRTyDjv', access_token='140272278-vgIp637jceMX7Vrh7LFvAdluRvSYAs3S2mtZlIJ2', access_token_secret='OYXxcGYxTlIMOCquAV14sSzCsQnssjKOoZfYfJqb666zm')

    api = tweepy.API(auth)
    
    trends = api.trends_place()

    for tweet in trends:
        print(tweet)

app = FastAPI()

@app.get('/trends')
def get_trends_route():
    pass

if __name__ == "__main__":
    trends = get_trends()

    if not trends:
        pass
        #save_trends()

    uvicorn.run(app, host="0.0.0.0", port=8000)