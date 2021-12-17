import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv('dev.env')
import os
import datetime

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_PORT = int(os.environ.get('DATABASE_PORT') )


client = MongoClient(DATABASE_URL, DATABASE_PORT)

db = client['database']

topSimilTrendsCollection = db['topSimilTrends']

import pandas as pd

from getTimeNow import getDate




def saveTopSimilTrendsDB(topSimilTrends):
    clearTopSimilTrendsDB()
    return topSimilTrendsCollection.insert_many(topSimilTrends.to_dict('records'))
    
def getTopSimilTrendsDB():
    
    df =  pd.DataFrame(list(topSimilTrendsCollection.find()))
    
    return df
    
    
def clearTopSimilTrendsDB():
    topSimilTrendsCollection.delete_many({})