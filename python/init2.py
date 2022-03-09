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


#Προσπαθεί να συνδεθεί με τα ειδησεογραφικά
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
    #Ο χρόνος που η εφαρμογή θα αναμένει μετά το πέρας της ολοκλήρωσεις του κύκλου του
    timeToSleep = 60*30

    #Αν αποτύχει η σύνδεση στα ειδησεογραφικά, τότε περιμένει 5 δευτερόλεπτα και επαναλαμβάνει μέχρι να συνδεθεί.
    try:
        print('Check Internet')
        checkInternetConnection()
    except Exception as e:
        print(e)
        time.sleep(5)
        continue


    try:
        #Η getDate() επιστρέφει την ημερομηνία του συστήματος την στιγμή που καλείται
        startDate = getDate()
        try:
            #Στην init() πραγματοποιείται όλη η διαδικασία της εξόρυξης γνώσης (κατέβασμα άρθρων, τάσεων, tweets και εξαγωγή αποτελεσμάτων)
            results = init()
        except BaseException as error:
            print('Program didnt finish init properly: {}'.format(error))    
            raise NameError('Cant continue, program problem on init')

        #Αποθηκεύει τα αποτελέσματα στο collection resultsLastAll.
        saveResultsLastAllDB(results)


        #Βρίσκει όλες τις τάσεις των αποτελεσμάτων που έχουν βρεθεί με υψηλή συσχέτιση με κάποιο άρθρο και τα αποθηκεύει στην ΒΔ.
        calcSim = calcSimilarityTrend()
        saveTopSimilTrendsDB(calcSim)
        
        #Μετράει και αποθηκεύει στοιχεία της ΒΔ (πλήθος άρθρων, πλήθος tweets, πλήθος κύκλων που έτρεξε το πρόγραμμα, πλήθος μοναδικών τάσεων)
        saveStatsDB(gatherStats())
        
        #Μετράει και αποθηκεύει την βαθμολογία των ειδησεογραφικών
        saveSourcesScoreDB(calcSourcesScore())

        endDate = getDate()

        timeTook = endDate - startDate
        print('Time took: ', timeTook)
        print('Next results at: ', getDate() + datetime.timedelta(minutes=30))

    #Αν κάτι από όλα τα παραπάνω αποτύχει, περιμένει 15 λεπτά και ξαναδοκιμάζει από την αρχή.
    except BaseException as error:
        print('ERROR IN PROGRAM TRYING TO RESTART: {}'.format(error))
        print('sleeping 15 mins')
        timeToSleep = 60*15


   
    time.sleep(timeToSleep)  #Αν ο κύκλος του προγράμματος επιτύχει τότε αναμένει 30 λεπτά και ξαναεκτελείται όλος ο κώδικας κάτω από την while loop μέχρι εδώ.
