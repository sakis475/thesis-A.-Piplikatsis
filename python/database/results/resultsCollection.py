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

resultsCollection = db['results']

import pandas as pd

def saveResultsDB(results):
    
    return resultsCollection.insert_many(results.to_dict('records'))

    
def getResultsDB(*args):
    
    if(len(args) == 2):
        trendsTopFive = args[0]
        howManyTop = args[1]
    
    
    #get ALL results
    df = pd.DataFrame(list(resultsCollection.find()))
    
    if(len(args) == 2):
    
        resultsTop5ht = pd.DataFrame()
        for top5ht in trendsTopFive['hashtag'].unique():
            mask = df['searchQuery'] == top5ht
            resultsTop5ht = resultsTop5ht.append(df[mask].sort_values(by='cosSimil', ascending = False).head(howManyTop) )
        return resultsTop5ht
    
    
    return df
    

    
    
    
def clearAllResultDB():
    resultsCollection.delete_many({})