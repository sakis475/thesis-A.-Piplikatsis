import json
import pandas as pd
from cleanTweets import cleanText
from searchTweets import searchTweets


def getTweets(searchQuery, maxTweets):

    tweetsData = searchTweets(searchQuery, maxTweets)

    tweetsData = cleanText(tweetsData)
    
    return tweetsData