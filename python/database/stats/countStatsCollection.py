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

statsCollection = db['countStats']

import pandas as pd

from getTimeNow import getDate




def saveStatsDB(stats):
    clearStatsDB()
    return statsCollection.insert_many(stats.to_dict('records'))
    
def getStatsDB():
    
    df =  pd.DataFrame(list(statsCollection.find()))
    
    return df
    
    
def clearStatsDB():
    statsCollection.delete_many({})