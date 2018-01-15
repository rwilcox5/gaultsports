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

def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa


yearn = 2017
allscores = readcsv('allscores'+str(yearn)+'.csv')
allinfo = readcsv('allgameinfo'+str(yearn)+'.csv')
for idx,i in enumerate(allinfo):
    allinfo[idx][0]=allinfo[idx][0].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell').replace('usc-upstate','sc-upstate')
    allinfo[idx][1]=allinfo[idx][1].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell').replace('usc-upstate','sc-upstate')
writecsvw(allinfo,'allgameinfo'+str(yearn)+'.csv') 
for idx,i in enumerate(allscores):
    allscores[idx][0]=allscores[idx][0].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell').replace('usc-upstate','sc-upstate')
    allscores[idx][1]=allscores[idx][1].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell').replace('usc-upstate','sc-upstate')
writecsvw(allscores,'allscores'+str(yearn)+'.csv') 

for idx,i in enumerate(allscores):
    for ii in allinfo:
        try:
            if i[:7]==ii[:7] and len(ii)>7:
                allscores[idx].append(ii[7])
        except:
            pass
writecsvw(allscores,'allgames'+str(yearn)+'.csv')






