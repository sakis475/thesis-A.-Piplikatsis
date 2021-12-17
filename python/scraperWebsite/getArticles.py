from getArticles_ingr import getArticles_ingr
from getArticles_kathimerinigr import getArticles_kathimerinigr
from getArticles_protothemagr import getArticles_protothemagr
from getArticles_skaigr import getArticles_skaigr
from getArticles_enikosgr import getArticles_enikosgr

import sys

sys.path.append('../database/helpers')

from getTimeNow import getDate
import datetime
import pandas as pd
pd.set_option('display.max_rows', 500)



def getALLarticles(fromDate):
    
    allArticles = pd.DataFrame()
    
    ingr = getArticles_ingr(fromDate, 50)
    kathim = getArticles_kathimerinigr(fromDate, 1)
    proto = getArticles_protothemagr(fromDate, 50)
    skai = getArticles_skaigr(fromDate, 50)
    enikos = getArticles_enikosgr(fromDate, 50)
    
    allArticles = allArticles.append([ingr,kathim,proto,skai,enikos])
    
    return allArticles