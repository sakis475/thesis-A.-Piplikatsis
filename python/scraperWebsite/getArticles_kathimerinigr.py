from bs4 import BeautifulSoup
import requests
import pandas as pd
from checkTimeFormat import checkTimeFormat
import datetime
import sys
import time
import re

import traceback
import logging

sys.path.append('../database/helpers')
from getTimeNow import getDate

def getHttpReq(url, retrys):
    
    r = requests.get(url)
    return r



def getArticleInPage_kathimerinigr():
    
    try:
        source = requests.get('https://feeds.feedburner.com/kathimerini/DJpy').text
    except:
        return pd.DataFrame(), getDate()    
    
    soup = BeautifulSoup(source, 'lxml')
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    for article in soup.find_all('item'):
        
        category = summary = ''
        
        try:
            
            try:
                category = article.category.text.strip()
            except:
                print('Didnt find category')
            
            title = article.title.text.strip()
            link = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",article.text)[0]
            
            #Fri, 29 Oct 2021 19:01:18 +0000
            date = article.pubdate.text.strip()
            
            date = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z') + datetime.timedelta(hours=3)
            date = date.strftime('%Y-%m-%d %H:%M:%S')
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')


            articleLink = requests.get(link).text.strip()
            soupArticleMain = BeautifulSoup(articleLink, 'lxml')
        
        except:
            
            print('error parsing, title or link or summary or date')
            continue
            
            
        try:
            articleText = soupArticleMain.find('div', class_='entry-content').text.strip()
            
            
        except Exception as e:
            #print('cat error: ',category)
            print('title error: ',title)
            logging.error(traceback.format_exc())
            print('#########')
            continue
            
        

        
        data = {'title': title, 'summary': summary, 'date': date, 'category': category, 'link': link, 'article': articleText, 'source': 'kathimerini.gr'}
        df = df.append(data, ignore_index = True )
    
    
    minDate = df['date'].min()
    
    return df, minDate

def getArticles_kathimerinigr(fromDate,limitPage):
    #ta promoted='false' einai auta p mpenun me taksinomhmeno date
    #if(df.loc[filtDateRange].loc[filtPromoted].shape[0] == 0):
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    
    print('%%%%%%%%%%%%%%%%%%%%%%%--kathimerini.gr--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')



    for i in range(0,limitPage):
        #print('at page: ' + str(i+1) + '/' + str(limitPage) )
        singlePagedf, minDateSinglePage = getArticleInPage_kathimerinigr()

        df = df.append(singlePagedf, ignore_index = True )

        try:
            if(minDateSinglePage <= fromDate ):
                print('stopped searching at page: ' + str(i+1))
                break;
        except:
            print('catch date type: ',type(minDateSinglePage))
            print('catch date: ',minDateSinglePage)




    filtDateRange = df['date'] >= fromDate    

    df = df.loc[filtDateRange]
    
    print('Number of articles found: ', df.shape[0])
    
    return df;