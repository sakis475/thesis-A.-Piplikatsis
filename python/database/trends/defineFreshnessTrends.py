


import time, datetime



import pandas as pd



def getTrendsInDateRange(allTrends, dateFrom, dateTill):
    
    
    dateRange = (allTrends['dateDownloaded'] >= dateFrom) & (allTrends['dateDownloaded'] <= dateTill)
    df = allTrends[dateRange]
    
    return df


def defineFreshnessTrends(trends):
    import sys
    sys.path.append('../results')
    sys.path.insert(0, '../helpers')

    from getTimeNow import getDate
    from trendsCollection import getTrendsDB
    
    dateNow_Const = getDate()
    
    allTrends = getTrendsDB()
        
    freshnessDf = pd.DataFrame()
    
    for hashtag in trends['hashtag'].unique():
        
        hashtagMask = allTrends['hashtag'] == hashtag

        freshness = 'noFound' #default

        # 5 - infinity
        dateFrom = dateNow_Const - datetime.timedelta(weeks=1000)
        dateTill = dateNow_Const - datetime.timedelta(days=5)
        gtidr = getTrendsInDateRange(allTrends[hashtagMask], dateFrom, dateTill)
        
        if(gtidr.shape[0] > 0):
            freshness =  'old'
            
            minDate = gtidr['dateDownloaded'].min()
            
            freshnessDf = freshnessDf.append({'hashtag': hashtag, 'freshness_trend': freshness, 'dateDiscovered_trend': minDate}, ignore_index=True)
            
            continue

        # 2 - 5 days
        dateFrom = dateNow_Const - datetime.timedelta(days=5)
        dateTill = dateNow_Const - datetime.timedelta(days=2)
        gtidr = getTrendsInDateRange(allTrends[hashtagMask], dateFrom, dateTill)
        
        if(gtidr.shape[0] > 0):
            freshness =  'recent'
            
            minDate = gtidr['dateDownloaded'].min()
            
            freshnessDf = freshnessDf.append({'hashtag': hashtag, 'freshness_trend': freshness, 'dateDiscovered_trend': minDate}, ignore_index=True)
            
            continue
            
        # 1 - 2 days
        dateFrom = dateNow_Const - datetime.timedelta(days=2)
        dateTill = dateNow_Const - datetime.timedelta(days=1)
        gtidr = getTrendsInDateRange(allTrends[hashtagMask], dateFrom, dateTill)
        
        if(gtidr.shape[0] > 0):
            freshness =  'veryRecent'
            
            minDate = gtidr['dateDownloaded'].min()
            
            freshnessDf = freshnessDf.append({'hashtag': hashtag, 'freshness_trend': freshness, 'dateDiscovered_trend': minDate}, ignore_index=True)
            
            continue
            
        # now - 24 hours
        dateFrom = dateNow_Const - datetime.timedelta(days=1)
        dateTill = dateNow_Const
        gtidr = getTrendsInDateRange(allTrends[hashtagMask], dateFrom, dateTill)
        
        if(gtidr.shape[0] > 0):
            freshness =  'new'
            
            minDate = gtidr['dateDownloaded'].min()
            
            freshnessDf = freshnessDf.append({'hashtag': hashtag, 'freshness_trend': freshness, 'dateDiscovered_trend': minDate}, ignore_index=True)
            
            continue
    
    return pd.merge(freshnessDf, trends, on=['hashtag'])