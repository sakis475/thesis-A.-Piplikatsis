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

tweetsCollection = db['tweets']

import pandas as pd
import datetime
import time
import sys

sys.path.append('../../getTweets')

from searchTweets import *


def saveTweetsDB(tweets):
    
    if getTweetsDB().empty and not tweets.empty:
        tweetsCollection.insert_many(tweets.to_dict('records'))
    elif not tweets.empty:
        
        tweetsUnique = pd.DataFrame()
        tweetsStored = getTweetsDB()
        
        tweetsStored = tweetsStored[tweetsStored['searchQuery'] == tweets['searchQuery'].iloc[0] ]
        
        for tweet in tweets.iterrows():
            try: 
                if tweet[1]['tweetID'] not in tweetsStored['tweetID'].values:
                    tweetsUnique = tweetsUnique.append(tweet[1])
            except FutureWarning:
                tweetsUnique = pd.DataFrame()
                print('FutereWarning except in saveTweetsDB')
                break
                
        if not tweetsUnique.empty:
            tweetsCollection.insert_many(tweetsUnique.to_dict('records'))
        print('saved: ' + str(tweetsUnique.shape[0]) + '/' + str(tweets.shape[0]) )

        

def searchHashtagsWithinDay(trendsTopFive, date):
        
    #search hashtags if there exists within a day in the tweetsDB
    dateTill = date - datetime.timedelta(seconds = 1) #minus 1 seconds to catch that, that already saved
    dateFrom = dateTill - datetime.timedelta(days = 1) #minus 1 day to search back 1 day..
        
    searchQuerys = trendsTopFive['hashtag'].unique()
    tweetsToBeSearched = pd.DataFrame()
    
    
    
    for searchQuery in searchQuerys:
        
        df = getTweetsDB(dateFrom, dateTill, searchQuery)
        
        #yparxoun tweets mesa sto date kai me to searchQuery
        if(not df.empty):
            
            
            if(df.shape[0] < 400):
                querySearchTweets = searchTweets(searchQuery, 400)
                
                #elegxos mhpws ta kainourgia p vrethikan einai perissotera
                if ( querySearchTweets.shape[0] >= df.shape[0] ):
                    #delete pastTweets
                    deleteTweetsOnQuery(searchQuery)
                    
                    tweetsToBeSearched = tweetsToBeSearched.append(querySearchTweets)
                    
                    #kane save ta kainourgia
                    saveTweetsDB(querySearchTweets)
                    print('Found ', df.shape[0], ' old tweets with searchQuery: "', searchQuery, '", replaced with ',  querySearchTweets.shape[0], ' fresh tweets' )
                    
                else:
                    #aband querySearchTweets cause we got less..
                    tweetsToBeSearched = tweetsToBeSearched.append(df)
                    print('Found tweets with searchQuery: "', searchQuery, '", in the DB, numbered to: ', df.shape[0])
                
            else:
                tweetsToBeSearched = tweetsToBeSearched.append(df)
                print('Found tweets with searchQuery: "', searchQuery, '", in the DB, numbered to: ', df.shape[0])
        
        #den yparxoun tweets opote katevase ta
        else:
            
            #time.sleep(5)
            
            
            querySearchTweets = searchTweets(searchQuery, 400)
            saveTweetsDB(querySearchTweets)
            
            tweetsToBeSearched =  tweetsToBeSearched.append(querySearchTweets)
            print('Zero (0) tweets found with searchQuery: "', searchQuery, '", in the DB, downloaded: ', querySearchTweets.shape[0], ' tweets')
            
        print('##################################')
            
            
    return tweetsToBeSearched
        
    
    
def deleteTweetsOnQuery(searchQuery):
    
    searchQuery_queryDB = { "searchQuery": searchQuery}
    tweetsDel = tweetsCollection.delete_many(searchQuery_queryDB)
    print('Deleted ', tweetsDel.deleted_count, ' Tweets with searchQuery: ', searchQuery)
    
    
    
    
    

def getTweetsDB(*args):
    
    if(len(args) >= 2):
        #ex 2021-10-18 00:00:00
        dateFrom = args[0]
        #ex 2021-10-18 08:00:00
        dateTill = args[1]
        
    if(len(args) >= 3):
        searchQuery = args[2]
    
    #get ALL tweets
    df = pd.DataFrame(list(tweetsCollection.find()))
    
    if(df.empty):
        return pd.DataFrame()
    
    if(len(args) == 2):
        
        mask = (df['dateSearched'] >= dateFrom) & (df['dateSearched'] <= dateTill)
        return df[mask]
    
    elif(len(args) == 3):
        
        mask = (df['dateSearched'] >= dateFrom) & (df['dateSearched'] <= dateTill)
        df = df[mask]
        mask2 = df['searchQuery'] == searchQuery
        return df[mask2]
    
    return df
    
    
    
    
def clearAllTweetsDB():
    tweetsCollection.delete_many({})