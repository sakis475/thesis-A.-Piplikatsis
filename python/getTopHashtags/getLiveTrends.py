import tweepy
import pandas as pd
import datetime
import time

auth = tweepy.OAuthHandler("4GqyMasQ288NdY6HhBo0HqRus", "8TJMxkatgFFaH7OM3S8KeqTml5PXg5GL8EzpWZPhYW8P2BGHJ2")
auth.set_access_token("833696769884160003-QMJy73JFNVt2fWVPmQ1YlXKi7TdfoqF", "hvjZJwwAUQdmVE1oFmr1wLTeCtCcmy15c0ADdWU0EOCvH")

api = tweepy.API(auth)

def getLiveTrends():
    # to count exei orio 100 tweets
    dfTrends = pd.DataFrame()
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')

    # thesaloniki 963291
    # athina 946738
    # ellada 23424833

    trendsNow = api.trends_place("23424833")[0]['trends']

    for i, trend in enumerate(trendsNow):
        dfTrends = dfTrends.append({"rank": (i + 1),"dateDownloaded": created_at, "hashtag": trend["name"], "volume": trend['tweet_volume']},ignore_index=True)
    
    #filtHashtagOnly = dfTrends['hashtag'].str.startswith('#', na=False)
    #dfTrends = dfTrends[filtHashtagOnly]
    
    return dfTrends.drop_duplicates(subset='hashtag',ignore_index=True)

