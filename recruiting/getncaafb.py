#from fabric.api import task

from ftplib import FTP
import csv
import math
import time
from selenium import webdriver
#domain name or server ip:



def writecsv(parr, filen):

        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i

def writecsvw(parr, filen):

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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append([row[0],row[1],int(row[2]),int(row[3]),int(row[4]),int(row[5])])
        return allgamesa

def readcsvtoday(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append([row[0],row[1],float(row[2]),row[3],row[4]])
        return allgamesa


def getthegames(driver,pagen,theyear,fcs,allgamesstart):
    if pagen>9:
            if fcs:
                    b_url = "http://www.ncaa.com/scoreboard/football/fcs/"+str(theyear)+"/"+str(pagen)
            else:
                    b_url = "http://www.ncaa.com/scoreboard/football/fbs/"+str(theyear)+"/"+str(pagen)
    else:
            if fcs:
                    b_url = "http://www.ncaa.com/scoreboard/football/fcs/"+str(theyear)+"/0"+str(pagen)
            else:
                    b_url = "http://www.ncaa.com/scoreboard/football/fbs/"+str(theyear)+"/0"+str(pagen)
    driver.get(b_url)
    alllinks = driver.find_elements_by_class_name("game-contents")
    nteams = 0
    allnflteams = []
    allgamesa = []
    for ilink in range(0,len(alllinks)):

            try:
                    allteams = alllinks[ilink].find_elements_by_tag_name("a")
                    allscores = alllinks[ilink].find_elements_by_class_name("score")
                    if int(allscores[0].text)+int(allscores[1].text)>0:
                            skipit = 0
                            i0=allteams[0].get_attribute('href')[28:]
                            i1=allteams[1].get_attribute('href')[28:]
                            i2=int(allscores[0].text)
                            i3=int(allscores[1].text)
                            for i in allgamesstart:
                                    if i[0]==i0:
                                            if i[1]==i1:
                                                    if i[2]==i2:
                                                            if i[3]==i3:
                                                                    if i[4]==theyear:
                                                                            skipit=1
                            if skipit==0:
                                    allgamesa.append([i0,i1,i2,i3,theyear,pagen])
            except:
                    print allteams[0]

    writecsv(allgamesa,'allncaafcsfbs.csv')
    return allgamesa

def gettodaysgames(driver,pagen):

    b_url = "http://www.ncaa.com/scoreboards/football/fbs/"
    driver.get(b_url)
    alllinks = driver.find_elements_by_class_name("game-contents")
    nteams = 0
    allnflteams = []
    allgamesa = []
    for ilink in range(0,len(alllinks)):
            try:
                    allteams = alllinks[ilink].find_elements_by_tag_name("a")
                    #allscores = alllinks[ilink].find_elements_by_class_name("score")
                    allgamesa.append([allteams[0].get_attribute('href')[28:],allteams[1].get_attribute('href')[28:]])
            except:
                    pass

    writecsvw(allgamesa,'allncaaftodayfbs.csv')
    return allgamesa

def runtheelo(allgamesa):
    teamlist = []
    teamname = []
    awaytotal = 0
    hometotal = 0
    for i in allgamesa:
            awaytotal=i[2]+awaytotal
            hometotal=i[3]+hometotal
    print awaytotal, hometotal, len(allgamesa)
    hfa = int((hometotal-awaytotal)*1./len(allgamesa)/2)
    hfa = 1
    totalarr = []
    eloinit = []
    teamarr = []
    for ii in range(0,100):
            totalarr.append(0)
            for i in allgamesa:
                    if i[2]+hfa >=ii:
                            totalarr[ii]=totalarr[ii]+1
                    if i[3]-hfa >=ii:
                            totalarr[ii]=totalarr[ii]+1
            
            if totalarr[ii]>0:
                    if totalarr[ii]*1./len(allgamesa)/2<1.:
                            eloinit.append(-200*math.log(1./(totalarr[ii]*1./len(allgamesa)/2)-1.,10))
                            #print totalarr[ii]*1./len(allgamesa)/2, -200*math.log(1./(totalarr[ii]*1./len(allgamesa)/2)-1.,10), ii
                    else:
                            eloinit.append(800)
            else:
                    eloinit.append(-800)
            
    for i in allgamesa:
            if i[0] not in teamname:
                    teamname.append(i[0])
                    teamarr = [i[0]]
                    for ii in range(0,100):
                            teamarr.append([1500+eloinit[ii],1500-eloinit[ii]])
                    teamarr.append([0,0,0])
                    teamlist.append(teamarr)
            if i[1] not in teamname:
                    teamname.append(i[1])
                    teamarr = [i[1]]
                    for ii in range(0,100):
                            teamarr.append([1500+eloinit[ii],1500-eloinit[ii]])
                    teamarr.append([0,0,0])
                    teamlist.append(teamarr)
    thestop=0
    for inde in range(0,len(allgamesa)):
        i = allgamesa[inde]
        if int(i[4])==2015:
                thestop = inde+1
    for ou in range(hfa,100-hfa):
            k = 20
            for inde in range(0,thestop):
                    i = allgamesa[inde]
                                    
                    for ii in range(0,len(teamlist)):
                            if teamlist[ii][0]==i[0]:
                                    awayid = ii
                            if teamlist[ii][0]==i[1]:
                                    homeid = ii
                    teamlist[awayid][101][0]=teamlist[awayid][101][0]+i[2]
                    teamlist[awayid][101][1]=teamlist[awayid][101][1]+i[3]
                    teamlist[awayid][101][2]=teamlist[awayid][101][2]+1
                    teamlist[homeid][101][0]=teamlist[homeid][101][0]+i[3]
                    teamlist[homeid][101][1]=teamlist[homeid][101][1]+i[2]
                    teamlist[homeid][101][2]=teamlist[homeid][101][2]+1
                    
                    try:
                            awayoffelo = teamlist[awayid][ou+1+hfa][0]
                            awaydefelo = teamlist[awayid][ou+1+hfa][1]
                            homeoffelo = teamlist[homeid][ou+1-hfa][0]
                            homedefelo = teamlist[homeid][ou+1-hfa][1]
                    except:
                            print awayid, homeid
                            print len(teamlist)
                            print teamlist[homeid]
                            print teamlist[awayid]
                            
                            
                    #print awayid, homeid, awayoffelo,
                    if i[2]>=ou:
                            elodiff = k*1./(1.+10.**((awayoffelo-homedefelo)/400))*math.log(i[2]-ou+1)
                            teamlist[awayid][ou+1+hfa][0]=teamlist[awayid][ou+1+hfa][0]+elodiff
                            teamlist[homeid][ou+1-hfa][1]=teamlist[homeid][ou+1-hfa][1]-elodiff
                    else:
                            elodiff = k*1./(1.+10.**(-(awayoffelo-homedefelo)/400))*math.log(-i[2]+ou)
                            teamlist[awayid][ou+1+hfa][0]=teamlist[awayid][ou+1+hfa][0]-elodiff
                            teamlist[homeid][ou+1-hfa][1]=teamlist[homeid][ou+1-hfa][1]+elodiff
                    if i[3]>=ou:
                            elodiff = k*1./(1.+10.**((homeoffelo-awaydefelo)/400))*math.log(i[3]-ou+1)
                            teamlist[awayid][ou+1+hfa][1]=teamlist[awayid][ou+1+hfa][1]-elodiff
                            teamlist[homeid][ou+1-hfa][0]=teamlist[homeid][ou+1-hfa][0]+elodiff
                    else:
                            elodiff = k*1./(1.+10.**(-(homeoffelo-awaydefelo)/400))*math.log(-i[3]+ou)
                            teamlist[awayid][ou+1+hfa][1]=teamlist[awayid][ou+1+hfa][1]+elodiff
                            teamlist[homeid][ou+1-hfa][0]=teamlist[homeid][ou+1-hfa][0]-elodiff
                    #print teamlist[awayid][ou+1+hfa][0], i[2], ou, hfa
    teamlist2 = []
    for theteam in teamlist:
            teamarr = [theteam[0]]
            for ii in range(0,100):
                    teamarr.append([(theteam[ii+1][0]+(1500+eloinit[ii]))/2.,(theteam[ii+1][1]+(1500-eloinit[ii]))/2.])
            teamarr.append(theteam[101])
            teamlist2.append(teamarr)
    teamlist = teamlist2
    for numtimes in range(0,2):
            for ou in range(hfa,100-hfa):
                    k = 20
                    chgyear  = 1
                    for inde in range(thestop,len(allgamesa)):
                            i = allgamesa[inde]
                            for ii in range(0,len(teamlist)):
                                    if teamlist[ii][0]==i[0]:
                                            awayid = ii
                                    if teamlist[ii][0]==i[1]:
                                            homeid = ii
                            teamlist[awayid][101][0]=teamlist[awayid][101][0]+i[2]
                            teamlist[awayid][101][1]=teamlist[awayid][101][1]+i[3]
                            teamlist[awayid][101][2]=teamlist[awayid][101][2]+1
                            teamlist[homeid][101][0]=teamlist[homeid][101][0]+i[3]
                            teamlist[homeid][101][1]=teamlist[homeid][101][1]+i[2]
                            teamlist[homeid][101][2]=teamlist[homeid][101][2]+1
                            try:
                                    awayoffelo = teamlist[awayid][ou+1+hfa][0]
                                    awaydefelo = teamlist[awayid][ou+1+hfa][1]
                                    homeoffelo = teamlist[homeid][ou+1-hfa][0]
                                    homedefelo = teamlist[homeid][ou+1-hfa][1]
                            except:
                                    print awayid, homeid
                                    print len(teamlist)
                                    print teamlist[homeid]
                                    print teamlist[awayid]
                                    
                                    
                            #print awayid, homeid, awayoffelo,
                            if i[2]>=ou:
                                    elodiff = k*1./(1.+10.**((awayoffelo-homedefelo)/400))*math.log(i[2]-ou+1)
                                    teamlist[awayid][ou+1+hfa][0]=teamlist[awayid][ou+1+hfa][0]+elodiff
                                    teamlist[homeid][ou+1-hfa][1]=teamlist[homeid][ou+1-hfa][1]-elodiff
                            else:
                                    elodiff = k*1./(1.+10.**(-(awayoffelo-homedefelo)/400))*math.log(-i[2]+ou)
                                    teamlist[awayid][ou+1+hfa][0]=teamlist[awayid][ou+1+hfa][0]-elodiff
                                    teamlist[homeid][ou+1-hfa][1]=teamlist[homeid][ou+1-hfa][1]+elodiff
                            if i[3]>=ou:
                                    elodiff = k*1./(1.+10.**((homeoffelo-awaydefelo)/400))*math.log(i[3]-ou+1)
                                    teamlist[awayid][ou+1+hfa][1]=teamlist[awayid][ou+1+hfa][1]-elodiff
                                    teamlist[homeid][ou+1-hfa][0]=teamlist[homeid][ou+1-hfa][0]+elodiff
                            else:
                                    elodiff = k*1./(1.+10.**(-(homeoffelo-awaydefelo)/400))*math.log(-i[3]+ou)
                                    teamlist[awayid][ou+1+hfa][1]=teamlist[awayid][ou+1+hfa][1]+elodiff
                                    teamlist[homeid][ou+1-hfa][0]=teamlist[homeid][ou+1-hfa][0]-elodiff
                            #print teamlist[awayid][ou+1+hfa][0], i[2], ou, hfa
    teams21= []
    for i in teamlist:
            teams21.append([i[0],i[40+1][0],i[40+1][1]])
    writecsvw(teams21,'nflelo.csv')
    return teamlist
            
                    
def makepred(thegame,ovun,half,teamlist,odds,totalbet):
        hfa = 1
        if half:
                
                try:
                        for inde in range(0,len(teamlist)):
                                i = teamlist[inde]
                                if i[0]==thegame[0]:
                                        awayid = inde
                                if i[0]==thegame[1]:
                                        homeid = inde
                        totalprob = 0
                        for ou in range(hfa,ovun-hfa):
                                awayoffelo = teamlist[awayid][ou+1+hfa][0]
                                awaydefelo = teamlist[awayid][ovun+1-ou+1+hfa][1]
                                homeoffelo = teamlist[homeid][ovun+1-ou+1-hfa][0]
                                homedefelo = teamlist[homeid][ou+1-hfa][1]
                                awayoffelo2 = teamlist[awayid][ou+2+hfa][0]
                                homedefelo2 = teamlist[homeid][ou+2-hfa][1]
                                probaw=1./(1.+10.**((homedefelo-awayoffelo)/400))-1./(1.+10.**((homedefelo2-awayoffelo2)/400))
                                
                                probho=1./(1.+10.**((awaydefelo-homeoffelo)/400))
                                #print probaw, ou, ovun-ou, probho, thegame, totalprob
                                totalprob=totalprob+probaw*probho
                        for ou in range(ovun-hfa,95):
                                awayoffelo = teamlist[awayid][ou+1+hfa][0]
                                homedefelo = teamlist[homeid][ou+1-hfa][1]
                                awayoffelo2 = teamlist[awayid][ou+2+hfa][0]
                                homedefelo2 = teamlist[homeid][ou+2-hfa][1]
                                probaw=1./(1.+10.**((homedefelo-awayoffelo)/400))-1./(1.+10.**((homedefelo2-awayoffelo2)/400))
                                
                                probho=1.
                                #print probaw, ou, ovun-ou, probho, thegame, totalprob
                                totalprob=totalprob+probaw*probho
                        if totalprob*odds-1>.1:
                                expectedprob=(totalprob+1./odds)/2
                                tbet = (expectedprob*(odds-1)-(1-expectedprob))/(odds-1)
                                totalbet=totalbet+tbet
                                print totalprob*odds-1, thegame, 'OVER', tbet
                        if (1-totalprob)*odds-1>.1:
                                expectedprob=(1-totalprob+1./odds)/2
                                tbet = (expectedprob*(odds-1)-(1-expectedprob))/(odds-1)
                                totalbet=totalbet+tbet
                                print (1-totalprob)*odds-1, thegame, 'UNDER', tbet
                        if totalprob < .52:
                                #print 'l',totalprob,ovun
                                if totalprob>.52:
                                        #print 'll',totalprob,ovun
                                        print thegame, ovun
                except:
                        pass
        else:
                
                try:
                        for inde in range(0,len(teamlist)):
                                i = teamlist[inde]
                                if i[0]==thegame[0]:
                                        awayid = inde
                                if i[0]==thegame[1]:
                                        homeid = inde
                        totalprob = 0
                        for ou in range(hfa,ovun-hfa):
                                awayoffelo = teamlist[awayid][ou+1+hfa][0]
                                awaydefelo = teamlist[awayid][ovun+1-ou+1+hfa][1]
                                homeoffelo = teamlist[homeid][ovun+1-ou+1-hfa][0]
                                homedefelo = teamlist[homeid][ou+1-hfa][1]
                                awayoffelo2 = teamlist[awayid][ou+2+hfa][0]
                                homedefelo2 = teamlist[homeid][ou+2-hfa][1]
                                probaw=1./(1.+10.**((homedefelo-awayoffelo)/400))-1./(1.+10.**((homedefelo2-awayoffelo2)/400))
                                
                                probho=1./(1.+10.**((awaydefelo-homeoffelo)/400))
                                #print probaw, ou, ovun-ou, probho, thegame, totalprob
                                totalprob=totalprob+probaw*probho
                        for ou in range(ovun-hfa,95):
                                awayoffelo = teamlist[awayid][ou+1+hfa][0]
                                homedefelo = teamlist[homeid][ou+1-hfa][1]
                                awayoffelo2 = teamlist[awayid][ou+2+hfa][0]
                                homedefelo2 = teamlist[homeid][ou+2-hfa][1]
                                probaw=1./(1.+10.**((homedefelo-awayoffelo)/400))-1./(1.+10.**((homedefelo2-awayoffelo2)/400))
                                
                                probho=1.
                                #print probaw, ou, ovun-ou, probho, thegame, totalprob
                                totalprob=totalprob+probaw*probho
                        pushprob = 0
                        for ou in range(hfa,ovun-hfa):
                                awayoffelo = teamlist[awayid][ou+1+hfa][0]
                                awaydefelo = teamlist[awayid][ovun+1-ou+1+hfa][1]
                                homeoffelo = teamlist[homeid][ovun+1-ou+1-hfa][0]
                                homedefelo = teamlist[homeid][ou+1-hfa][1]
                                awayoffelo2 = teamlist[awayid][ou+2+hfa][0]
                                homedefelo2 = teamlist[homeid][ou+2-hfa][1]
                                awaydefelo2 = teamlist[awayid][ovun-ou+1+hfa][1]
                                homeoffelo2 = teamlist[homeid][ovun-ou+1-hfa][0]
                                probaw=1./(1.+10.**((homedefelo-awayoffelo)/400))-1./(1.+10.**((homedefelo2-awayoffelo2)/400))
                                
                                probho=1./(1.+10.**((awaydefelo2-homeoffelo2)/400))-1./(1.+10.**((awaydefelo-homeoffelo)/400))
                                #print probaw, ou, ovun-ou, probho, thegame, totalprob
                                pushprob=pushprob+probaw*probho
                        if totalprob*odds+pushprob-1>.1:
                                expectedprob=(totalprob+1./odds)/2
                                tbet = (expectedprob*(odds-1)-(1-expectedprob))/(odds-1)
                                totalbet=totalbet+tbet
                                print totalprob*odds+pushprob-1, thegame, 'OVER',tbet
                        if (1-totalprob)*odds+pushprob-1>.1:
                                expectedprob=(1-totalprob+1./odds)/2
                                tbet = (expectedprob*(odds-1)-(1-expectedprob))/(odds-1)
                                totalbet=totalbet+tbet
                                print (1-totalprob)*odds+pushprob-1, thegame, 'UNDER',tbet

                except:
                        pass
        
        return totalbet

#@task

#787 rows from last year
def run_bets():
    fcs = True
    driver1 = webdriver.Chrome("C:\Python27\Chrome\chromedriver")
    for i in range(1,17):
            for theyear in range(2016,2017):
                    allgamesstart = readcsv('allncaafcsfbs.csv')
                    allgamesa = getthegames(driver1,i,theyear,fcs,allgamesstart)
    fcs = False
    for i in range(1,17):
            for theyear in range(2016,2017):
                    allgamesstart = readcsv('allncaafcsfbs.csv')
                    allgamesa = getthegames(driver1,i,theyear,fcs,allgamesstart)
    
    driver1.close()
    print stopit
    #driver1 = webdriver.Firefox()
    #allgamest = gettodaysgames(driver1,0)
    #driver1.close()
    #print stopit
    allgamesa = readcsv('ncaa16.csv')
    teamlist = runtheelo(allgamesa)
    allgamest = readcsvtoday('ncaatoday.csv')
    totalbet = 0
    for thegame in allgamest:
            odds = 1.95
            if int(thegame[2])==thegame[2]:
                    totalbet = makepred(thegame,int(thegame[2]),False,teamlist,odds,totalbet)
            else:
                    totalbet = makepred(thegame,int(thegame[2]),True,teamlist,odds,totalbet)
    
    
    print 'done in tow.', totalbet

run_bets()
