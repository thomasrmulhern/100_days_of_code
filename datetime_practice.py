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

import re

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''


    x = list(re.search('(\d+\W){2}\d+', line).group(0))
    y = list(re.search('(\d+\W){3}', line).group(0).strip())
    xy = x+y

    def form(beg, end):
        return  int(''.join(xy[beg:end]))

    year = form(0,4)
    month = form(5,7)
    day = form(8,10)
    hour = form(10,12)
    second = form(13,15)
    milisecond = form(16,18)

    # '''trying to convert the earlier code into a dictionary,
    # then loop over it for the final return'''
    #
    # # should the dict values be lists of all strings, mixed types or just ints?

    # time_dict = {
    #     year : [0,4]
    #     month : [5,7]
    #     day : [8,10]
    #     hour : [10,12]
    #     second = [13,15]
    #     milisecond = [16,18]
    # }

    return datetime(year, month, day, hour, second, milisecond)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''

    line = [re.search("Shutdown initiated", loglines) for log in loglines]
    dt = [convert_to_datetime(lines) for lines in line]
    return datetime.timedelta(dt[len(dt)]-dt[0])


# TESTS

line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
print(convert_to_datetime(line1))
print(convert_to_datetime(line2))
print(convert_to_datetime(line3))
