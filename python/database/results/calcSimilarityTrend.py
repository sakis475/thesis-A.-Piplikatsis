from dotenv import load_dotenv
load_dotenv('../../dev.env')
import sys

sys.path.append('../results')
sys.path.append('../trends')
sys.path.append('../helpers')
sys.path.append('../tweets')


from resultsLastAllCollection import *

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.options.mode.chained_assignment = None
#pd.set_option('display.max_colwidth', None)

import time
import datetime

#ευρεση των trends που βρέθηκαν με μεγάλο similarity
def calcSimilarityTrend():
    allResults = getResultsLastAllDB().drop_duplicates(subset='cosSimil')
    dfTemp = allResults[allResults['cosSimil']>100]
    
    highSimTrends = dfTemp['searchQuery'].unique()
    
    highSimArticlesTrends = pd.DataFrame()
    
    for trend in highSimTrends:
        
        trendMask = allResults['searchQuery'] == trend
        maxCosSimilForTrend = allResults[trendMask]
        
        
        maxCosSimil = maxCosSimilForTrend['cosSimil'].max()
        maxCosSimilForTrend = maxCosSimilForTrend[maxCosSimilForTrend['cosSimil'] == maxCosSimil]
    
        highSimArticlesTrends = highSimArticlesTrends.append(maxCosSimilForTrend)
    
    return highSimArticlesTrends.sort_values(by='dateDiscovered_trend', ascending = False).head(50)