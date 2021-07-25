#encoding:utf-8
import time

def toDate(timeStamp):
    timeArray = time.localtime(timeStamp)
    return time.strftime("%Y-%m-%d", timeArray)
