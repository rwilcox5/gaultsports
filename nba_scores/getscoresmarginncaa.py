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
def readcsvn(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
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

    oddsgames = readcsvn('ncaam1517.csv')
    oddsteams = []
    rawteams = []
    for i in oddsgames:
        if i[3] not in oddsteams:
            oddsteams.append(i[3])
    print oddsteams


    ptgames = []
    for i in range(0,len(oddsgames[1:])/2):
        try:
            if oddsgames[i*2+1][8]=='pk' or oddsgames[i*2+2][8]=='pk':
                thespread = 0
            elif float(oddsgames[i*2+1][8])<80:
                thespread = -1*float(oddsgames[i*2+1][8])
            elif float(oddsgames[i*2+2][8])<80:
                thespread = float(oddsgames[i*2+2][8])
            awayteam = oddsgames[i*2+1][3]
            hometeam = oddsgames[i*2+2][3]
            if int(oddsgames[i*2+2][6])>int(oddsgames[i*2+1][6]):
                thisgame = ['2016-17 season:',oddsgames[i*2+1][0],'',hometeam,awayteam,int(oddsgames[i*2+2][6]),int(oddsgames[i*2+1][6]),'w',thespread] #thespread is winner adv.
            else:
                thisgame = ['2016-17 season:',oddsgames[i*2+1][0],'',awayteam,hometeam,int(oddsgames[i*2+1][6]),int(oddsgames[i*2+2][6]),'l',-1*thespread] #thespread is winner adv.
            ptgames.append(thisgame)
        except:
            print oddsgames[i*2+1],oddsgames[i*2+2]

    print ptgames[0]





    return ptgames


def updateelo(winnerElo,loserElo,eloType,adjMOV,winnerID,loserID,teams,hc):
    k=20
    elo_diff = (winnerElo-loserElo)*1.+hc
    if eloType[0]==eloType[1] or 3==3:
        elochg = k*(adjMOV*1.+3.)**(.8)/(7.5+(.006)*elo_diff)*(1./(1.+10.**(elo_diff/400.)))
    else:
        elochg = k*(1./(1.+10.**(elo_diff/400.)))
    winnerElo_new = winnerElo+elochg
    loserElo_new = loserElo-elochg
    teams[winnerID][eloType[0]+1]=winnerElo_new
    teams[loserID][eloType[1]+1]=loserElo_new
    return teams

def makepred():
    predspread = (team1elo-team2elo)/28.
    actspread = mov
    if idx>400:
        x[eloID-1].append(predspread)
        y[eloID-1].append(actspread)
    return teams,x,y

def predgames(season,allgames):
    teams = []
    xc = []
    yc = []
    x = []
    y = []
    beatsp = 0
    lostsp = 0
    movchg = 7.0
    onedev = 100.
    for idx,i in enumerate(allgames):
        if i[0]==season:
            team1 = i[3]
            team2 = i[4]
            team1id = -1
            team2id = -1
            for iidx,ii in enumerate(teams):
                if ii[0]==team1:
                    team1elo = ii[1:6]
                    team1id = iidx
                if ii[0]==team2:
                    team2elo = ii[1:6]
                    team2id = iidx
            if team1id == -1:
                teams.append([team1,1500.+2*onedev,1500.+onedev,1500.,1500.-onedev,1500.+2*onedev])
                team1elo = [1500.+2*onedev,1500.+onedev,1500.,1500.-onedev,1500.+2*onedev]
                team1id = len(teams)-1
            if team2id == -1:
                teams.append([team2,1500.+2*onedev,1500.+onedev,1500.,1500.-onedev,1500.+2*onedev])
                team2elo = [1500.+2*onedev,1500.+onedev,1500.,1500.-onedev,1500.+2*onedev]
                team2id = len(teams)-1

            

            

            if i[7]=='w':
                hc = 100.
            else:
                hc = -100.

            m,b = numpy.polyfit([-2,-1,0,1,2], team1elo, 1)
            est1elo = [b+hc,m]
            m,b = numpy.polyfit([-2,-1,0,1,2], team2elo, 1)
            est2elo = [b,m]
            xx = (est2elo[0]-est1elo[0])/(est1elo[1]+est2elo[1])

            predspread = xx*movchg
            conspread = (team1elo[3]-team2elo[3]+hc)/28.

            if i[5]>i[6]+2*movchg:
                teams = updateelo(team1elo[4],team2elo[0],[4,0],i[5]-i[6]-2*movchg,team1id,team2id,teams,hc)
                teams = updateelo(team1elo[3],team2elo[1],[3,1],i[5]-i[6]-movchg,team1id,team2id,teams,hc)
                teams = updateelo(team1elo[2],team2elo[2],[2,2],i[5]-i[6],team1id,team2id,teams,hc)
                teams = updateelo(team1elo[1],team2elo[3],[1,3],i[5]-i[6]+movchg,team1id,team2id,teams,hc)
                teams = updateelo(team1elo[0],team2elo[4],[0,4],i[5]-i[6]+2*movchg,team1id,team2id,teams,hc)
            elif i[5]>i[6]+movchg:
                teams = updateelo(team2elo[0],team1elo[4],[0,4],-1*(i[5]-i[6]-2*movchg),team2id,team1id,teams,-1*hc)
                teams = updateelo(team1elo[3],team2elo[1],[3,1],i[5]-i[6]-movchg,team1id,team2id,teams,hc)
                teams = updateelo(team1elo[2],team2elo[2],[2,2],i[5]-i[6],team1id,team2id,teams,hc)
                teams = updateelo(team1elo[1],team2elo[3],[1,3],i[5]-i[6]+movchg,team1id,team2id,teams,hc)
                teams = updateelo(team1elo[0],team2elo[4],[0,4],i[5]-i[6]+2*movchg,team1id,team2id,teams,hc)
            else:
                teams = updateelo(team2elo[0],team1elo[4],[0,4],-1*(i[5]-i[6]-2*movchg),team2id,team1id,teams,-1*hc)
                teams = updateelo(team2elo[1],team1elo[3],[1,3],-1*(i[5]-i[6]-movchg),team2id,team1id,teams,-1*hc)
                teams = updateelo(team1elo[2],team2elo[2],[2,2],i[5]-i[6],team1id,team2id,teams,hc)
                teams = updateelo(team1elo[1],team2elo[3],[1,3],i[5]-i[6]+movchg,team1id,team2id,teams,hc)
                teams = updateelo(team1elo[0],team2elo[4],[0,4],i[5]-i[6]+2*movchg,team1id,team2id,teams,hc)

            m,b = numpy.polyfit([-2,-1,0,1,2], teams[team1id][1:6], 1)
            est1elo = [b,m]
            m,b = numpy.polyfit([-2,-1,0,1,2], teams[team2id][1:6], 1)
            est2elo = [b,m]
            teams[team1id][1]=est1elo[0]-2*est1elo[1]
            teams[team1id][2]=est1elo[0]-est1elo[1]
            #teams[team1id][3]=est1elo[0]
            teams[team1id][4]=est1elo[0]+est1elo[1]
            teams[team1id][5]=est1elo[0]+2*est1elo[1]
            teams[team2id][1]=est2elo[0]-2*est2elo[1]
            teams[team2id][2]=est2elo[0]-est2elo[1]
            #teams[team2id][3]=est2elo[0]
            teams[team2id][4]=est2elo[0]+est2elo[1]
            teams[team2id][5]=est2elo[0]+2*est2elo[1]


            
            if predspread >0:
                actspread = i[5]-i[6]
            else:
                actspread = i[6]-i[5]
            if conspread >0:
                actcspread = i[5]-i[6]
            else:
                actcspread = i[6]-i[5]
            vegasspread = i[8]
            if idx>2500:
                if predspread>conspread+1.5 and abs(vegasspread)>8:
                    betamt = 1.
                    if i[5]-i[6]>vegasspread:
                        beatsp +=betamt
                    elif i[5]-i[6]<vegasspread:
                        lostsp +=betamt
                elif predspread<conspread-1.5 and abs(vegasspread)>8:
                    betamt = 1.
                    if i[5]-i[6]<vegasspread:
                        beatsp +=betamt
                    elif i[5]-i[6]>vegasspread:
                        lostsp +=betamt
            if idx>800:
                x.append(abs(predspread))
                y.append(actspread)
                xc.append(abs(conspread))
                yc.append(actcspread)


            
    for i in teams:
        #print i
        m,b = numpy.polyfit([0,1,2,3,4], i[1:6], 1)
        #print [b,b+m,b+2*m,b+3*m,b+4*m]
    print numpy.corrcoef(x,y)[0][1],numpy.corrcoef(xc,yc)[0][1], beatsp, lostsp, beatsp*1./(beatsp+lostsp)
    shiftxy = 0
    for i in range(0,len(x)):
        shiftxy +=x[i]-y[i]
    #print shiftxy/len(x)




for i in range(2016,2017):
    allgames = getgames()
    if i<2009:
        predgames(str(i)+'-0'+str(i-1999)+' season:',allgames)
    else:
        predgames(str(i)+'-'+str(i-1999)+' season:',allgames)









