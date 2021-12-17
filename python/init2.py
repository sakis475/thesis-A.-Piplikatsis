##
#DOCKER PYTHON SCRIPT
########

from init import init
import sys
sys.path.append('database/results')
sys.path.append('database/helpers')
sys.path.append('database/stats')
sys.path.append('stats')
from resultsCollection import *
from timeScriptStoppedCollection import *
from resultsLastCollection import *
from resultsLastAllCollection import *
from getTimeNow import getDate
from findPopularTweets import findPopularTweetsOfHashtags
from calcSimilarityTrend import *
from topSimilTrendsCollection import *


from countStatsCollection import *
from countStats import *

from sourcesScoreCollection import *
from sumSourcesScore import *

import pandas as pd
pd.options.mode.chained_assignment = None

import time, datetime

import traceback
import logging

def checkInternetConnection():
    import requests
    urls = ['https://www.skai.gr','https://www.protothema.gr', 'https://feeds.feedburner.com/kathimerini/DJpy','https://www.in.gr', 'https://www.enikos.gr']

    timeout = 5

    try:
        for url in urls:
            requests.get(url, timeout=timeout)
        print('Connection succesfull to all endpoints!')
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection, or a website is failing")
        print(exception)
        raise NameError('No internet connection, or a website is failing')
        
        
        
        
while True:

    timeToSleep = 60*30

    try:
        print('Check Internet')
        checkInternetConnection()
    except Exception as e:
        print(e)
        time.sleep(5)
        continue

    

    

    

    try:
        

        startDate = getDate()
        try:
            results = init()
        except BaseException as error:
            print('Program didnt finish init properly: {}'.format(error))    
            raise NameError('Cant continue, program problem on init')

        #kane save ta apotelesmata
        #kane merge ta topTrends pu vrethikan kai ta info tus
        #kane merge to diffDate
        #apothikeuse ta sto resultsLastAll
        saveResultsLastAllDB(results)


        #find trends found with high similarity
        #and save them to DB
        calcSim = calcSimilarityTrend()
        saveTopSimilTrendsDB(calcSim)
        
        #save countStats
        saveStatsDB(gatherStats())
        
        #save sumSourcesScore
        saveSourcesScoreDB(calcSourcesScore())

        endDate = getDate()

        timeTook = endDate - startDate
        print('Time took: ', timeTook)
        print('Next results at: ', getDate() + datetime.timedelta(minutes=30))

    except BaseException as error:
        print('ERROR IN PROGRAM TRYING TO RESTART: {}'.format(error))
        saveScriptStoppedDateDB(getDate())
        print('sleeping 15 mins')
        timeToSleep = 60*15



    time.sleep(timeToSleep)
