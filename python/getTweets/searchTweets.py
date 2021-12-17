#syllegei Tweets gia th frash pu thelume (query), kai trofodotei 
#me append to tweetsData me to plhtmos tweets (max_tweets) p thelume

#7 requests/100 tweets, 180 requests/15min
import pandas as pd
import datetime


import time
import re

import sys
sys.path.append('../database/helpers')
from getTimeNow import *

def logging(e):
    import logging
    import os

    logFile = 'sample.log'
    logging.basicConfig( filename = logFile,filemode = 'w',level = logging.DEBUG,format = '%(asctime)s - %(levelname)s: %(message)s',\
                         datefmt = '%m/%d/%Y %I:%M:%S %p' )

    logging.debug(e)


def handleAuthTweeterAndSearch(query, max_tweets):
    
    import tweepy
    auth = tweepy.OAuthHandler("4GqyMasQ288NdY6HhBo0HqRus", "8TJMxkatgFFaH7OM3S8KeqTml5PXg5GL8EzpWZPhYW8P2BGHJ2")
    auth.set_access_token("833696769884160003-QMJy73JFNVt2fWVPmQ1YlXKi7TdfoqF", "hvjZJwwAUQdmVE1oFmr1wLTeCtCcmy15c0ADdWU0EOCvH")

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    #tweepy.debug(False)
    time.sleep(1)
    searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=query+'-filter:retweets', result_type="recent", tweet_mode="extended", lang='el').items(max_tweets)]
    
    return searched_tweets




def searchTweets(query, max_tweets):
    
    tweetsData = pd.DataFrame()
    
    try:
        
        searched_tweets = handleAuthTweeterAndSearch(query, max_tweets)
        
    except Exception as e:
        #second try
        time.sleep(30)
        searched_tweets = handleAuthTweeterAndSearch(query, max_tweets)
        
        logging(e)
        

    
    
    
    for searchFound in searched_tweets:
        # pairnw to full_text aneksartita an einai tweet h retweet
        search_tweetsFullText = searchFound["full_text"];
        search_tweetID = searchFound["id_str"];
        created_at = searchFound["created_at"]
        created_at = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')
        created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        dateSearched = getDate()
        
        # elegxw an einai tweet h retweet gia na parw to full_text kai oxi to truncated
        if search_tweetsFullText[0:2] != "RT":
            hashtags = re.findall("([#][\w_-]+)",search_tweetsFullText)
            tweetsData = tweetsData.append({'dateSearched': dateSearched, "date": created_at,"fullText": search_tweetsFullText, "tweetID": search_tweetID, "userID": searchFound["user"]["id_str"], "userScreenName": searchFound["user"]["screen_name"], "RT": False, "RTCount": searchFound["retweet_count"], "searchQuery": query, "hashtags": hashtags},ignore_index=True,sort=False)
        elif search_tweetsFullText[0:2] == "RT":
            searchHelper = searchFound["retweeted_status"]["full_text"]
            hashtags = re.findall("([#][\w_-]+)",searchHelper)
            tweetsData = tweetsData.append({"dateSearched": dateSearched,"date": created_at, "fullText": searchHelper, "tweetID": search_tweetID, "userID": searchFound["user"]["id_str"], "userScreenName": searchFound["user"]["screen_name"], "RT": True, "RTCount": searchFound["retweet_count"], "searchQuery": query, "hashtags": hashtags},ignore_index=True,sort=False)
        else:
            print("error thanos..")
    return tweetsData;