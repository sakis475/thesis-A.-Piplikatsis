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

def getArticleInPage_protothemagr(page):
    
    try:
        source = requests.get('https://www.protothema.gr/oles-oi-eidiseis/?pg='+str(page)+'&$component=Main[0]').text
    except:
        return pd.DataFrame(), getDate()
        
    soup = BeautifulSoup(source, 'lxml')
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    for article in soup.find_all('div', class_= 'article'):
        
        ignore_categories = ['ygeiamou.gr', 'English News', 'Olivemagazine', 'Best of network','Marie Claire','Travel.gr','for Electric']
        if (article.find('a', class_='categ').text.strip() in ignore_categories):
            continue
        else:
            category = article.find('a', class_='categ').text.strip()
        
        try:
            title = article.find('div', class_='heading').a.text.strip()
        except:
            title = ''
            continue
            
        try:
            summary = article.find('p').text.strip()
            link = article.find('div', class_='heading').a['href']


            date = article.find('time').text.strip()
            date = datetime.datetime.strptime(date, '%d/%m/%Y, %H:%M')
            date = date.strftime('%Y-%m-%d %H:%M:%S')
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            articleLink = requests.get(link).text.strip()
        except:
            continue
        
        soupArticleMain = BeautifulSoup(articleLink, 'lxml')
        try:
            articleText = soupArticleMain.find('div', class_='cntTxt').text.strip();
        except:
            continue
            print('cat error: ',category)
            print('title error: ',title)
            print('#########')

        
        data = {'title': title, 'summary': summary, 'date': date, 'category': category, 'link': link, 'article': articleText, 'source': 'protothema.gr'}
        df = df.append(data, ignore_index = True )
    
    
    minDate = df['date'].min()
    
    return df, minDate

def getArticles_protothemagr(fromDate,limitPage):
    #ta promoted='false' einai auta p mpenun me taksinomhmeno date
    #if(df.loc[filtDateRange].loc[filtPromoted].shape[0] == 0):
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    
    print('%%%%%%%%%%%%%%%%%%%%%%%--protothema.gr--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')



    for i in range(0,limitPage):
        print('at page: ' + str(i+1) + '/' + str(limitPage) )
        singlePagedf, minDateSinglePage = getArticleInPage_protothemagr(str(i+1))

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