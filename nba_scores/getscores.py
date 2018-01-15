import time
import datetime
import random
import csv
import math
import numpy
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import lxml
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from lxml.cssselect import CSSSelector
import requests

def writecsvw(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i
def writecsv(parr, filen):
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
                spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa
def readcsva(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append(row[0])
        return allgamesa

def getgames():

    rawgames = readcsv('nbalast10seasons.csv')
    allgames = []
    for i in rawgames:
        try:
            winner = i[3]
            firstint = 0
            for iidx,ii in enumerate(winner):
                try:
                    iiint = int(ii)
                    firstint = iidx
                    break
                except:
                    pass
            winner_team = winner[:firstint-1]
            winner_score = int(winner[firstint:])

            loser = i[4]
            firstint = 0
            for iidx,ii in enumerate(loser):
                try:
                    iiint = int(ii)
                    firstint = iidx
                    break
                except:
                    pass
            loser_team = loser[:firstint-1]
            loser_score = int(loser[firstint:])

            allgames.append([i[0],i[1],i[2],winner_team,loser_team,winner_score,loser_score])
        except:
            pass
    return allgames

def predgames(season,allgames):
    teams = []
    x = []
    y = []
    for idx,i in enumerate(allgames):
        if i[0]==season:
            team1 = i[3]
            team2 = i[4]
            team1id = -1
            team2id = -1
            for iidx,ii in enumerate(teams):
                if ii[0]==team1:
                    team1elo = ii[1]
                    team1id = iidx
                if ii[0]==team2:
                    team2elo = ii[1]
                    team2id = iidx
            if team1id == -1:
                teams.append([team1,1500.])
                team1elo = 1500.
                team1id = len(teams)-1
            if team2id == -1:
                teams.append([team2,1500.])
                team2elo = 1500.
                team2id = len(teams)-1
            predspread = (team1elo-team2elo)/28.
            mov = i[5]-i[6]
            k=20
            elo_diff = (team1elo-team2elo)*1.
            elochg = k*(mov*1.+3.)**(.8)/(7.5+(.006)*elo_diff)*(1./(1.+10.**(elo_diff/400.)))
            #elochg = k*(1./(1.+10.**(elo_diff/400.)))
            team1elo_new = team1elo+elochg
            team2elo_new = team2elo-elochg
            teams[team1id][1]=team1elo_new
            teams[team2id][1]=team2elo_new
            
            if predspread>0:
                actspread = mov
            else:
                actspread = -1*mov
            if idx>400:
                x.append(abs(predspread))
                y.append(actspread)

    print numpy.corrcoef(x,y)[0][1]
    shiftxy = 0
    for i in range(0,len(x)):
        shiftxy+=x[i]-y[i]
    #print shiftxy/len(x)


for i in range(2007,2017):
    allgames = getgames()
    if i<2009:
        predgames(str(i)+'-0'+str(i-1999)+' season:',allgames)
    else:
        predgames(str(i)+'-'+str(i-1999)+' season:',allgames)










