import math

import sys
sys.path.append('getTweets')
from cleanTweets import cleanText

sys.path.append('greek_stemmer')
from greek_stemmer import stemmer

sys.path.append('database/helpers')
from getTimeNow import getDate


#Επιστρέφει το lemmatization κειμένου
def lemmatizer2(text):
    
    lemText = ''
    for token in text.split():
        lemText += ' ' + stemmer.stem_word(token, 'VBG')
    return lemText

#Επιστρέφει την διανυσματικοποίηση κειμένου δοθείσας το κείμενο και το λεξικό του.
def bagOfWords(text, voc):
    wob = dict.fromkeys(voc,0)
    text = text.split()
    
    #δημιουργία bagOfWords 
    for j in text:
        wob[j] += 1
    
    l2normSum = 0
    
    #εφαρμογή l2norm στο διάνυσμα
    for i in list(wob.values()):
        l2normSum += i*i
        
    
    l2normSum = math.sqrt( l2normSum )
    
    
    
    if(l2normSum != 0):
        for i in wob.keys():
            wob[i] = wob[i]/l2normSum
    
        
        
    return list(wob.values() )

#Επιστρέφει την συνημιτονοειδής απόσταση μεταξύ δύο διανυσμάτων
def cosineSimil(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        distance += vec1[i]*vec2[i]
    return distance




#Συγκρίνει άρθρα με tweets και επιστρέφει τα αποτελέσματα
def similarity(articles, tweets, searchQuery):
    #Διαγράφει τα τύχον διπλότυπα άρθρα
    articles.drop_duplicates(subset=["article",'link'], inplace=True)
    #Διαγράφει κενά  άρθρα
    articles = articles[~articles['article'].isna() ]
    #Κρατάει αντίγραφο του πραγματικού άρθραυ
    articles['articleOriginal'] = articles['article']
    #Καθαρισμός άρθρου
    articles = cleanText(articles.rename(columns={'article': 'fullText'}))
    #Πραγματοποιεί lemmatization στο κείμενο του άρθρου
    articles['fullText'] = articles['fullText'].apply(lambda text: lemmatizer2(text))
    
    #Κρατάει αντίγραφο του πραγματικού tweet
    tweets['tweetOriginal'] = tweets['fullText']
    #Καθαρισμός tweet
    tweets = cleanText(tweets)
    #Διαγράφει τα τύχον διπλότυπα tweets
    tweets.drop_duplicates(subset=["fullText"], inplace=True)
    #Διαγράφει κενά tweets
    tweets = tweets[~tweets['fullText'].str.split().str.len().lt(1) ]
    #Πραγματοποιεί lemmatization στο tweet
    tweets['fullText'] = tweets['fullText'].apply(lambda text: lemmatizer2(text))

    #Δημιουργεί το λεξικό των άρθρων
    articlesVocub = set()
    articles['fullText'].str.split().apply(articlesVocub.update)
    
    #Δημιουργεί το λεξικό των tweets
    tweetsVocub = set()
    tweets['fullText'].str.split().apply(tweetsVocub.update)
    
    #Ενώνει το λεξικό των tweets και άρθρων
    vocubConcatenated = articlesVocub.union(tweetsVocub)


    #Δημιουργείται στήλη με την διανυσματικοποίηση άρθρου και tweet αντίστοιχα
    articles['bow'] = articles['fullText'].apply(lambda text: bagOfWords(text, vocubConcatenated))
    tweets['bow'] = tweets['fullText'].apply(lambda text: bagOfWords(text, vocubConcatenated))


    
    import pandas as pd
    pd.options.mode.chained_assignment = None
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_colwidth', None)

    
    
    
    similResults = pd.DataFrame()
    
    #Αθροίζονται όλες οι συνημιτονοειδής αποστάσεις και διαιρούνται με το πλήθος των κειμένων για να πάρουμε τον μέσο όρο.
    for i in range(articles.shape[0]):
        similarity = 0
        for j in range(tweets.shape[0]):
            tweet = tweets['bow'].iloc[j]
            article = articles['bow'].iloc[i]

            similarity += cosineSimil(tweet, article)

        
        similarity = (similarity/(tweets.shape[0]) ) * 1000
        #print(str(similarity) + ' ' + articles['summaryOriginal'].iloc[i])

        #Όλες οι πληροφορίες των αποτελεσμάτων αποθηκεύονται σε dataframe
        similResults = similResults.append({'cosSimil': similarity, 'articleOriginal': articles['articleOriginal'].iloc[i], 'articleTitle': articles['title'].iloc[i], 'articleDate': articles['date'].iloc[i], 'articleCategory': articles['category'].iloc[i], 'articleLink': articles['link'].iloc[i], 'articleSource': articles['source'].iloc[i], 'searchQuery': searchQuery} ,ignore_index=True)
        
        #clear_output(wait=True)
        #print(similResults[similResults['cosSimil'].max() == similResults['cosSimil']])
        #print('Done '+ str(i+1) + '/' + str(articles.shape[0]) )
    print('calculated ', articles.shape[0], ' articles X ', tweets.shape[0], ' tweets')
    return similResults