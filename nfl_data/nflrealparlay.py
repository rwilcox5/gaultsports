import time
import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
nteams = 130
this_week = 5

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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

allgames = readcsv('nfl16.csv')

print len(allgames)

teams = []
allelos = [1386.60661738187,1523.61839594805,1483.88120708739,1577.25173932155,1451.58424856129,1476.43131892176,1463.0081034697,1297.4840313748,1645.58794425166,1504.09669826344,1438.6571174855,1595.46410064528,1458.19106743891,1365.20428758862,1515.42579084463,1537.81266533677,1670.67562006733,1465.66647164366,1464.20068481427,1443.26379253801,1400.92674053396,1413.45250987923,1418.36940674607,1493.09912723611,1476.82828101692,1554.94879549516,1434.98431735436,1492.28569222856,1598.89740469865,1545.63720313099,1508.07362423011,1380.59003149679]

for i in range(0,256):
    allin = False
    for ii in range(0,len(teams)):
        if teams[ii][0]==allgames[i][0]:
            allin = True
    if not allin:
        all32 = []
        for ii in range(0,32):
            all32.append(0)
        teams.append([allgames[i][0],1500])

realgames = []
for i in range(0,256):
    ateam = allgames[i][0]
    hteam = allgames[i][1]
    for ii in range(0,len(teams)):
        if ateam==teams[ii][0]:
            ateamid= ii
        if hteam==teams[ii][0]:
            hteamid= ii  
    aelo = teams[ateamid][1]
    helo = teams[hteamid][1]

    if int(allgames[i][3])>int(allgames[i][2]):
        hwin = True
    else:
        hwin = False
    k = 25.
    kk = 1.
    if hwin:
        ateamprob = 1./(1.+10.**((helo-aelo)/400.))
        helo = helo+k*ateamprob
        aelo = aelo-k*ateamprob               
        
    else:
        hteamprob = 1./(1.+10.**((aelo-helo)/400.))
        helo = helo-k*hteamprob
        aelo = aelo+k*hteamprob
                
        
    teams[ateamid][1] = aelo
    teams[hteamid][1] = helo

def getteamdiffs(team1,team2,team3,team4,team5,team6,team7,team8,teams):
    teamids = []
    for idx,i in enumerate(teams):
        if i[0]==team1:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team2:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team3:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team4:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team5:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team6:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team7:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team8:
            teamids.append(idx)

    adjteams = []
    for i in range(0,32):
        adjteams.append([teams[i][0],teams[i][1]])
    sumprobbronco = 0.
    sumprobboth = 0.
    probbetter = [0.,0.,0.,0.]
    probworse = [0.,0.,0.,0.]
    probbothbetter = [0.,0.]
    probbothworse = [0.,0.]
    proballbetter = 0.
    proballworse = 0.
    prob3better = [0.,0.,0.,0.]
    prob3worse = [0.,0.,0.,0.]
    chgamt = 25.
    ovprob = 0.
    for i in range(0,256):
        for ii in range(1,9):
            if i%(2**ii) < 2**(ii-1):
                adjteams[teamids[ii-1]][1]=teams[teamids[ii-1]][1]+chgamt
            else:
                adjteams[teamids[ii-1]][1]=teams[teamids[ii-1]][1]-chgamt

        proboutcome = 1.
        for ii in range(0,256):
            ateam = allgames[ii][0]
            hteam = allgames[ii][1]
            for iii in range(0,len(teams)):
                if ateam==teams[iii][0]:
                    ateamid= iii
                if hteam==teams[iii][0]:
                    hteamid= iii  
            aelo = adjteams[ateamid][1]
            helo = adjteams[hteamid][1]
            if int(allgames[ii][3])>int(allgames[ii][2]):
                proboutcome *= 1.82/(1.+10.**((aelo-helo)/400.))
            else:
                proboutcome *= 1.82/(1.+10.**((helo-aelo)/400.))
        if i%2==0:
            probbetter[0]+=proboutcome
        else:
            probworse[0]+=proboutcome
        if i%4 < 2:
            probbetter[1]+=proboutcome
        else:
            probworse[1]+=proboutcome
        if i%8 < 4:
            probbetter[2]+=proboutcome
        else:
            probworse[2]+=proboutcome
        if i%16 < 8:
            probbetter[3]+=proboutcome
        else:
            probworse[3]+=proboutcome
        if i%4 == 0:
            probbothbetter[0]+=proboutcome
        if i%16 < 4:
            probbothbetter[1]+=proboutcome
        if i%4 == 3:
            probbothworse[0]+=proboutcome
        if i%16 > 11:
            probbothworse[1]+=proboutcome

        if i%256 == 0:
            proballbetter+=proboutcome
        if i%256 == 255:
            proballworse+=proboutcome


        if i%2 == 0 and i%4 < 2 and i%8 < 4:
            prob3better[0]+=proboutcome
        if i%2 == 0 and i%4 < 2 and i%16 < 8:
            prob3better[1]+=proboutcome
        if i%2 == 0 and i%16 < 8 and i%8 < 4:
            prob3better[2]+=proboutcome
        if i%16 < 8 and i%4 < 2 and i%8 < 4:
            prob3better[3]+=proboutcome
        if i%2 == 1 and i%4 >= 2 and i%8 >= 4:
            prob3worse[0]+=proboutcome
        if i%2 == 1 and i%4 >= 2 and i%16 >= 8:
            prob3worse[1]+=proboutcome
        if i%2 == 1 and i%16 >= 8 and i%8 >= 4:
            prob3worse[2]+=proboutcome
        if i%16 >= 8 and i%4 >= 2 and i%8 >= 4:
            prob3worse[3]+=proboutcome
        ovprob +=proboutcome
        
    #print probbothbetter[0]/probbetter[0]+ probbothworse[0]/probworse[0], probbothbetter[0]/probbetter[1]+ probbothworse[0]/probworse[1], probbothbetter[1]/probbetter[2]+ probbothworse[1]/probworse[2], probbothbetter[1]/probbetter[3]+ probbothworse[1]/probworse[3]
    for i in range(0,1):
        print proballbetter/prob3better[i], proballworse/prob3worse[i], proballbetter/prob3better[i] + proballworse/prob3worse[i], (proballbetter/ovprob+proballworse/ovprob)*128
def getteamdiffs2(team1,team2,team3,team4,team5,team6,team7,team8,teams):
    teamids = []
    for idx,i in enumerate(teams):
        if i[0]==team1:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team2:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team3:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team4:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team5:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team6:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team7:
            teamids.append(idx)
    for idx,i in enumerate(teams):
        if i[0]==team8:
            teamids.append(idx)
    maxteams = 3
    for teamswap in range(0,maxteams):
        adjp = 0
        adjn = 0
        for chgamt in [50.,0.]:
            adjteams = []
            for i in range(0,32):
                adjteams.append([teams[i][0],teams[i][1]])
            teamnotswap = []
            for i in range(0,maxteams):
                if i != teamswap:
                    teamnotswap.append(i)
            for i in teamnotswap:
                adjteams[teamids[i]][1]=teams[teamids[i]][1]+chgamt

            proboutcome = 1.
            for ii in range(0,256):
                ateam = allgames[ii][0]
                hteam = allgames[ii][1]
                for iii in range(0,len(teams)):
                    if ateam==teams[iii][0]:
                        ateamid= iii
                    if hteam==teams[iii][0]:
                        hteamid= iii  
                aelo = adjteams[ateamid][1]
                helo = adjteams[hteamid][1]
                k = 20.
                if int(allgames[ii][3])>int(allgames[ii][2]):
                    proboutcome = 1./(1.+10.**((helo-aelo)/400.))
                    helo = helo+k*proboutcome
                    aelo = aelo-k*proboutcome

                else:
                    proboutcome = 1./(1.+10.**((aelo-helo)/400.))
                    helo = helo-k*proboutcome
                    aelo = aelo+k*proboutcome
                adjteams[ateamid][1]=aelo
                adjteams[hteamid][1]=helo

            if chgamt == 50.:
                adjp = int(adjteams[teamids[teamswap]][1]*10)*1./10-1000
        print adjp-int(adjteams[teamids[teamswap]][1]*10)*1./10+1000,
    print ""



byconf = []
byconf.append(['Denver Broncos','Oakland Raiders','San Diego Chargers','Kansas City Chiefs'])
byconf.append(['Indianapolis Colts','Jacksonville Jaguars','Tennessee Titans','Houston Texans'])
byconf.append(['Pittsburgh Steelers','Baltimore Ravens','Cincinnati Bengals','Cleveland Browns'])
byconf.append(['Miami Dolphins','Buffalo Bills','New England Patriots','New York Jets'])
byconf.append(['Philadelphia Eagles','Dallas Cowboys','Washington Redskins','New York Giants'])
byconf.append(['Chicago Bears','Green Bay Packers','Detroit Lions','Minnesota Vikings'])
byconf.append(['Atlanta Falcons','Tampa Bay Buccaneers','Carolina Panthers','New Orleans Saints'])
byconf.append(['Arizona Cardinals','San Francisco 49ers','Seattle Seahawks','St. Louis Rams'])
def dobyteam():
    for i in byconf:
        team1 = i[0]
        team2 = i[1]
        team3 = i[2]
        team4 = i[3]
        getteamdiffs(team1,team2,team3,team4,teams)
        team1 = i[0]
        team2 = i[2]
        team3 = i[1]
        team4 = i[3]
        getteamdiffs(team1,team2,team3,team4,teams)
        team1 = i[0]
        team2 = i[3]
        team3 = i[1]
        team4 = i[2]
        getteamdiffs(team1,team2,team3,team4,teams)

for idx,i in enumerate(byconf[:3]):
    for ii in byconf[idx+1:4]:
        team1 = i[0]
        team2 = i[1]
        team3 = i[2]
        team4 = i[3]
        team5 = ii[0]
        team6 = ii[1]
        team7 = ii[2]
        team8 = ii[3]
        getteamdiffs2(team1,team2,team3,team4,team5,team6,team7,team8,teams)
print soto
for i in byconf:
    team1 = i[0]
    team2 = i[1]
    team3 = i[2]
    team4 = i[3]
    getteamdiffs2(team1,team2,team3,team4,team5,team6,team7,team8,teams)
print soto

for idx,i in enumerate(byconf[4:4]):
    for ii in byconf[idx+5:8]:
        team1 = i[0]
        team2 = i[1]
        team3 = i[2]
        team4 = i[3]
        team5 = ii[0]
        team6 = ii[1]
        team7 = ii[2]
        team8 = ii[3]
        getteamdiffs(team1,team2,team3,team4,team5,team6,team7,team8,teams)



    
