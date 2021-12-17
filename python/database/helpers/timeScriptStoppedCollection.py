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

scriptStoppedCollection = db['scriptStopped']

import pandas as pd

from getTimeNow import getDate

def saveScriptStoppedDateDB(timeStopped):
    return scriptStoppedCollection.insert_one({'lastTimeStopped': timeStopped})
    
def getScriptStoppedDateDB():

    df =  pd.DataFrame(list(scriptStoppedCollection.find()))
    
    return df
    
def getScriptStoppedDateLAST_DB():
    return getScriptStoppedDateDB().sort_values(by='lastTimeStopped', ascending= False).head(1)['lastTimeStopped'].item()
    
    
    
def clearScriptStoppedDateDB():
    scriptStoppedCollection.delete_many({})