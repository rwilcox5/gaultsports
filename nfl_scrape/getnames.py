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





def getqblist(driver):
    b_url = "http://www.nfl.com/players/search?category=position&filter=quarterback&conferenceAbbr=null&playerType=current&conference=ALL"
    driver.get(b_url)
    time.sleep(2)
    allqbs = []
    alllinks = driver.find_elements_by_tag_name('a')
    for i in alllinks:
        plink = i.get_attribute('href')
        pindex = plink.find('/player/')
        ppindex = plink.find('/',pindex+9)
        eindex = plink.find('/',ppindex+1)
        if pindex>-1 and ppindex>-1 and eindex >-1:
            allqbs.append(int(plink[ppindex+1:eindex]))
            allqbs.append(str(i.get_attribute('innerHTML')))

    b_url = "http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=quarterback&conferenceAbbr=null"
    driver.get(b_url)
    time.sleep(2)
    alllinks = driver.find_elements_by_tag_name('a')
    for i in alllinks:
        plink = i.get_attribute('href')
        pindex = plink.find('/player/')
        ppindex = plink.find('/',pindex+9)
        eindex = plink.find('/',ppindex+1)
        if pindex>-1 and ppindex>-1 and eindex >-1:
            allqbs.append(int(plink[ppindex+1:eindex])) 
            allqbs.append(str(i.get_attribute('innerHTML')))
       
    return allqbs


driver = webdriver.Chrome()
allqbs = getqblist(driver)
print allqbs






