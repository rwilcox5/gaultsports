import time

import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
teamtrans=[]
with open('teamtrans.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        for i in range(0,1000):
                try:
                        row.remove('')
                except:
                        pass
        teamtrans.append(row)
pagen = 10
theyear = 2017
allplayers = []
with open('allrecs2017fb.csv', 'rb') as csvfile:
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

def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i

teams = []
#print allplayers[0]
print time.time()
for i in range(0,len(allplayers)):
        for ii in range(3,len(allplayers[i])):
                if allplayers[i][ii] not in teams:
                    if str(allplayers[i][ii]) != "0":
                        teams.append(allplayers[i][ii])

print "done", time.time()
for i in range(0,len(teams)):
        teams[i]=[teams[i],0,1500,1500,0]
        for ii in range(0,len(allplayers)):
                for iii in range(3,len(allplayers[ii])):
                        if allplayers[ii][iii]==teams[i][0]:
                                teams[i][1]=teams[i][1]+1

print teams[:5]
for i in range(0,len(teams)):
        if teams[i][1]<10:
                teams[i][2]=1200
                teams[i][3]=1200
        if teams[i][1]<7:
                teams[i][2]=1000
                teams[i][3]=1000
        if teams[i][1]<4:
                teams[i][2]=800
                teams[i][3]=800
for iiii in range(0,4):
    for i in range(0,len(allplayers)):
        if len(allplayers[i])>5:
            notsorted = 1
            while notsorted == 1:
                notsorted = 0
                for ii in range(4,len(allplayers[i])-1):
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
    print "done", time.time()
    for ii in range(0,len(allplayers)):
            if len(allplayers[ii])==4:
                    wt = allplayers[ii][3]
                    for i in range(0,len(teams)):
                        if wt==teams[i][0]:
                                wtid = i
                    wtelo0 = teams[wtid][2]
                    kw0 = 3.14/(iiii+1)**0
                    newelow0 = wtelo0+kw0*.5
                    teams[wtid][2]=newelow0
                    allplayers[ii][len(allplayers[ii])-1]=kw0*.5

            if len(allplayers[ii])>4:
                    sumadded = 0
                    for iii in range(4,len(allplayers[ii])):
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
                            if int(allplayers[ii][1])==2006:
                                noffers = teams[ltid][3]
                            elif int(allplayers[ii][1])==2007:
                                noffers = teams[ltid][4]
                            else:
                                noffers = teams[ltid][1]
                            kw = 25*1./noffers**0/(3.**(iii-2))/(iiii+1)
                            kl = 25*1./noffers**0/(3.**(iii-2))/(iiii+1)
                            if iii < 9:
                                kw0 = 12./(1.1**(iii-2))/(iiii+1)**0
                            else:
                                kw0 = 0
                            kl0 = 20000*1./noffers**1/(5**(iii-2))/(iiii+1)

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
                            if iiii <2:
                                teams[wtid][3]=newelow
                                teams[ltid][3]=newelol

                            sumadded = sumadded +kw0*ltchance
                    allplayers[ii][len(allplayers[ii])-1]=sumadded

print teams[:10]
#print stopit

teamrats=[]
with open('2009sag.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        for i in range(0,1000):
                try:
                        row.remove('')
                except:
                        pass
        teamrats.append(row)
tteams = []
trats = []
for i in range(0,len(teams)):
    yt = ""
    #indexend = teams[i][0].find("-",0)
    #for ii in range(0,indexend):
    #    yt=yt+teams[i][0][ii]
    
    #teams[i][0]=yt
    sgo = 1
    #for ii in range(0,len(teamtrans)):
    #    if teamtrans[ii][1]==teams[i][0]:
    #        teams[i][0]=teamtrans[ii][0]
    #        #print teamtrans[ii][0], teams[i][0]
    #        sgo = 1
    if sgo==0:
        print teams[i][0]
    else:
        #for ii in range(0,len(teamrats)):
        #    if teamrats[ii][0].lower()==teams[i][0]:
        #        teams[i].append(teamrats[ii][4])
                #print teamrats[ii][0].lower(), teams[i][0]
        if len(teams[i])==5:
            if int(teams[i][1])>10:
                tteams.append(teams[i])
            else:
                print "not Enough", teams[i][0]
        else:
            print "WWWWWWWWWWW", teams[i][0], len(teams[i])
writecsv(tteams,'elorecmy.csv')
tocsv = []
for i in range(0,len(allplayers)):
    tocsv.append([allplayers[i][0],allplayers[i][3],allplayers[i][len(allplayers[i])-1]])
writecsv(tocsv,'eloplayers.csv')
#for i in range(0,len(teams)):
#        print teams[i]



