import datetime
import re

def findMonthAbbr(month):
    month = month.replace("ά", 'α')
    month = month.replace("έ", 'ε')
    month = month.replace("ή", 'η')
    month = month.replace("ί", 'ι')
    month = month.replace("ό", 'ο')
    month = month.replace("ύ", 'υ')
    month = month.replace("ώ", 'ω')
    
    if(re.search('Ιαν.*', month)):
        return '01'
    elif(re.search('Φεβ.*', month)):
        return '02'
    elif(re.search('Μαρ.*', month)):
        return '03'
    elif(re.search('Απρ.*', month)):
        return '04'
    elif(re.search('Μαι.*', month)):
        return '05'
    elif(re.search('Ιουν.*', month)):
        return '06'
    elif(re.search('Ιουλ.*', month)):
        return '07'
    elif(re.search('Αυγ.*', month)):
        return '08'
    elif(re.search('Σεπ.*', month)):
        return '09'
    elif(re.search('Οκτ.*', month)):
        return '10'
    elif(re.search('Νο.*', month)):
        return '11'
    elif(re.search('Δεκ.*', month)):
        return '12'
    else:
        return -1
    

def checkTimeFormat(dateInput):
    
    #17:23\n, Πέμπτη 07 Οκτωβρίου 2021
    
    dateInput = dateInput.split()
    
    time = dateInput[0]
    day = dateInput[3]
    month = findMonthAbbr(dateInput[4])
    year = dateInput[5]
    
    date = time + ' ' + day + ' ' + month + ' ' + year
    
    date = datetime.datetime.strptime(date, '%H:%M %d %m %Y')
    
    return date
