#creates the regex pattern to remove every stopword

from stopwords import stopWords
import re
#metatroph kai sort apo set se list
def convert(set): 
    return sorted(set) 

def rmStopwords():
    #eisagwgh tu arxeiou me ta stopwords
    #https://github.com/explosion/spaCy/blob/master/spacy/lang/el/stop_words.py
    sw = set(stopWords) 
    sw = convert(sw)
    #metatroph se regex
    pat = r'\b(?:{})\b'.format('|'.join(sw))
    pat = pat.replace("ά", 'α')
    pat = pat.replace("έ", 'ε')
    pat = pat.replace("ή", 'η')
    pat = pat.replace("ί", 'ι')
    pat = pat.replace("ό", 'ο')
    pat = pat.replace("ύ", 'υ')
    pat = pat.replace("ώ", 'ω')
    
    return pat;



#clean text: stopword, new line, tabs, links, punctuation..
def cleanText(tweetsData):
    #remove links
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ',regex=True)
    #remove hashtags
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("([#][\w_-]+)", '',regex=True)
    #remove mentions
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("([@][\w_-]+)", '',regex=True)
    #remove html encoded characters amp (&)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("([&][\w_-]+)", '',regex=True)
    #remove special characters
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[^\w\s]", ' ',regex=True)
    #remove tabs, new lines chars, space
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[\t\n\r]", ' ',regex=True)
    #transform words to be without intonation
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ά]", 'α',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[έ]", 'ε',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ή]", 'η',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ί]", 'ι',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ϊ]", 'ι',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ΐ]", 'ι',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ό]", 'ο',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ύ]", 'υ',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ώ]", 'ω',regex=True)
    #remove stopwords
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace(rmStopwords(), ' ',regex=True)
    #remove numbers
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[\d-]", '',regex=True)
    #tweetsData["fullText"] = tweetsData["fullText"].apply(lambda fullText: re.sub(r'\b\w{1,2}\b', '', fullText))

    
    return tweetsData

#clean text: new line, tabs, links, punctuation..
def cleanTextNoSwords(tweetsData):
    #remove links
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ',regex=True)
    #remove hashtags
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("([#][\w_-]+)", '',regex=True)
    #remove mentions
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("([@][\w_-]+)", '',regex=True)
    #remove html encoded characters amp (&)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("([&][\w_-]+)", '',regex=True)
    #remove special characters
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[^\w\s]", ' ',regex=True)
    #remove tabs, new lines chars
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[\t\n\r]", ' ',regex=True)
    #transform words to be without intonation
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ά]", 'α',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[έ]", 'ε',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ή]", 'η',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ί]", 'ι',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ϊ]", 'ι',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ΐ]", 'ι',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ό]", 'ο',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ύ]", 'υ',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ϋ]", 'υ',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ΰ]", 'υ',regex=True)
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[ώ]", 'ω',regex=True)
    
    #remove numbers
    tweetsData["fullText"] = tweetsData['fullText'].str.lower().str.replace("[\d-]", '',regex=True)
    return tweetsData