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


def getvoters():

    burl = "http://www.ncaa.com/standings/basketball-men/d1"
    allhrefs = []
    res = requests.get(burl)
    doc = html.fromstring(res.content)

    allvoters = doc.xpath('//*[@id="ncaa-standings-conferences"]//table//a')
    alldivs = doc.xpath('//*[@id="ncaa-standings-conferences"]//div')
    acconf = []
    allteams = []
    for i in range(1,len(alldivs)+1):
        allconfs = doc.xpath('//*[@id="ncaa-standings-conferences"]/div['+str(i)+']//div[contains(@class, "ncaa-standings-conference-name")]')
        allvoters = doc.xpath('//*[@id="ncaa-standings-conferences"]/div['+str(i)+']//table//a')
        
        for conf in allconfs:
            acconf.append([etree.tostring(conf).replace('<div class="ncaa-standings-conference-name">','').replace('</div>','')])
        for voter in allvoters:
            votename = str(voter.attrib['href'])
            votename = votename.replace('alcorn-st','alcorn')
            votename = votename.replace('long-island','liu-brooklyn')
            votename = votename.replace('st-francis-ny','st-francis-brooklyn')
            votename = votename.replace('st-francis-pa','saint-francis-pa')
            votename = votename.replace('loyola-il','loyola-chicago')
            votename = votename.replace('md-east-shore','umes')
            votename = votename.replace('st-peters','saint-peters')
            votename = votename.replace('sc-upstate','usc-upstate')
            allhrefs.append(votename)
            allteams.append([etree.tostring(conf).replace('<div class="ncaa-standings-conference-name">','').replace('</div>','').replace('Southeastern','SEC').replace('Atlantic Coast','ACC').replace('Mid-American','MAC'),votename.replace('/schools/','').replace('/basketball-men',''),voter.text_content()])
            acconf[len(acconf)-1].append(votename.replace('/schools/','').replace('/basketball-men',''))
    writecsvw(allteams,'abbrevTOnames.csv')
    return allhrefs





import sys

allvoters = getvoters()





