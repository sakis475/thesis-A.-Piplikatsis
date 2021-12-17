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

articleDownloadDateCollection = db['articleDownloadDate']

import pandas as pd

from getTimeNow import getDate

def saveArticleDownloadDateDB(articleDownloadDate):
    return articleDownloadDateCollection.insert_one({'lastTimeArticle': articleDownloadDate})
    
def getArticleDownloadDateDB():
    
    df =  pd.DataFrame(list(articleDownloadDateCollection.find()))
    
    if (df.empty):
        saveArticleDownloadDateDB(getDate() - datetime.timedelta(days=2))
        
    df =  pd.DataFrame(list(articleDownloadDateCollection.find()))
    
    return df
    
def getArticleDownloadDateLAST_DB():
    return getArticleDownloadDateDB().sort_values(by='lastTimeArticle', ascending= False).head(1)['lastTimeArticle'].item()
    
    
    
def clearArticleDownloadDateDB():
    articleDownloadDateCollection.delete_many({})