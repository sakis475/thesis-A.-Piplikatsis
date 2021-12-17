from bs4 import BeautifulSoup
import requests
import pandas as pd
from checkTimeFormat import checkTimeFormat
import datetime
import sys
import time


def getHttpReq(url, retrys):
    
    r = requests.get(url)
    return r
   
def getArticleInPage(page, category):
    
    try:
        source = requests.get('https://www.enikos.gr/'+category+'/page/'+str(page)).text
    except:
        return pd.DataFrame(), getDate()     
    
    soup = BeautifulSoup(source, 'lxml')
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    
    for article in soup.find_all(class_='archive-post'):
        
        try:
        
            if(article.find(class_='radio-show-image')):
                continue

            title = summary = date = link = articleText = ''

            #title
            if(article.find('h2', class_='archive-post-title')):
                title = article.find('h2', class_='archive-post-title').text.strip()

            #summary
            if(article.find('div', class_ = 'archive-post-excerpt')):
                summary = article.find('div', class_ = 'archive-post-excerpt').text.strip()



            #category
            #-


            #link
            #article
            #date

            if(article.find('h2', class_ = 'archive-post-title')):

                link = article.find('h2', class_ = 'archive-post-title').a['href']


                articleLink = requests.get(link).text.strip()

                soupArticleMain = BeautifulSoup(articleLink, 'lxml')
                if(soupArticleMain.find_all('div', id='articletext')):
                    articleText = soupArticleMain.find('div', id='articletext').text.strip();

                #date
                if(soupArticleMain.find('div', class_ = 'post-date')):
                    date = soupArticleMain.find('div', class_ = 'post-date').text.strip()
                    date = checkTimeFormat(date)
        except:
            continue
            
        data = {'title': title, 'summary': summary, 'date': date, 'category': category, 'link': link, 'article': articleText, 'source': 'enikos.gr'}
        df = df.append(data, ignore_index = True )

    minDate = df['date'].min()
    
    return df, minDate
        
     

def getArticles_enikosgr(fromDate,limitPage):
    #ta promoted='false' einai auta p mpenun me taksinomhmeno date
    #if(df.loc[filtDateRange].loc[filtPromoted].shape[0] == 0):
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    print('%%%%%%%%%%%%%%%%%%%%%%%--enikos.gr--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    for category in ['media','politics', 'economy', 'society', 'international','sports','lifestyle']:
        print('--------', category, '----------')
        
        for i in range(0,limitPage):
            print('at page: ' + str(i+1) + '/' + str(limitPage) )
            singlePagedf, minDateSinglePage = getArticleInPage(str(i+1), category)
            
            

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