import sys
sys.path.append('../trends')
sys.path.append('../helpers')
sys.path.append('../tweets')
sys.path.append('../results')
sys.path.append('../../getTweets')
from trendsCollection import *
from getTimeNow import *
from tweetsCollection import *
from resultsTopTweets import saveResultsTopTweetsDB

import pandas as pd

import time
import datetime

def findPopularTweetsOfHashtags(constDate):
    latestTrends = getLastTrendsDB()

    tweets = getTweetsDB()

    topTweets = pd.DataFrame()
    for searchQuery in latestTrends['hashtag'].unique():
        df = tweets[tweets['searchQuery'] == searchQuery]
        df = df.sort_values(by=['dateSearched', 'RTCount'], ascending=False).head(4)
        topTweets = topTweets.append(df)

    
    
    #sindew ta top tweets me to bestResultsDate pou einai koino me to resultsLastAll collection!
    topTweets['bestResultsDate'] = constDate 
    
    saveResultsTopTweetsDB(topTweets)