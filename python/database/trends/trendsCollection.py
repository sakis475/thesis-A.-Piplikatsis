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

trendsCollection = db['trends']

import pandas as pd

from defineFreshnessTrends import defineFreshnessTrends


def saveTrendsDB(trends):
    trends['hashtag'] = trends['hashtag'].str.lower()
    return trendsCollection.insert_many(trends.to_dict('records'))
    
def getTrendsDB(*args):
    if(len(args) == 2):
        #ex 2021-10-18 00:00:00
        dateFrom = args[0]
        #ex 2021-10-18 08:00:00
        dateTill = args[1]
        
        
    df = pd.DataFrame(list(trendsCollection.find()))
    
    if(len(args) == 2):
        
        mask = (df['dateDownloaded'] >= dateFrom) & (df['dateDownloaded'] <= dateTill)
        return df[mask]
    
    
    df['hashtag'] = df['hashtag'].str.lower()
    
    return df

#vres ta trends an emfanizontai syxna h oxi, pote protoemfanisthkan
#def findAppearanceOfTrend():

def getLastTrendsInListDB():
    df = getTrendsDB()
    df = df[df['dateDownloaded'] == df['dateDownloaded'].max()]
    return df['hashtag'].unique()
    
    
def getLastTrendsDB():
    
    df = getTrendsDB()
    
    df = df[df['dateDownloaded'] == df['dateDownloaded'].max()]
    
    df = defineFreshnessTrends(df)
    
    return df

def clearAllTrendsDB():
    trendsCollection.delete_many({})