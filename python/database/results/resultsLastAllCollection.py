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

resultsLastAllCollection = db['resultsLastAll']
import sys
sys.path.append('database/trends')
sys.path.append('database/helpers')
from trendsCollection import *
from getTimeNow import *

import pandas as pd
from findPopularTweets import findPopularTweetsOfHashtags

def saveResultsLastAllDB(results):
    
    constDate = getDate()
    
    #dinei sta results ta info (columns) twn trends
    results = pd.merge(results, getLastTrendsDB().rename(columns = {'hashtag':'searchQuery'}), on='searchQuery').drop(columns='_id')
    
    
    #diffDate, if articleDate is later than dateDiscovered_trend -> that means trend appeared diffDate earlier
    results['diffDate'] = results['articleDate'] - results['dateDiscovered_trend']
    results['diffDate'] = results['diffDate'].apply(str)
    
    try:
        #results not older that x day
        allResults = getResultsLastAllDB(getDate() - datetime.timedelta(days=7) , getDate()).drop(columns=['_id']).append(results, ignore_index=True)
    except:
        #propably emprt results db
        results['bestResultsDate'] = constDate
        findPopularTweetsOfHashtags(constDate)
        return resultsLastAllCollection.insert_many(results.to_dict('records'))
        
        
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
  
    allResultsBestCos['bestResultsDate'] = constDate
    
    findPopularTweetsOfHashtags(constDate)
    
    return resultsLastAllCollection.insert_many(allResultsBestCos.to_dict('records'))

def getResultsLastAllDB(*args):
    
    
    
    if(len(args) == 2):
        #ex 2021-10-18 00:00:00
        dateFrom = args[0]
        #ex 2021-10-18 08:00:00
        dateTill = args[1]
    
    
    
    df =  pd.DataFrame(list(resultsLastAllCollection.find()))
    
    if(df.empty):
        return pd.DataFrame()
    
    if(len(args) == 2):
        
        mask = (df['resultCompletedDate'] >= dateFrom) & (df['resultCompletedDate'] <= dateTill)
        return df[mask]
    
   
    
    return df;