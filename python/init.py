import sys
sys.path.append('getTopHashtags')
sys.path.append('database/trends')
sys.path.append('database/helpers')
sys.path.append('database/articles')
sys.path.append('database/tweets')
sys.path.append('database/results')
sys.path.append('getTweets')
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

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.options.mode.chained_assignment = None

sys.path.append('scraperWebsite')
sys.path.append('database/articles')

from getArticles import getALLarticles
import time
import datetime

#elegxos an vrethike kainourgio TREND poy den yparxei sta results
#!opote prepei na ginei deep search sta articles!
def trendForDeepSearch(constDate, trendsTopFive):
    
    fromDate_results = constDate - datetime.timedelta(days = 7)
    tillDate_results = constDate
    
    threeDaysBackresults = getResultsLastAllDB(fromDate_results, tillDate_results)
    if(threeDaysBackresults.empty):
        return trendsTopFive['hashtag'].unique()
    
    trendToDeepSearch = []
    for trend in trendsTopFive['hashtag'].unique():
        if(not (trend in threeDaysBackresults['searchQuery'].unique()) ):
            #den yparxei to trend p vrethike twra, sta results!
            trendToDeepSearch.append(trend)
    return trendToDeepSearch

def init():
    
    constDate = getDate()
    
    
    ### get hashtags ####
    trendsTopFive = getLiveTrends().sort_values(by=['rank']).head(5)
    saveTrendsDB(trendsTopFive)
    

    #### get tweets ####
    tweetsToSearch = searchHashtagsWithinDay(trendsTopFive, trendsTopFive['dateDownloaded'].iloc[0])

    ###### DOWNLOAD articles ####

    #to date orio pou tha psaksei 'fromDate' pisw sta arthra
    fromDate_lastDownloadArticles = getArticleDownloadDateLAST_DB() - datetime.timedelta(hours = 2)

    articles = getALLarticles(fromDate_lastDownloadArticles)

    #to date pou ksekinisa na psaxnw arthra twra (apothikeush sto DB)
    saveArticleDownloadDateDB( constDate )

    saveArticlesDB(articles)

    #main job,
    #for all trends
    #get latest tweets
    #and for each source compare the trends
    results = pd.DataFrame()
    trendListDeepSearch = trendForDeepSearch(constDate , trendsTopFive)
    for searchQuery in trendsTopFive['hashtag'].unique():

        groupTweetsOfHashtag = tweetsToSearch[tweetsToSearch['searchQuery'] == searchQuery]

        #an einai true tote psaxnei pisw x meres sta arthra
        #deep search
        if(searchQuery in trendListDeepSearch):
            print('DOING DEEP SEARCH FOR "', searchQuery, '"')
            fromDate = constDate - datetime.timedelta(days = 3)
            TillDate = constDate
        else:
            fromDate = fromDate_lastDownloadArticles
            TillDate = constDate

        #get all articles from all sources within date range, (TillDate actually means till Now Date, and fromDate how back in time, to get articles)    
        articles = getArticlesDB(fromDate,TillDate).sort_values(by='date')

        for source in articles['source'].unique():
                print('source: ', source, ', searchQuery: ', searchQuery)
                try:
                    similResult = similarity(articles[articles['source'] == source], groupTweetsOfHashtag, searchQuery) #note: every time article date range might change, cause of trendToDeepSearch
                except Exception as e:
                    print('source ', source, ' with searchQuery: ', searchQuery, ', propably something wrong with tweet clean..', e)
                    print('skipping')
                    continue

                similResult['resultCompletedDate'] = constDate

                results = results.append(similResult)







    results_all_sources = pd.DataFrame()

    sources = ['protothema.gr', 'enikos.gr', 'in.gr', 'kathimerini.gr', 'skai.gr']
    searchQuerysToSearch = getLastTrendsInListDB()
    for articleSource in sources:
        for searchQuery in searchQuerysToSearch:

            results_source = pd.DataFrame()

            results_source = results[results['articleSource'] == articleSource]

            results_source = results_source[results_source['searchQuery'] == searchQuery]

            results_source = results_source.sort_values(by='cosSimil', ascending = False).head(1)

            results_all_sources = results_all_sources.append(results_source, ignore_index=True)
    
    
    return results_all_sources

#results
#results.sort_values(by='cosSimil', ascending = False)