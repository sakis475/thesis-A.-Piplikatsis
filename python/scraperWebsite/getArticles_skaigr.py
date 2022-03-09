from bs4 import BeautifulSoup
import requests
import pandas as pd
from checkTimeFormat import checkTimeFormat
import datetime
import sys
import time

import traceback
import logging

sys.path.append('../database/helpers')
from getTimeNow import getDate

def getHttpReq(url, retrys):
    
    r = requests.get(url)
    return r

#Κατέβασμα όλων των άρθρων και των μεταδεδομένων από μία σελίδα του skai.gr
def getArticleInPage_skaigr(page):
    
    #Κατεβαίνει μια σελίδα του ειδησεογραφικού
    try:
        source = requests.get(' https://www.skai.gr/newsfeed?page='+str(page)).text
    except:
        return pd.DataFrame(), getDate()    
    
    #Εισαγωγή της σελίδας του ειδησεογραφικού στην BeautifulSoup βιβλιοθήκη με lxml parser
    soup = BeautifulSoup(source, 'lxml')
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    

    #Αναζήτηση και αποθήκευση σε μεταβλητές όλων των επιμέρων στοιχείων του ειδησεογραφικού
    for article in soup.find_all('div', class_= 'cmnArticleTitlePad'):
        
        category = ''
        
        try:
            
            
            title = article.find('a', class_='title mainLink').text.strip()
            link = 'https://www.skai.gr' + article.find('a', class_='title mainLink')['href']
            summary = article.find('div', class_='lead').text.strip()

            date = article.find('div', class_='date').text.strip()
            date = datetime.datetime.strptime(date, '%d/%m/%Y - %H:%M')
            date = date.strftime('%Y-%m-%d %H:%M:%S')
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

            #Κατεβαίνει η σελίδα που περιέχει το άρθρο
            articleLink = requests.get(link).text.strip()
            soupArticleMain = BeautifulSoup(articleLink, 'lxml')
        
        except:
            
            print('error parsing, title or link or summary or date')
            continue
            
            
        try:
            articleText = soupArticleMain.find('div', id='articleHidder').text.strip();
            
            
        except Exception as e:
            #print('cat error: ',category)
            print('title error: ',title)
            logging.error(traceback.format_exc())
            print('#########')
            continue
            
        try:
            category = soupArticleMain.find('div', class_='article-category').find('a').text.strip()
        except:
            print('Didnt find category')

        
        data = {'title': title, 'summary': summary, 'date': date, 'category': category, 'link': link, 'article': articleText, 'source': 'skai.gr'}
        df = df.append(data, ignore_index = True )
    
    
    minDate = df['date'].min()
    
    return df, minDate


#Κατέβασμα όλων των άρθρων και των μεταδεδομένων από εισαγώμενη ημερομηνία και μετά του skai.gr
def getArticles_skaigr(fromDate,limitPage):
    
    
    df = pd.DataFrame(columns = ['title', 'summary', 'date', 'category', 'link', 'article', 'source'])
    
    
    print('%%%%%%%%%%%%%%%%%%%%%%%--skai.gr--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')



    for i in range(0,limitPage):
        print('at page: ' + str(i+1) + '/' + str(limitPage) )
        singlePagedf, minDateSinglePage = getArticleInPage_skaigr(str(i))

        df = df.append(singlePagedf, ignore_index = True )

        try:
            if(minDateSinglePage <= fromDate ):
                print('stopped searching at page: ' + str(i+1))
                break
        except:
            print('catch date type: ',type(minDateSinglePage))
            print('catch date: ',minDateSinglePage)




    filtDateRange = df['date'] >= fromDate    

    df = df.loc[filtDateRange]
    
    print('Number of articles found: ', df.shape[0])
    
    return df