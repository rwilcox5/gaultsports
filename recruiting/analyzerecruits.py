import time
import sys
import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select

pagen = 10
theyear = sys.argv[1]
basefile = sys.argv[2]



def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
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

#print allplayers[0]
def minforstars(nstars):
    nstars = int(nstars)
    if nstars == 2:
        return 5.
    elif nstars == 3:
        return 10.
    elif nstars == 4:
        return 20.
    elif nstars == 5:
        return 30.
    else:
        return 2.5
def getallplayers():
    allplayers = []
    with open(basefile+str(theyear)+'done.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            for i in range(0,1000):
                    try:
                            row.remove('')
                    except:
                            pass
            if len(row)>3:
                row.append(0)
            allplayers.append(row)
    return allplayers


def getteamlist(allplayers):
    teams = []
    for i in range(0,len(allplayers)):
            for ii in range(3,len(allplayers[i])):
                    if allplayers[i][ii] not in teams:
                        if str(allplayers[i][ii]) != "0":
                            teams.append(allplayers[i][ii])
    return teams


def setinitialelos(teams,allplayers):
    for i in range(0,len(teams)):
            teams[i]=[teams[i],0,1500,1500,0]
            for ii in range(0,len(allplayers)):
                    for iii in range(3,len(allplayers[ii])):
                            if allplayers[ii][iii]==teams[i][0]:
                                    teams[i][1]=teams[i][1]+1
                                    if iii==3:
                                        teams[i][4]=teams[i][4]+1

    for i in range(0,len(teams)):
            if teams[i][1]<30:
                    teams[i][2]=1200
                    teams[i][3]=1200
            if teams[i][1]<20:
                    teams[i][2]=1000
                    teams[i][3]=1000
            if teams[i][1]<10:
                    teams[i][2]=800
                    teams[i][3]=800
    return teams

def sortallplayers(allplayers,teams):
    for i in range(0,len(allplayers)):
        if len(allplayers[i])>6:
            notsorted = 1
            while notsorted == 1:
                notsorted = 0
                for ii in range(4,len(allplayers[i])-2):
                    for iii in range(0,len(teams)):
                        if teams[iii][0]==allplayers[i][ii]:
                            tid = iii
                        if teams[iii][0]==allplayers[i][ii+1]:
                            tido = iii
                    if teams[tid][2]<teams[tido][2]:
                        nt1 = allplayers[i][ii+1]
                        nt2 = allplayers[i][ii]
                        allplayers[i][ii]=nt1
                        allplayers[i][ii+1]=nt2
                        notsorted = 1
    return allplayers

def rankteams(allplayers,teams,iiii):
    for ii in range(0,len(allplayers)):
            nstars = allplayers[ii][2]
            if len(allplayers[ii])==5:
                    wt = allplayers[ii][3]
                    for i in range(0,len(teams)):
                        if wt==teams[i][0]:
                                wtid = i
                    wtelo0 = teams[wtid][2]
                    kw0 = minforstars(nstars)
                    newelow0 = wtelo0+kw0
                    teams[wtid][2]=newelow0
                    allplayers[ii][len(allplayers[ii])-1]=kw0

            if len(allplayers[ii])>5:
                    sumadded = 0
                    for iii in range(4,len(allplayers[ii])-1):
                            wt = allplayers[ii][3]
                            lt = allplayers[ii][iii]
                            
                            for i in range(0,len(teams)):
                                    if wt==teams[i][0]:
                                            wtid = i
                                    if lt==teams[i][0]:
                                            ltid = i
                            
                            wtelo = teams[wtid][3]
                            ltelo = teams[ltid][3]
                            wtelo0 = teams[wtid][2]
                            ltelo0 = teams[ltid][2]

                            noffers = teams[ltid][1]
                            if iii < 20:
                                kw = 12.-iii/8.-iiii*3.
                                kl = 12.-iii/8.-iiii*3.
                            else:
                                kw = 2.
                                kl = 2.
                            kw0 = kw
                            kl0 = kl

                            #kw = 50*1./noffers**0/(4.**(iii-2))/(iiii+1)
                            #kl = 50*1./noffers**0/(4.**(iii-2))/(iiii+1)
                            #kw0 = 250./(1.5**(iii-2))/(iiii+1)**0
                            #kl0 = 50000*1./noffers**1/(4.**(iii-2))/(iiii+1)
                            
                            ltchance = 1./(1.+10.**((wtelo-ltelo)*1./400))
                            
                            newelow = wtelo+kw*ltchance
                            newelol = ltelo-kl*ltchance
                            newelow0 = wtelo0+kw0*ltchance
                            newelol0 = ltelo0-kl0*ltchance
                            teams[wtid][2]=newelow0
                            teams[ltid][2]=newelol0
                            if iiii <4:
                                teams[wtid][3]=newelow
                                teams[ltid][3]=newelol

                            sumadded = sumadded +kw0*ltchance
                    if sumadded < minforstars(nstars):
                        teams[wtid][2]=teams[wtid][2]+minforstars(nstars)-sumadded
                        teams[wtid][3]=teams[wtid][3]+minforstars(nstars)-sumadded
                    allplayers[ii][len(allplayers[ii])-1]=sumadded
    return allplayers, teams








allplayers = getallplayers()
teams = getteamlist(allplayers)
teams = setinitialelos(teams,allplayers)

for iiii in range(0,4):
    allplayers = sortallplayers(allplayers,teams)

    print "done", time.time()
    allplayers,teams = rankteams(allplayers,teams,iiii)


tteams = []
for i in range(0,len(teams)):
    yt = ""
    if len(teams[i])==5:
        if int(teams[i][1])>30:
            this_team = [teams[i][0],teams[i][3]+min(teams[i][4],30)*20+teams[i][1],teams[i][4]]
            tteams.append(this_team)
        else:
            print "not Enough", teams[i][0]
    else:
        print "WWWWWWWWWWW", teams[i][0], len(teams[i])
writecsv(tteams,'elorecmy.csv')
tocsv = []
for i in range(0,len(allplayers)):
    allplayers[i][1]=allplayers[i][len(allplayers[i])-1]
    tocsv.append(allplayers[i])
writecsv(tocsv,'eloplayers.csv')
#for i in range(0,len(teams)):
#        print teams[i]
unsorted = True
while unsorted:
    unsorted = False
    for i in range(0,len(tteams)-1):
        if float(tteams[i][1])<float(tteams[i+1][1]):
            holdt = tteams[i]
            tteams[i]=tteams[i+1]
            tteams[i+1]=holdt
            unsorted = True

conflist = readcsv('conflist.csv')
confconv = [['acc','ACC'],['big10','Big 10'],['big12','Big 12'],['pac12','Pac 12'],['sec','SEC'],['sbelt','Sun Belt'],['ia','Ind.'],['mwest','M. West'],['midam','MAC'],['aac','American'],['wac','WAC'],['cusa','Conf USA']]
for i in range(0,len(conflist)):
    for ii in confconv:
        if ii[0]==conflist[i][1]:
            conflist[i][1]=ii[1]
teamstr = "teams = ['Heading','"
confstr = "conferences = ['Heading','"
commitstr = "commits = ['Heading',"
ratingstr = "ratings = ['Heading',"
for i in range(0,99):
    teamstr +=tteams[i][0]+"','"
    confname = 'FCS'
    for ii in conflist:
        if ii[0]==tteams[i][0]:
            confname = ii[1]
    confstr += confname+"','"
    if confname=='':
        print tteams[i][0]
    commitstr += str(tteams[i][2]) +","
    ratingstr += str(int(tteams[i][1]))+","

i = 99
teamstr +=tteams[i][0]+"'];"
confname = 'FCS'
for ii in conflist:
    if ii[0]==tteams[i][0]:
        confname = ii[1]
confstr += confname+"'];"
commitstr += str(tteams[i][2]) +"];"
ratingstr += str(int(tteams[i][1]))+"];"
print teamstr
print confstr
print commitstr
print ratingstr