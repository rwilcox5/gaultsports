import time

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
        voter = doc.xpath('//*[@id="scoreboard"]//section['+str(i)+']//div[contains(@class, "team")]//a')
        if len(voter)>1:
            voter2 = doc.xpath('//*[@id="scoreboard"]//section['+str(i)+']//td[contains(@class, "final")]')
            if len(voter2)>1 and len(voter2[0].text_content())>0 and len(voter2[0].text_content())>0:
                allhrefs.append([voter[0].attrib['href'].replace('/schools/',''), voter[1].attrib['href'].replace('/schools/',''),int(voter2[0].text_content()), int(voter2[1].text_content()),year,month,day])
            elif len(voter2)>1 and int(year)*10000+int(month)*100+int(day)>=today:
                allhrefs.append([voter[0].attrib['href'].replace('/schools/',''), voter[1].attrib['href'].replace('/schools/',''),year,month,day])
    return allhrefs

def getgames():
    allhrefs = []
    yearn = 2017
    today = int(sys.argv[1])*10000+int(sys.argv[2])*100+int(sys.argv[3])
    year = str(yearn)
    for monthn in [11,12]:
        if monthn < 10:
            month = '0'+str(monthn)
        else:
            month = str(monthn)
        for dayn in range(1,32):

            if dayn < 10:
                day = '0'+str(dayn)
            else:
                day = str(dayn)
            print month, day, len(allhrefs)
            try:
                lah = len(allhrefs)
                allhrefs = getdaysgames(year,month,day,today,allhrefs)
                if len(allhrefs)==lah:
                    print soto
            except:
                lah = len(allhrefs)
                allhrefs = getdaysgames(year,month,day,today,allhrefs)
                if len(allhrefs)==lah:
                    print year,month,day

            
        writecsvw(allhrefs,'allgames'+str(yearn)+'.csv')
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
            if dayn < 10:
                day = '0'+str(dayn)
            else:
                day = str(dayn)
            print month, day, len(allhrefs)
            try:
                lah = len(allhrefs)
                allhrefs = getdaysgames(year,month,day,today,allhrefs)
                if len(allhrefs)==lah:
                    print soto
            except:
                lah = len(allhrefs)
                allhrefs = getdaysgames(year,month,day,today,allhrefs)
                if len(allhrefs)==lah:
                    print year,month,day
        writecsvw(allhrefs,'allgames'+str(yearn)+'.csv')
    return allhrefs




import sys

allvoters = getgames()




