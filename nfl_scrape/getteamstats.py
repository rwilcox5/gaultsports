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

year = int(sys.argv[1])


def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

def writecsva(parr, filen):
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i
def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i
def writecsvstr(parr, filen):
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                pp = [parr[i]]
                                spamwriter.writerow(pp)
                        except:
                                print parr[i], i
def combine():
        allrecs = []
        for ii in range(0,5):
            with open('allrecs'+str(theyear)+str(ii)+'.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    allrecs.append(row)
        writecsv(allrecs,"allrecs"+str(theyear)+"fb.csv")





def getgamelist(driver,year,week):
    b_url = "http://www.nfl.com/scores/"+str(year)+"/REG"+str(week)
    driver.get(b_url)
    time.sleep(2)
    allgames = []
    alllinks = driver.find_elements_by_class_name('game-center-link')
    for i in alllinks:
        allgames.append(i.get_attribute('href')+'#menu=gameinfo&tab=analyze')
    
       
    return allgames

def getgamedata(driver,b_url,teams,week):
    
    ateam = b_url[b_url.find('REG'+str(week))+len('REG'+str(week))+1:b_url.find('@')]
    hteam = b_url[b_url.find('@')+1:b_url.find('#menu')]
    ateamid = -1
    hteamid = -1
    adonebefore = False
    hdonebefore = False
    for idx,i in enumerate(teams):
        if i[0]==ateam:
            ateamid = idx
            for ii in range(0,len(i)/9):
                if int(i[ii*9+1])==int(week):
                    adonebefore = True
        elif i[0]==hteam:
            hteamid = idx
            for ii in range(0,len(i)/9):
                if int(i[ii*9+1])==int(week):
                    hdonebefore = True
    if ateamid == -1:
        teams.append([str(ateam)])
        ateamid = len(teams)-1
    if hteamid == -1:
        teams.append([str(hteam)])
        hteamid = len(teams)-1
    if adonebefore and hdonebefore:
        return teams
    else:
        driver.get(b_url)
        time.sleep(2)
        allcells = driver.find_elements_by_tag_name('td')
        apass = -1000
        hpass = -1000
        arush = -1000
        hrush = -1000
        apts = -1000
        hpts = -1000
        for cellid,cell in enumerate(allcells):
            if str(cell.get_attribute("innerHTML")).find('Net Yards Passing')>-1:
                if apass == -1000:
                    apass = int(allcells[cellid+1].get_attribute("innerHTML"))
                else:
                    hpass = int(allcells[cellid+1].get_attribute("innerHTML"))
            if str(cell.get_attribute("innerHTML")).find('Net Yards Rushing')>-1:
                if arush == -1000:
                    arush = int(allcells[cellid+1].get_attribute("innerHTML"))
                else:
                    hrush = int(allcells[cellid+1].get_attribute("innerHTML"))
            if str(cell.get_attribute("innerHTML")).find('Final Score')>-1:
                if apts == -1000:
                    apts = int(allcells[cellid+1].get_attribute("innerHTML"))
                else:
                    hpts = int(allcells[cellid+1].get_attribute("innerHTML"))
        if not adonebefore:
            teams[ateamid].append(week)
            teams[ateamid].append(ateamid)
            teams[ateamid].append(hteamid)
            teams[ateamid].append(apass)
            teams[ateamid].append(arush)
            teams[ateamid].append(apts)
            teams[ateamid].append(hpass)
            teams[ateamid].append(hrush)
            teams[ateamid].append(hpts)
        if not hdonebefore:
            teams[hteamid].append(week)
            teams[hteamid].append(ateamid)
            teams[hteamid].append(hteamid)
            teams[hteamid].append(hpass)
            teams[hteamid].append(hrush)
            teams[hteamid].append(hpts)
            teams[hteamid].append(apass)
            teams[hteamid].append(arush)
            teams[hteamid].append(apts)
        return teams


driver = webdriver.Chrome()
try:
    teams = readcsv("nflg.csv")
except:
    teams = []
for week in range(1,8):
    print week
    allgames = getgamelist(driver,year,week)
    for game in allgames:
        teams = getgamedata(driver,game,teams,week)
        writecsv(teams,"nflg.csv")
driver.close()

