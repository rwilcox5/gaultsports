import time
import datetime
import random
import csv
import math
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

def combine():
        allrecs = []
        for ii in range(0,5):
            with open('allrecs'+str(theyear)+str(ii)+'.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    allrecs.append(row)
        writecsv(allrecs,"allrecs"+str(theyear)+"fb.csv")

def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
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
def getdaysgames(year,month,day,today,allhrefs):
    burl = "http://www.ncaa.com/scoreboard/basketball-men/d1/"+year+"/"+month+"/"+day        
    res = requests.get(burl)
    doc = html.fromstring(res.content)

    allvoters = doc.xpath('//*[@id="scoreboard"]//section')
    for i in range(0,len(allvoters)):
        if allvoters[i].get('id') != None:
            allhrefs.append('http://www.ncaa.com/game/'+allvoters[i].get('id')[allvoters[i].get('id').find('/game/')+6:])
        
    return allhrefs

def getgameinfo(burl,year,month,day,allhrefs):
    gameinfo = []
    res = requests.get(burl)
    doc = html.fromstring(res.content)
    loc_str = str(doc.find_class('round-location')[0].text_content()).replace('\n','').replace('\t','')

    gameinfo.append(doc.find_class('school-name')[0].find('a').get('href').replace('/schools/','').replace('/basketball-men',''))
    gameinfo.append(doc.find_class('school-name')[1].find('a').get('href').replace('/schools/','').replace('/basketball-men',''))
    gameinfo.append(int(doc.find_class('game-score')[0].text_content()))
    gameinfo.append(int(doc.find_class('game-score')[1].text_content()))
    gameinfo.append(year)
    gameinfo.append(month)
    gameinfo.append(day)
    gameinfo.append(loc_str)

    allhrefs.append(gameinfo)
    return allhrefs
def getgames():

    allhrefs = []
    yearn = 2017
    now = datetime.datetime.now()
    today = int(now.year)*10000+int(now.month)*100+int(now.day)
    year = str(yearn)

    for monthn in [11,12]:
        if monthn < 10:
            month = '0'+str(monthn)
        else:
            month = str(monthn)
        for dayn in range(1,32):

            if dayn<10 and monthn == 11:
                continue

            if dayn < 10:
                day = '0'+str(dayn)
            else:
                day = str(dayn)
            print year,month,day,len(allhrefs)
            try:
                lah = len(allhrefs)
                allgames = getdaysgames(year,month,day,today,[])
                for i in allgames:
                    try:
                        allhrefs = getgameinfo(i,year,month,day,allhrefs)
                    except:
                        try:
                            allhrefs = getgameinfo(i,year,month,day,allhrefs)
                        except:
                            print i

                if len(allhrefs)==lah:
                    print soto
            except:
                lah = len(allhrefs)
                allgames = getdaysgames(year,month,day,today,[])
                for i in allgames:
                    try:
                        allhrefs = getgameinfo(i,year,month,day,allhrefs)
                    except:
                        try:
                            allhrefs = getgameinfo(i,year,month,day,allhrefs)
                        except:
                            pass
                if len(allhrefs)==lah:
                    print year,month,day

            
        writecsvw(allhrefs,'allgameinfo'+str(yearn)+'.csv')
    year = str(yearn+1)
    for monthn in [1,2,3]:
        if monthn < 10:
            month = '0'+str(monthn)
        else:
            month = str(monthn)
        if monthn==3:
            maxday = 13
        else:
            maxday = 32
        for dayn in range(1,maxday):
            if dayn<10 and monthn == 11:
                continue

            if dayn < 10:
                day = '0'+str(dayn)
            else:
                day = str(dayn)
            print year,month,day,len(allhrefs)
            try:
                lah = len(allhrefs)
                allgames = getdaysgames(year,month,day,today,[])
                for i in allgames:
                    try:
                        allhrefs = getgameinfo(i,year,month,day,allhrefs)
                    except:
                        try:
                            allhrefs = getgameinfo(i,year,month,day,allhrefs)
                        except:
                            pass
                if len(allhrefs)==lah:
                    print soto
            except:
                lah = len(allhrefs)
                allgames = getdaysgames(year,month,day,today,[])
                for i in allgames:
                    try:
                        allhrefs = getgameinfo(i,year,month,day,allhrefs)
                    except:
                        try:
                            allhrefs = getgameinfo(i,year,month,day,allhrefs)
                        except:
                            pass
                if len(allhrefs)==lah:
                    print year,month,day
        writecsvw(allhrefs,'allgameinfo'+str(yearn)+'.csv')
    return allhrefs




import sys

allvoters = getgames()




