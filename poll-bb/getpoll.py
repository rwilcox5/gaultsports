import time
import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import lxml
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from lxml.cssselect import CSSSelector
import requests

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
    b_url = "https://collegebasketball.ap.org/poll"
    allhrefs = []
    driver.get(b_url)
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "voter-menu"))
        )
    element.click()
    time.sleep(1)
    voterMenu = driver.find_element_by_xpath('//*[@id="block-ap-poll-top-25-left-nav"]/div/div/div[2]/div/div[2]/div')
    allvoters = voterMenu.find_elements_by_tag_name('a')
    for voter in allvoters:
        print voter.get_attribute('href')
        allhrefs.append(str(voter.get_attribute('href')).replace('http:','https:'))
    return allhrefs

def getvotes(burl):
    allvotes = [burl[burl.find('voter/')+6:]]
    res = requests.get(burl)
    doc = html.fromstring(res.content)
    voteTable = doc.xpath("//td[contains(@class, 'tname')]//a")
    for vote in voteTable[:25]:
        allvotes.append(vote.attrib['href'].replace('/teams/',''))
    return allvotes

import sys
weekn = str(sys.argv[1])
driver = webdriver.PhantomJS()
allvoters = getvoters(driver)
allvotes = []
driver.close()
for voter in allvoters[0:]:
    try:
        allvotes = getvotes(voter)
        writecsv([allvotes],'ap1718/week'+weekn+'temp.csv')
    except:
        allvotes = getvotes(voter)
        writecsv([allvotes],'ap1718/week'+weekn+'temp.csv')
