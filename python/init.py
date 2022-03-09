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

#Ελέγχει αν βρέθηκαν καινούργιες τάσεις που δεν υπάρχει αποθηκευμένη στην ΒΔ και τις επιστρέφει
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
    
    
    #Κατεβαίνουν οι πρώτες πέντε τάσεις από το Twitter API

    ### get hashtags ####
    trendsTopFive = getLiveTrends().sort_values(by=['rank']).head(5)
    saveTrendsDB(trendsTopFive)
    

    #Κατεβαίνουν tweets για αυτές τις πρώτες πέντε τάσεις

    #### get tweets ####
    tweetsToSearch = searchHashtagsWithinDay(trendsTopFive, trendsTopFive['dateDownloaded'].iloc[0])



    ###### DOWNLOAD articles ####

    #Η μεταβλητή επιλέγει πόσο πίσω να ψάξει για άρθρα στα ειδησεογραφικά με βάση την προηγούμενη φορά που κατέβασε άρθρα.
    fromDate_lastDownloadArticles = getArticleDownloadDateLAST_DB() - datetime.timedelta(hours = 2)


    #Αποθηκεύονται όλα τα άρθρα στην μεταβλητή articles
    articles = getALLarticles(fromDate_lastDownloadArticles)

    #Αποθήκευση της ημερομηνίας που κατέβηκαν μόλις τώρα τα άρθρα.
    saveArticleDownloadDateDB( constDate )
    #Αποθήκευση των άρθρων που κατέβηκαν στην ΒΔ.
    saveArticlesDB(articles)



    ########### ΚΥΡΙΑ ΔΙΕΡΓΑΣΙΑ ####################
   

    #Αρχικά αρχικοποιείται ένα άδειο dataframe που στην συνέχεια θα γεμίσει με τα αποτελέσματα του αλγόριθμου
    results = pd.DataFrame()

   
    trendListDeepSearch = trendForDeepSearch(constDate , trendsTopFive)

    #Για κάθε τάση, παίρνει τα tweets της και τα συγκρίνει με όλα τα άρθρα
    for searchQuery in trendsTopFive['hashtag'].unique():

        groupTweetsOfHashtag = tweetsToSearch[tweetsToSearch['searchQuery'] == searchQuery]

        #Οι τάσεις που είναι καινούργιες για την εφαρμογή κάνουν εξοχυνιστική αναζήτηση σε άρθρα έως τρεις ημέρες πίσω.
        #Αλλιώς αν είναι τάση που έχει ξανασυγκριθεί με άρθρα τοτε γίνεται αναζήτηση μόνο στα νεοσυλλεχθέντα άρθρα.
        if(searchQuery in trendListDeepSearch):
            print('DOING DEEP SEARCH FOR "', searchQuery, '"')
            fromDate = constDate - datetime.timedelta(days = 3)
            TillDate = constDate
        else:
            fromDate = fromDate_lastDownloadArticles
            TillDate = constDate

        
        articles = getArticlesDB(fromDate,TillDate).sort_values(by='date')

        for source in articles['source'].unique():
                print('source: ', source, ', searchQuery: ', searchQuery)
                try:

                    #Επιστρέφονται τα αποτελέσματα από την συσχέτιση άρθρων της δοθείσας πηγής ειδησεογραφικου (μία από τις πέντε, από την αρχή με την σειρά) και τα tweets μίας τάσης
                    similResult = similarity(articles[articles['source'] == source], groupTweetsOfHashtag, searchQuery) 
                except Exception as e:
                    print('source ', source, ' with searchQuery: ', searchQuery, ', propably something wrong with tweet clean..', e)
                    print('skipping')
                    continue

                similResult['resultCompletedDate'] = constDate

                results = results.append(similResult)






    #Ένα τελευταίο φιλτράρισμα στα αποτελέσματα.
    #Για όλες τις πηγές ειδησεογραφικών, και για όλες τις διαφορετικές τάσεις επιλέγεται αυτό με το καλύτερο αποτέλεσμα
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

    ########### ΤΕΛΟΣ ΚΥΡΙΑΣ ΔΙΕΡΓΑΣΙΑΣ ####################

