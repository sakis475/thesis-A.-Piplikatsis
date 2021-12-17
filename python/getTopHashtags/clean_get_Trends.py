import pandas as pd
import re

#                    '#ελληνικαΜονο', '11-07-2021'
def clean_get_Trends(hashtags, date):
    

    #vgazw ola ta rows poy exoun to header 
    hashtags = hashtags[hashtags['date'] != 'date']

    #epilegw na exw MONO hashtags
    filtHashtagOnly = hashtags['hashtag'].str.startswith('#', na=False)
    hashtags = hashtags[filtHashtagOnly]

    hashtags.reset_index(inplace=True)

    #first 11-07-2021 17:35
    #last  16-07-2021 20:30
    filtDate = hashtags['date'].str.startswith(date, na=False)
    hashtags = hashtags[filtDate]

    #diagrafh olwn twn hashtags sta agglika
    hashtags['hashtag'] = hashtags['hashtag'].apply(lambda hashtag: re.sub('\B\#[0-9]*[a-zA-Z]\w+','None', hashtag))
    hashtags = hashtags[hashtags['hashtag'] != 'None']

    #kane ola ta hashtag me mikra grammata, to twitter exei case-insensitive search
    hashtags['hashtag'] = hashtags['hashtag'].apply(lambda hashtag: hashtag.lower())

    #groupby kathe hashtag gia na vroume to plhthos tu, oso megalitero toso pio poli wra emfanisthke sta top trends
    hashtags = hashtags.groupby(['hashtag']).size()
    
    hashtags = hashtags.to_frame(name = 'count')
    
    hashtags.reset_index(inplace=True)
    
    hashtags = hashtags.sort_values(by='count', ascending = False)
    
    
    
    return hashtags