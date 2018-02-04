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
    url = "http://data.nba.net/10s/prod/v1/"+str(year)+str(month)+str(day)+"/scoreboard.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    gameIds = []
    for i in data['games']:
        gameIds.append(i['gameId'])
    return gameIds

def getpbp(year,month,day,gameId):
    if month<10:
        month = '0'+str(month)
    if day<10:
        day = '0'+str(day)
    url = "http://data.nba.net/10s/prod/v1/"+str(year)+str(month)+str(day)+"/"+str(gameId)+"_pbp_1.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    scoreUpdates = []
    for i in data['plays']:
        if i['isScoreChange']:
            scoreUpdates.append([gameId,i['personId'],int(i['vTeamScore']),int(i['hTeamScore']),int(str(i['clock'])[:str(i['clock']).find(':')]),float(str(i['clock'])[str(i['clock']).find(':')+1:])])
    return scoreUpdates


gameIds = getschedule(2018,1,21)
for i in gameIds:
    scoreUpdates = getpbp(2018,1,21,i)
    writecsva(scoreUpdates,'allnbagames1718.csv')
print soto
f = open('hello_recruits.txt','w')
f.write(istr+'\n')
f.close()