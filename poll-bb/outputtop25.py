import time
import sys
import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
nteams = 351
this_week = int(sys.argv[1])

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


csvapmassey = readcsv('convertedapmassey.csv')
apmassey = []
apconvert = []
nameconvert = []
for i in csvapmassey:
    apmassey.append([i[0],i[3],int(i[2])])
    apconvert.append([i[0],i[3],int(i[2])])
    nameconvert.append([i[3],i[1]])

print apmassey[:5]
print len(apmassey)
def getranking(voterranks,week):  #Creates full 351 team ranking for each voter with normal top 25 and then computer generated rest of rank
    masseyrankraw = readcsv('massey1718/masseyweek'+str(week-1)+'.csv')
    masseyranks = []
    for i in range(0,nteams):
        masseyranks.append(int(masseyrankraw[i][0]))
    myrank = []
    for i in voterranks:
        team = str(i)
        for ii in apmassey:
            if ii[1]==team:
                masseyranks.remove(ii[2])
                myrank.append(ii[2])
    for i in masseyranks:
        myrank.append(i)
    return myrank

def sse(x):
    tse = 0.
    nse = 0.
    for i in x:
        tse+=i**2.
        nse+=1.
    if nse==0:
        return 0.
    else:
        return tse*1./nse

def genbias(voter,this_week,apmassey,apgames):
    allranks = []
    for i in range(1,this_week+1):
        allvotes = readcsv('ap1718/week'+str(i)+'.csv')
        for ii in allvotes:
            if ii[0]==voter:
                voterranks = getranking(ii[1:],i)
                allranks.append(voterranks)

    teambias = []
    for i in apmassey:
        teambias.append([i[0],i[1],0])
    if this_week>0:
        for iiii in range(0,2):
            for week in range(1,this_week+1):
                myrank = allranks[week-1]
                teams = []
                for idx,ii in enumerate(myrank):
                    for idxbias,i in enumerate(apmassey):
                        if i[2]==ii:
                            teams.append([i[1],-4.160255889*(idx+1)**.5+102.8304061+teambias[idxbias][2]]) #Adjust this to create ELO for any ranking
                if week != this_week:
                    for i in apgames:
                        if i[0]==week:
                            ateam = i[1][0]
                            hteam = i[1][1]
                            ateamrate = 55.
                            hteamrate = 55.
                            for ii in teams:
                                if ii[0]==ateam:
                                    ateamrate = ii[1]
                                    break
                            for ii in teams:
                                if ii[0]==hteam:
                                    hteamrate = ii[1]
                                    break
                            if i[4]==1:
                                if hteamrate>ateamrate:
                                    predoutcome = math.log(hteamrate-ateamrate+1)
                                else:
                                    predoutcome = -1.*math.log(-hteamrate+ateamrate+1)
                            else:
                                if hteamrate+2>ateamrate:
                                    predoutcome = math.log(hteamrate+2-ateamrate+1)
                                else:
                                    predoutcome = -1.*math.log(-hteamrate-2+ateamrate+1)
                            if int(i[3][1])>int(i[3][0]):
                                actoutcome = math.log(int(i[3][1])*1.+int(i[3][0])*-1.+1.)
                            else:
                                actoutcome = -1.*math.log(int(i[3][1])*-1.+int(i[3][0])*1.+1.)
                            for idx,ii in enumerate(teambias):
                                if ii[1]==ateam:
                                    teambias[idx].append(1.*(predoutcome-actoutcome))
                                    break
                            for idx,ii in enumerate(teambias):
                                if ii[1]==hteam:
                                    teambias[idx].append(-1.*(predoutcome-actoutcome))
                                    break
            if iiii==0:
                for idx, i in enumerate(teambias):
                    if sum(teambias[idx][3:])>0:
                        teambias[idx][2]=1.5**(sum(teambias[idx][3:])/len(teambias[idx][3:]))
                    elif sum(teambias[idx][3:])<0:
                        teambias[idx][2]=-1.*.667**(sum(teambias[idx][3:])/len(teambias[idx][3:]))
                    else:
                        teambias[idx][2]=0.

                    #if i[1]=='ohio-state':
                    #    print teambias[idx], sum(teambias[idx][3:]), len(teambias[idx][3:])
                    teambias[idx]=[teambias[idx][0],teambias[idx][1],teambias[idx][2]]
            else:
                for idx, i in enumerate(teambias):
                    if len(teambias[idx])>3:
                        teambias[idx][3]=sse(teambias[idx][3:])
                    else:
                        teambias[idx].append(0.)

                    myrank = allranks[this_week-1]
                    teams = []
                    for idxb,ii in enumerate(myrank):
                        for idxbias,ibias in enumerate(apmassey):
                            if ibias[2]==ii:
                                teams.append([ibias[1],-4.160255889*(idxb+1)**.5+102.8304061])
                    for ii in teams:
                        if ii[0]==i[1]:
                            if len(teambias[idx])>4:
                                teambias[idx][4]=ii[1]
                            elif len(teambias[idx])==4:
                                teambias[idx].append(ii[1])
                    
                    teambias[idx]=[teambias[idx][0],teambias[idx][1],teambias[idx][2],teambias[idx][3],teambias[idx][4]]


    return teambias

def formatGames(allgames):
    apgames = []
    for game in allgames:
        if len(game)>4:
            gameday = game[2]
            month = gameday[5:7]
            date = int(gameday[8:])
            week = 0
            if month=='11':
                if date < 13:
                    week = 1
                elif date < 20:
                    week = 2
                elif date < 27:
                    week = 3
                else:
                    week = 4
            elif month=='12':
                if date < 4:
                    week = 4
                elif date < 11:
                    week = 5
                elif date < 18:
                    week = 6
                elif date < 25:
                    week = 7
                else:
                    week = 8
            elif month=='01':
                if date < 8:
                    week= 9
                elif date < 15:
                    week = 10
                elif date < 22:
                    week = 11
                elif date < 29:
                    week = 12
                else:
                    week = 13
            elif month=='02':
                if date < 3:
                    week= 15
                else:
                    week = 16
            elif month=='03':
                week = 16
            ateam = 'FCS'
            aconf = 'FCS'
            hteam = 'FCS'
            hconf = 'FCS'
            for i in apconvert:
                if i[2]==int(game[0]):
                    ateam = i[1]
                    aconf = i[0]
                    break
            for i in apconvert:
                if i[2]==int(game[1]):
                    hteam = i[1]
                    hconf = i[0]
                    break
            if game[3].find(' ')>-1:
                game[3]=game[3][:game[3].find(' ')]
            if game[4].find(' ')>-1:
                game[4]=game[4][:game[4].find(' ')]
            donotadd = False
            nsite = 0
            for i in apgames:
                #if i[0]==week and i[1]==[ateam,hteam]:
                #    donotadd = True
                #if i[0]==week and i[1]==[hteam,ateam]:
                apgames.remove(i)
            if len(game)>5:
                nsite = 1
            if not donotadd:
                apgames.append([week,[ateam,hteam],[aconf,hconf],[game[3],game[4]],nsite])
    return apgames

def removeTempVoters(my_week):  #Remove voters that haven't voted every week.
    allvoters = []
    allvotes = readcsv('ap1718/week1.csv')
    for i in allvotes:
        allvoters.append(i[0])

    for i in range(2,my_week+1):
        allvotes = readcsv('ap1718/week'+str(i)+'.csv')
        for ii in allvoters:
            voterin = False
            for iii in allvotes:
                if iii[0]==ii:
                    voterin = True
            if not voterin:
                allvoters.remove(ii)
    return allvoters

def createTop25(allvoterbias):

    top25 = []
    expweight = 1.0
    teambiaschg = 2.
    confbiaschg = 2.
    for i in apmassey:
        rating = 0
        adjrating = 0
        totalweight = 0
        tvoters = 0
        tbias = 0
        for voter in allvoterbias:
            for ii in voter:
                if ii[1]==i[1]:
                    totalweight += 1./(.000001+ii[3]**expweight+ii[5]**expweight+ii[7]**expweight)
                    tvoters += 1
        for voter in allvoterbias:
            for ii in voter:
                if ii[1]==i[1]:
                    rating += 1./tvoters*(ii[4])
                    adjrating += (1./(.000001+ii[3]**expweight+ii[5]**expweight+ii[7]**expweight))/totalweight*(ii[4]+ii[2]/teambiaschg+ii[6]/confbiaschg)
                    tbias += ii[2]/tvoters
        top25.append([i[1], rating, adjrating,tbias])
    return top25

def createRank(my_week):
    allgames = readcsv('results.csv')
    apgames = formatGames(allgames)
    
    
    allvoters = removeTempVoters(my_week)
    

    allvoterbias = []
    for voter in allvoters:
        allvoterbias.append(genbias(voter,my_week,apmassey,apgames))

    for voter in allvoterbias:
        confs = []
        for i in apmassey:
            if i[0] not in confs:
                confs.append([i[0],0,0,0])
        toterror = 0.
        for i in voter:
            toterror+=i[3]
            for idx,ii in enumerate(confs):
                if ii[0]==i[0]:
                    confs[idx][1]+=i[3]
                    confs[idx][2]+=i[2]
                    confs[idx][3]+=1

        for idx,i in enumerate(voter):
            for ii in confs:
                if ii[0]==i[0]:
                    voter[idx].append(ii[1]*1./ii[3])
                    voter[idx].append(ii[2]*1./ii[3])
                    voter[idx].append(toterror*1./nteams)

    top25 = createTop25(allvoterbias)
    

    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0,len(top25)-1):
            if top25[i][2]<top25[i+1][2]:
                holdit = top25[i]
                top25[i]=top25[i+1]
                top25[i+1]=holdit
                unsorted = True
    return top25

def unbiasedRank(my_week):
    allvoters = []
    allvotes = readcsv('ap1718/week'+str(my_week)+'.csv')
    for i in allvotes:
        allvoters.append(i[0])


    allvoterdata = []
    for voter in allvoters:
        allvotes = readcsv('ap1718/week'+str(my_week)+'.csv')
        for ii in allvotes:
            if ii[0]==voter:
                voterranks = ii[1:]
                allranks = voterranks
        allvoterdata.append(allranks)

    top25 = []
    for i in apmassey:
        rating = 0
        for voter in allvoterdata:
            for iidx,ii in enumerate(voter):
                if ii==i[1]:
                    rating += max(0,25-iidx)
        top25.append([i[1], rating, rating,0])

    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0,len(top25)-1):
            if top25[i][2]<top25[i+1][2]:
                holdit = top25[i]
                top25[i]=top25[i+1]
                top25[i+1]=holdit
                unsorted = True
    return top25

all_ranks = []
for my_week in range(1,int(this_week)+1):
    print my_week
    if my_week<6:
        top25ap = unbiasedRank(my_week)
        top25 = unbiasedRank(my_week)
    else:
        top25ap = unbiasedRank(my_week)
        top25 = createRank(int(my_week))
    all_ranks.append(top25)

    istr = 'top25 = ['
    for i in top25[:25]:
        teamname = i[0]
        for ii in apmassey:
            if ii[1]==teamname:
                confname = ii[0]
        for iidx,ii in enumerate(top25ap):
            if ii[0]==teamname:
                aprank = str(iidx+1)
        weightedpoints = str(i[2])
        for ii in nameconvert:
            if ii[0]==teamname:
                namename = ii[1]
        if str(confname).find('Independents')>-1:
            confname = 'Ind.'
        if str(confname).find('The American')>-1:
            confname = 'American'
        istr +='["'+namename.replace('"','')+'","'+confname.replace('"','')+'",'+weightedpoints+','+aprank+','+'['
        for iii in range(0,len(all_ranks)):
            for iiiidx,iiii in enumerate(all_ranks[iii]):
                if iiii[0]==teamname:
                    istr += str(26-min(iiiidx+1,26))+','
        istr = istr[:-1]+']],'
    istr = istr[:-1]+'];'

    


f = open('helloworld.txt','w')
f.write(istr+'\n')
f.close()
