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
            acconf[len(acconf)-1].append(votename.replace('/schools/','').replace('/basketball-men',''))
    writecsvw(acconf,'conflist.csv')
    return allhrefs

def getvotes(burl):
    burl = 'http://www.ncaa.com'+burl
    allvotes = [burl[burl.find('schools/')+8:].replace('/basketball-men','')]
    res = requests.get(burl)
    doc = html.fromstring(res.content)

    voteTable = doc.xpath('//*[contains(@class, "ncaa-schools-sport-table")]//tr')
    for i in range(1,len(voteTable)+1):
        opplist = doc.xpath('//*[contains(@class, "ncaa-schools-sport-table")]//tr['+str(i)+']//a')
        scorelist = doc.xpath('//*[contains(@class, "ncaa-schools-sport-table")]//tr['+str(i)+']//td[3]')
        loclist = doc.xpath('//*[contains(@class, "ncaa-schools-sport-table")]//tr['+str(i)+']//td[2]')
        if len(opplist)>0 and len(scorelist)>0 and len(loclist)>0:
            game = loclist[0]
            if game.text_content().find('@')>-1:
                allvotes.append('@')
            elif game.text_content().find('vs.')>-1:
                allvotes.append('vs.')
            else:
                allvotes.append('')
            game = opplist[0]
            allvotes.append(game.attrib['href'].replace('/schools/','').replace('/basketball-men',''))
            game = scorelist[0]
            allvotes.append(game.text_content())

    return allvotes



import sys

allvoters = getvoters()



print len(allvoters)
writecsvw([],'testschedule.csv')
for voter in allvoters:
    try:
        allvotes = getvotes(voter)
        writecsv([allvotes],'testschedule.csv')
    except:
        allvotes = getvotes(voter)
        writecsv([allvotes],'testschedule.csv')



