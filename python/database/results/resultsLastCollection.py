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

resultsLastCollection = db['resultsLast']


import sys
sys.path.append('database/results')
sys.path.append('database/trends')
sys.path.append('database/helpers')
from getTimeNow import getDate
from trendsCollection import *
from resultsLastAllCollection import *
import pandas as pd

import datetime



def clearAllTopResults():
    resultsLastCollection.delete_many({})
    
def getResultsLastDB():
    #get last results
    return pd.DataFrame(list(resultsLastCollection.find()))

def saveResultsLastDB():
    
    #results not older that x day
    allResults = getResultsLastAllDB(getDate() - datetime.timedelta(days=7) , getDate()).drop(columns=['_id'])
    
    latestDateHashtags = getLastTrendsInListDB()
    
    
    sources = ['protothema.gr', 'enikos.gr', 'in.gr', 'kathimerini.gr', 'skai.gr']
    allResultsBestCos = pd.DataFrame()
    for searchQuery in latestDateHashtags:
        for source in sources:
            #re-initialize to nothing every time
            searQuerArtSource = pd.DataFrame()
            #take only the selected searchQuery
            searQuerArtSource = allResults[allResults['searchQuery'] == searchQuery]
            #from that searchquery take the selected searchQuery
            searQuerArtSource = searQuerArtSource[searQuerArtSource['articleSource'] == source]
            #take the max cosSimil of this source and searchQuery
            searQuerArtSource = searQuerArtSource.sort_values(by='cosSimil', ascending=False).head(1)
            #append that result
            allResultsBestCos = allResultsBestCos.append(searQuerArtSource)


    
    clearAllTopResults()
    return resultsLastCollection.insert_many(allResultsBestCos.to_dict('records'))
    