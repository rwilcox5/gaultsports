import time
import random
import csv
import math
import numpy
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

allpred = [94.64,93.9,93.24,93.16,92.75,92.57,91.75,91.59,91.15,90.93,90.59,90.39,89.69,89.66,89.6,89.36,89.05,88.55,88.42,88.4,88.17,87.95,87.72,87.47,87.12,87,86.79,86.67,84.82,84.68,84.61,84.47,84.3,84.24,83.8,83.74,83.68,83.59,83.57,83.53,83.51,83.47,83.46,83.45,82.93,82.87,82.58,82.49,82.28,82.27,82.12,81.7,81.69,81.36,81.35,81.32,81.28,81.2,81.14,81.13,81.05,80.9,80.84,80.62,80.58,80.06,79.99,79.88,79.8,79.75,79.57,79.45,79.23,79.06,78.72,78.54,78.4,78.18,78.14,78.01,77.91,77.77,77.68,77.22,77.18,77.15,77.14,77.13,77.05,76.87,76.85,76.84,76.77,76.68,76.58,76.57,76.36,76.3,76.16,76.15,76,75.95,75.91,75.88,75.6,75.48,75.43,74.78,74.71,74.6,74.56,74.15,74.14,74.01,74,73.84,73.79,73.78,73.76,73.76,73.76,73.69,73.67,73.62,73.61,73.6,73.58,73.48,73.44,73.39,73.27,73.22,73.18,73.04,72.98,72.97,72.84,72.82,72.75,72.66,72.59,72.5,72.46,72.46,72.16,72.16,72.15,72.15,72.11,72.07,72.05,71.9,71.85,71.84,71.81,71.76,71.69,71.65,71.49,71.45,71.44,71.43,71.42,71.41,71.36,71.34,71.24,71.14,71.04,70.96,70.9,70.85,70.75,70.69,70.68,70.66,70.64,70.6,70.54,70.45,70.41,70.32,70.3,70.22,70.03,69.97,69.84,69.79,69.75,69.66,69.6,69.58,69.51,69.51,69.48,69.42,69.28,69.19,69.17,69.08,68.81,68.72,68.38,68.28,68.16,68.15,68.14,68.02,68,67.98,67.97,67.91,67.88,67.83,67.78,67.77,67.68,67.65,67.45,67.43,67.42,67.39,67.33,67.31,67.21,67.15,67.15,67.13,67.08,67.03,66.76,66.74,66.73,66.7,66.59,66.59,66.58,66.34,66.14,66.12,66.08,66.07,66.02,66.02,65.91,65.9,65.89,65.86,65.82,65.76,65.66,65.55,65.53,65.48,65.32,65.28,65.25,65.13,65.12,65.01,64.89,64.83,64.77,64.73,64.67,64.6,64.6,64.52,64.43,64.39,64.39,64.29,64.18,64.14,64.09,64.03,63.98,63.92,63.9,63.88,63.68,63.48,63.46,63.34,63.28,63.15,63.11,63.11,62.99,62.93,62.89,62.84,62.83,62.46,62.39,62.32,62.28,62.22,62.12,61.85,61.71,61.71,61.66,61.61,61.54,61.2,61.11,61.09,61.03,61.02,60.88,60.79,60.71,60.69,60.09,59.92,59.86,59.84,59.47,59.36,59.31,59.25,59.2,59.09,58.83,58.83,58.58,58.41,58.33,58.2,57.81,57.62,57.35,57.23,56.52,56.48,56.35,56.32,55.67,55.56,55.33,55.18,54.46,54.26,53.25,53.21,53.19,52.03,51.9,50.68,48.89]
x = []
y = []
for i in range(0,1):
        sumpyelo = 0
        allpyelo = []
        for ii in range(0,10000):
                spread = 82.27-allpred[i]
                ptdiff = numpy.random.normal(spread,10.5)
                ptscored = 82.27+ptdiff/2
                ptallowed = 82.27-ptdiff/2
                pywin = ptscored**15./(ptscored**15+ptallowed**15)
                pyelo = 400*math.log(1/pywin-1)/math.log(10.)
                sumpyelo += pyelo
                allpyelo.append(pyelo)
        x.append(i)
        y.append(sumpyelo/10000)



allgames = readcsv('allgames2015.csv')
for i in range(0,len(allgames)):
        allgames[i][0] = allgames[i][0].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell')
        allgames[i][1] = allgames[i][1].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell')

allteams = readcsv('conflist.csv')
teamstr = 'allteams = ['
teams = []
clist = []
confstr = 'allconfs = ['
idx = 0
for i in allteams:
        confstr +='["'+i[0]+'",'+str(idx)+','
        for ii in i[1:]:
                teams.append(ii)
                clist.append(i[0])
                teamstr += '"'+ii+'",'
                ingames = False
                for iii in allgames:
                        if iii[0]==ii:
                                ingames = True
                                break
                if not ingames:
                        print ii
                idx +=1
        confstr += str(idx)+',0],'


alldata = []
for i in teams:
        datarow = [i]
        for ii in allgames:
                if ii[0] in teams and ii[1] in teams:
                        if ii[0]==i:
                                if clist[teams.index(ii[0])]== clist[teams.index(ii[1])]:
                                        datarow.append('@c')
                                else:
                                        datarow.append('@n')
                                datarow.append(ii[1])
                                if len(ii)>5:
                                        if int(ii[2])>int(ii[3]):
                                                datarow.append('W '+str(ii[2])+'-'+str(ii[3]))
                                        else:
                                                datarow.append('L '+str(ii[3])+'-'+str(ii[2]))
                                else:
                                        datarow.append('')
                        if ii[1]==i:
                                if clist[teams.index(ii[0])]== clist[teams.index(ii[1])]:
                                        datarow.append('hc')
                                else:
                                        datarow.append('hn')
                                datarow.append(ii[0])
                                if len(ii)>5:
                                        if int(ii[3])>int(ii[2]):
                                                datarow.append('W '+str(ii[3])+'-'+str(ii[2]))
                                        else:
                                                datarow.append('L '+str(ii[2])+'-'+str(ii[3]))
                                else:
                                        datarow.append('')
        alldata.append(datarow)


print alldata[0]
print len(alldata)

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

alldev = []
for i in allgamesplayed:
        teamdev = 0
        for ii in i[1:]:
                opponent = ii[1]
                opponentrpi = -1
                for iii in range(0,len(teamrpi)):
                        if teamrpi[iii][0]==opponent:
                                opponentrpi = iii+1
                                break
                if opponentrpi>-1:
                        actpywin = ii[2]**15./(ii[2]**15.+ii[3]**15.)
                        actpyelo = 400*math.log(1./actpywin-1.)/math.log(10.)
                        estpyelo = -.0000636076820*opponentrpi**3+.0362780638*opponentrpi**2-8.53439177*opponentrpi+343.020636
                        devdiff = (actpyelo-estpyelo)/-330.
                        teamdev += devdiff
        alldev.append([i[0],teamdev])
unsorted = True

while unsorted:
        unsorted = False
        for i in range(0,len(alldev)-1):
                if alldev[i][1]<alldev[i+1][1]:
                        holdrpi = alldev[i]
                        alldev[i]=alldev[i+1]
                        alldev[i+1]=holdrpi
                        unsorted = True
for i in range(0,60):
        print alldev[i]





