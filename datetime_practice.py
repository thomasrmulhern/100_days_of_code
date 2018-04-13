'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    import re
    line = 'INFO 2014-07-03T23:27:51 supybot Shutdown complete.'
    x = re.search('(\d+\W){2}\d+', line)
    y = re.search('(\d+\W){3}', line)
    x = x.group(0)
    y = y.group(0)
    y = y.strip()
    xy = list(x+y)
    year = int(''.join(xy[0:4]))
    month = int(''.join(xy[5:7]))
    day = int(''.join(xy[8:10]))
    hour = int(''.join(xy[10:12]))
    second = int(''.join(xy[13:15]))
    milisecond = int(''.join(xy[16:18]))

    return datetime(year, month, day, hour, second, milisecond)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    pass
