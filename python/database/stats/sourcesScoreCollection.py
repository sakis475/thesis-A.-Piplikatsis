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

sourcesScoreCollection = db['sourcesScore']

import pandas as pd

from getTimeNow import getDate




def saveSourcesScoreDB(stats):
    clearSourcesScoreDB()
    return sourcesScoreCollection.insert_many(stats.to_dict('records'))
    
def getSourcesScoreDB():
    
    df =  pd.DataFrame(list(sourcesScoreCollection.find()))
    
    return df
    
    
def clearSourcesScoreDB():
    sourcesScoreCollection.delete_many({})