import time
import sys
import random
import csv
import math
import threading
import urllib, json


def writecsva(parr, filen):
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i

def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

def getschedule(year,month,day):
    if month<10:
        month = '0'+str(month)
    if day<10:
        day = '0'+str(day)
    url = "http://statsapi.web.nhl.com/api/v1/schedule"
    response = urllib.urlopen(url)
    data = json.loads(response.read())


def getbox(year,month,day,gameId):
    if month<10:
        month = '0'+str(month)
    if day<10:
        day = '0'+str(day)
    url = "http://statsapi.web.nhl.com/api/v1/game/2015020742/feed/live"
    response = urllib.urlopen(url)
    data = json.loads(response.read())




    return scoreUpdates




gameIds = getschedule(2018,1,21)
for i in gameIds:

    scoreUpdates = getpbp(2018,1,21,i)
    writecsva(scoreUpdates,'allnbagames1718.csv')
print soto
f = open('hello_recruits.txt','w')
f.write(istr+'\n')
f.close()