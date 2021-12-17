import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv('dev.env')
import os

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_PORT = int(os.environ.get('DATABASE_PORT') )

#172.17.0.2
client = MongoClient(DATABASE_URL, DATABASE_PORT)

db = client['database']

resultsTopTweetsCollection = db['topTweets']

import pandas as pd

def saveResultsTopTweetsDB(results):
    #clearAllTopTweetsCollection()
    results = results.drop(columns='_id')
    return resultsTopTweetsCollection.insert_many(results.to_dict('records'))

    
def clearAllTopTweetsCollection():
    resultsTopTweetsCollection.delete_many({})