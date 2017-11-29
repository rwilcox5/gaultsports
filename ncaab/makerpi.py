import time
import random
import csv
import math
import threading
from threading import Thread

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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

alldata = readcsv('2017-18.csv')

allgamesplayed = []
allgamestoplay = []
for row in alldata:
        playeddata = [row[0]]
        toplaydata = [row[0]]
        for i in range(0,(len(row))/3):
                if len(row[3*i+3])>0:
                        lscore = row[3*i+3][row[3*i+3].find('-')+1:]
                        wscore = row[3*i+3][row[3*i+3].find(' '):row[3*i+3].find('-')]
                        if row[3*i+3].find('W')>-1:
                                game = [row[3*i+1],row[3*i+2],int(wscore),int(lscore)]
                        else:
                                game = [row[3*i+1],row[3*i+2],int(lscore),int(wscore)]
                        playeddata.append(game)
                else:
                        game = [row[3*i+1],row[3*i+2]]
                        toplaydata.append(game)
        if len(playeddata)>15:
                donot = 0
        else:
                allgamesplayed.append(playeddata)
                allgamestoplay.append(toplaydata)

teamwp = []
teamopp = []
teamadjwp = []
for i in allgamesplayed:
        wins = 0
        games = 0
        opponents = []
        adjgames = 0
        adjwins = 0
        for ii in i[1:]:
                games += 1
                if ii[0]=='@':
                        adjgames +=1.4
                        if ii[2]>ii[3]:
                                adjwins +=1.4
                elif ii[0]=='vs.':
                        adjgames += 1.0
                        if ii[2]>ii[3]:
                                adjwins +=1.0
                else:
                        adjgames += .6
                        if ii[2]>ii[3]:
                                adjwins +=.6
                if ii[2]>ii[3]:
                        opponents.append([ii[1],0])
                        wins +=1
                else:
                        opponents.append([ii[1],1])
        teamwp.append([i[0],wins,games])
        teamopp.append([i[0],opponents])
        teamadjwp.append([i[0],adjwins*1./adjgames])
teamoppwp = []
for i in teamopp:
        oppwp = 0.
        opptot = 0.
        for ii in i[1]:

                for iii in teamwp:
                        if iii[0]==ii[0]:
                                if iii[2]>1:
                                        oppwp += (iii[1]-ii[1])*1./(iii[2]-1.)
                                        opptot += 1.

                                break
        if opptot==0:
                print i
                print i[1]
        else:
                teamoppwp.append([i[0],oppwp*1./opptot])

teamoppoppwp = []
for i in teamopp:
        oppwp = 0.
        opptot = 0.
        for ii in i[1]:
                for iii in teamoppwp:
                        if iii[0]==ii[0]:
                                oppwp += iii[1]
                                opptot += 1.
                                break
        if opptot==0:
                print i
        else:
                teamoppoppwp.append([i[0],oppwp*1./opptot])
print len(teamwp),len(teamoppwp),len(teamoppoppwp)
teamrpi = []
for i in range(0,len(teamwp)):
        tname = teamwp[i][0]
        teamopp = -1
        teamoppopp = -1
        for ii in range(0,len(teamoppwp)):
                if tname==teamoppwp[ii][0]:
                        teamopp=teamoppwp[ii][1]
        for ii in range(0,len(teamoppoppwp)):
                if tname==teamoppoppwp[ii][0]:
                        teamoppopp=teamoppoppwp[ii][1]
        if teamopp != -1 and teamoppopp != -1:
                teamrpi.append([tname,teamadjwp[i][1]*.25+teamopp*.5+teamoppopp*.25,teamadjwp[i][1],teamopp,teamoppopp])
unsorted = True

while unsorted:
        unsorted = False
        for i in range(0,len(teamrpi)-1):
                if teamrpi[i][1]<teamrpi[i+1][1]:
                        holdrpi = teamrpi[i]
                        teamrpi[i]=teamrpi[i+1]
                        teamrpi[i+1]=holdrpi
                        unsorted = True
for i in range(0,10):
        print teamrpi[i]
