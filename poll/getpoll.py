import time

import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


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


def getvoters(driver):

    b_url = "https://collegefootball.ap.org/poll"
    allhrefs = []
    driver.get(b_url)
    time.sleep(1)
    driver.find_element_by_id('voter-menu').click()
    time.sleep(1)
    voterMenu = driver.find_element_by_xpath('//*[@id="block-ap-poll-top-25-left-nav"]/div/div/div[2]/div/div[2]/div')
    allvoters = voterMenu.find_elements_by_tag_name('a')
    for voter in allvoters:
        print voter.get_attribute('href')
        allhrefs.append(str(voter.get_attribute('href')).replace('http:','https:'))
    return allhrefs

def getvotes(b_url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-javascript")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    allvotes = [b_url[b_url.find('voter/')+6:]]
    time.sleep(1)
    driver.get(b_url)
    time.sleep(1)
    pollTable = driver.find_element_by_id('poll-content')
    time.sleep(1)
    voteTable = pollTable.find_elements_by_tag_name('tr')
    print len(voteTable), b_url
    for vote in voteTable:
        isheader = vote.find_elements_by_tag_name('th')
        if len(isheader)==0:
            allvotes.append(vote.find_element_by_tag_name('a').get_attribute('href'))
    driver.close()
    return allvotes



import sys
weekn = str(sys.argv[1])
chrome_options = Options()
chrome_options.add_argument("--disable-javascript")
driver = webdriver.Chrome(chrome_options=chrome_options)
allvoters = getvoters(driver)
allvotes = []
driver.close()
for voter in allvoters[9:]:
    try:
        allvotes = getvotes(voter)
        writecsv([allvotes],'week'+weekn+'temp.csv')
    except:
        allvotes = getvotes(voter)
        writecsv([allvotes],'week'+weekn+'temp.csv')
driver.close()


