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

def getteams(driver):
    b_url = "http://collegefootball.ap.org/conferences"
    driver.get(b_url)
    time.sleep(1)
    alllinks = driver.find_elements_by_tag_name('a')
    convertnames = []
    for link in alllinks:
        index = str(link.get_attribute('href')).find('collegefootball.ap.org/teams/')
        if index >-1:
            convertnames.append([str(link.get_attribute('href'))[index+29:], str(link.get_attribute('innerHTML'))])
    return convertnames
driver = webdriver.Chrome()
convertnames = getteams(driver)
print convertnames
driver.close()