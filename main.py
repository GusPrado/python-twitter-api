from typing import List
import uvicorn

from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from src.services import get_trends

class TrendItem(BaseModel):
    name: str
    url: str

BRAZIL_WOE_ID = 23424768

app = FastAPI()

@app.get('/trends', response_model=List[TrendItem])
def get_trends_route():
    trends = get_trends(woe_id=BRAZIL_WOE_ID)

    return trends[0]['trends']

if __name__ == "__main__":

    if not trends:
        pass
        #save_trends()

    uvicorn.run(app, host="0.0.0.0", port=8000)