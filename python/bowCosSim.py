import math

import sys
sys.path.append('getTweets')
from cleanTweets import cleanText

sys.path.append('greek_stemmer')
from greek_stemmer import stemmer

sys.path.append('database/helpers')
from getTimeNow import getDate

def lemmatizer2(text):
    
    lemText = ''
    for token in text.split():
        lemText += ' ' + stemmer.stem_word(token, 'VBG')
    return lemText


def bagOfWords(text, voc):
    wob = dict.fromkeys(voc,0)
    text = text.split()
    
    #create bagOfWords vector
    for j in text:
        wob[j] += 1
    
    l2normSum = 0
    
    #apply l2norm in vector
    for i in list(wob.values()):
        l2normSum += i*i
        
    
    l2normSum = math.sqrt( l2normSum )
    
    
    
    if(l2normSum != 0):
        for i in wob.keys():
            wob[i] = wob[i]/l2normSum
    
        
        
    return list(wob.values() )


def cosineSimil(vec1, vec2):
    distance = 0;
    for i in range(len(vec1)):
        distance += vec1[i]*vec2[i]
    return distance





def similarity(articles, tweets, searchQuery):
    
    articles.drop_duplicates(subset=["article",'link'], inplace=True)
    articles = articles[~articles['article'].isna() ]
    articles['articleOriginal'] = articles['article']
    #lemmatize articles summary
    articles = cleanText(articles.rename(columns={'article': 'fullText'}))
    articles['fullText'] = articles['fullText'].apply(lambda text: lemmatizer2(text))
    
    
    tweets['tweetOriginal'] = tweets['fullText']
    tweets = cleanText(tweets)
    tweets.drop_duplicates(subset=["fullText"], inplace=True)
    tweets = tweets[~tweets['fullText'].str.split().str.len().lt(1) ]
    tweets['fullText'] = tweets['fullText'].apply(lambda text: lemmatizer2(text))

    
    articlesVocub = set()
    articles['fullText'].str.split().apply(articlesVocub.update)
    #len(articlesVocub)

    tweetsVocub = set()
    tweets['fullText'].str.split().apply(tweetsVocub.update)
    #len(tweetsVocub)

    vocubConcatenated = articlesVocub.union(tweetsVocub)

    #len(vocubConcatenated)

    #koines lekseis
    #len(articlesVocub.intersection(tweetsVocub) )

    articles['bow'] = articles['fullText'].apply(lambda text: bagOfWords(text, vocubConcatenated))
    tweets['bow'] = tweets['fullText'].apply(lambda text: bagOfWords(text, vocubConcatenated))


    #from IPython.display import clear_output
    import pandas as pd
    pd.options.mode.chained_assignment = None
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_colwidth', None)

    
    
    
    similResults = pd.DataFrame()
    
    
    for i in range(articles.shape[0]):
        similarity = 0;
        for j in range(tweets.shape[0]):
            tweet = tweets['bow'].iloc[j]
            article = articles['bow'].iloc[i]

            similarity += cosineSimil(tweet, article)

        
        similarity = (similarity/(tweets.shape[0]) ) * 1000
        #print(str(similarity) + ' ' + articles['summaryOriginal'].iloc[i])
        similResults = similResults.append({'cosSimil': similarity, 'articleOriginal': articles['articleOriginal'].iloc[i], 'articleTitle': articles['title'].iloc[i], 'articleDate': articles['date'].iloc[i], 'articleCategory': articles['category'].iloc[i], 'articleLink': articles['link'].iloc[i], 'articleSource': articles['source'].iloc[i], 'searchQuery': searchQuery} ,ignore_index=True)
        
        #clear_output(wait=True)
        #print(similResults[similResults['cosSimil'].max() == similResults['cosSimil']])
        #print('Done '+ str(i+1) + '/' + str(articles.shape[0]) )
    print('calculated ', articles.shape[0], ' articles X ', tweets.shape[0], ' tweets')
    return similResults