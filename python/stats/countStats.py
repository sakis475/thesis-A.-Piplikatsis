import sys
sys.path.append('../getTopHashtags')
sys.path.append('../database/trends')
sys.path.append('../database/helpers')
sys.path.append('../database/articles')
sys.path.append('../database/tweets')
sys.path.append('../database/results')
sys.path.append('../database/stats')
sys.path.append('../getTweets')
from getLiveTrends import getLiveTrends
from articlesCollection import *
from trendsCollection import *
from getTimeNow import *
from routineCollection import *
from searchTweets import *
from tweetsCollection import *
from bowCosSim import *
from resultsLastCollection import *
from resultsLastAllCollection import *
from countStatsCollection import *


import pandas as pd

sys.path.append('scraperWebsite')
sys.path.append('database/articles')

from getArticles import getALLarticles
import time
import datetime





#epanalamvanomena Trends
def getRepeatedTrends(allResults):
    return allResults[allResults['freshness_trend'] == 'old']['searchQuery'].unique()

def countArticles():
    artCount = getArticlesDB()
    artCount = artCount['link'].unique().shape[0]
    return artCount

def countTweets():
    tweetsCount = getTweetsDB()
    tweetsCount = tweetsCount['tweetID'].unique().shape[0]
    return tweetsCount

def countTrends():
    hashtagCount = getTrendsDB()
    hashtagCount = hashtagCount['hashtag'].unique().shape[0]
    return hashtagCount

def countResults(allResults):
    return allResults['bestResultsDate'].unique().shape[0]





def gatherStats():
    allResults = getResultsLastAllDB()
    stats = pd.DataFrame()
    dataStats = {'countArticles': countArticles(),
                 'countTweets': countTweets(), 'countTrends': countTrends(), 'countResults': countResults(allResults)}
    stats = stats.append(dataStats, ignore_index = True )
    return stats

