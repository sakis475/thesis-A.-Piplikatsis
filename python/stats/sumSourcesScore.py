import sys

sys.path.append('../database/results')
sys.path.append('../database/stats')
from resultsLastAllCollection import *
from sourcesScoreCollection import *


import pandas as pd

import time
import datetime



def calcSourcesScore():
    df = getResultsLastAllDB()
    sourcesScore = pd.DataFrame()

    sources = ['protothema.gr','in.gr','kathimerini.gr','skai.gr','enikos.gr']



    for source in sources:



        maskArticle = df['articleSource'] == source
        maskCosLimit = df['cosSimil'] > 35
       # maskCategory = df['articleCategory'].isin(['Πολιτική', 'politics', 'ΠΟΛΙΤΙΚΗ','Κυβέρνηση','Κόμματα','ΕΞΩΤΕΡΙΚΗ ΠΟΛΙΤΙΚΗ','ΚΟΜΜΑΤΑ','ΚΥΒΕΡΝΗΣΗ'])

        dfMasked = df[maskArticle & maskCosLimit]

        numArticles = df[maskArticle].drop_duplicates(subset='articleLink').shape[0]

        #dfMasked = dfMasked[maskCosLimit]

        #dfMasked = dfMasked[maskCategory]


        sourcesScore = sourcesScore.append({'source': source,'cosBigger35': dfMasked.drop_duplicates(subset='articleLink').shape[0], 'countArticlesSource': numArticles, 'perc': dfMasked.drop_duplicates(subset='articleLink').shape[0]/numArticles*100}, ignore_index=True)
        
    return sourcesScore