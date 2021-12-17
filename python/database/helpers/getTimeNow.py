from datetime import datetime as dtNow
import datetime


def getDate():
    # datetime object containing current date and time
    now = dtNow.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
    dt_string = datetime.datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')
    return dt_string