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

articlesCollection = db['articles']

import pandas as pd

def saveArticlesDB(articles):
    articles = articles.drop_duplicates()
    if getArticlesDB().empty and not articles.empty:
        articlesCollection.insert_many(articles.to_dict('records'))
    elif not articles.empty:
        
        articlesUnique = pd.DataFrame()
        articlesStored = getArticlesDB()
        for article in articles.iterrows():
            if article[1]['link'] not in articlesStored['link'].unique():
                articlesUnique = articlesUnique.append(article[1])
        
        if not articlesUnique.empty:
            articlesCollection.insert_many(articlesUnique.to_dict('records'))
        print('new articles saved in DB: ' + str(articlesUnique.shape[0]) + '/' + str(articles.shape[0]), ' of articles downloaded now')

    
def getArticlesDB(*args):
    
    if(len(args) == 2):
        #ex 2021-10-18 00:00:00
        dateFrom = args[0]
        #ex 2021-10-18 08:00:00
        dateTill = args[1]
    
    
    
    #get ALL articles
    df = pd.DataFrame(list(articlesCollection.find()))
    
    
    
    if(len(args) == 2):
        
        mask = (df['date'] >= dateFrom) & (df['date'] <= dateTill)
        return df[mask]
    
    
    return df
    

def clearAllArticlesDB():
    articlesCollection.delete_many({})