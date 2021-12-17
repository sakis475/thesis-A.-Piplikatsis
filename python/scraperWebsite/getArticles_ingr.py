from bs4 import BeautifulSoup
import requests
import pandas as pd
from checkTimeFormat import checkTimeFormat
import datetime
import sys
import time

sys.path.append('../database/helpers')
from getTimeNow import getDate

def getHttpReq(url, retrys):
    
    r = requests.get(url)
    return r

def getArticleInPage_ingr(page):
    try:
        source = requests.get('https://www.in.gr/latestnews/page/'+str(page) ).text
    except:
        return pd.DataFrame(), getDate()    
    
    soup = BeautifulSoup(source, 'lxml')
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    for article in soup.find_all('a', class_= 'relative-title'):
        
        ignore_categories = ['English edition']
        
        try:
            if (article.find('span', class_='vinieta').text.strip() in ignore_categories):
                continue
            else:
                category = article.find('span', class_='vinieta').text.strip()
        except:
            continue
        
        
        try:
            title = article.h3.text.strip()
            summary = article.p.text.strip()

            date = article.find('span', class_='post-meta').text.strip()
            date = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
            date = date.strftime('%Y-%m-%d %H:%M:%S')
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

            link = article['href']

            articleLink = requests.get(link).text.strip()
            soupArticleMain = BeautifulSoup(articleLink, 'lxml')

            articleText = soupArticleMain.find(attrs={"itemprop" : "articleBody"}).text;
        except:
            continue
        
        data = {'title': title, 'summary': summary, 'date': date, 'category': category, 'link': link, 'article': articleText, 'source': 'in.gr'}
        df = df.append(data, ignore_index = True )
        
    minDate = df['date'].min()
        
    return df, minDate

def getArticles_ingr(fromDate,limitPage):
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    
    print('%%%%%%%%%%%%%%%%%%%%%%%--in.gr--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    

    for i in range(0,limitPage):
        print('at page: ' + str(i+1) + '/' + str(limitPage) )
        singlePagedf, minDateSinglePage = getArticleInPage_ingr(str(i+1))

        df = df.append(singlePagedf, ignore_index = True )

        try:
            if(minDateSinglePage <= fromDate ):
                print('stopped searching at page: ' + str(i+1))
                break;
        except:
            print(type(minDateSinglePage))
            print(minDateSinglePage)




    filtDateRange = df['date'] >= fromDate    

    df = df.loc[filtDateRange]
    
    print('Number of articles found: ', df.shape[0])
    
    return df;