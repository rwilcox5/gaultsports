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
import lxml
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from lxml.cssselect import CSSSelector
import requests

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
       
    return allqbs

def getgamedata(qb_id):
    burl = "http://www.nfl.com/player/tombrady/"+str(qb_id)+"/gamelogs"
    res = requests.get(burl)
    doc = html.fromstring(res.content)
    alltables = doc.find_class('data-table1')
    allgames = []
    for i in range(1,len(alltables)+1):
        season_type = 'Not'
        all_cells = doc.xpath('//*[@id="player_profile_tabs_0"]/table['+str(i)+']/thead/tr[1]//td')
        for cell in all_cells:
            if cell.text_content()=='Preseason':
                season_type = 'Pre'
            if cell.text_content()=='Regular Season':
                season_type = 'Reg'
            if cell.text_content()=='Postseason':
                season_type = 'Post'

        if season_type != 'Not':
            all_rows = doc.xpath('//*[@id="player_profile_tabs_0"]/table['+str(i)+']/tbody//tr')
            for ii in range(0,len(all_rows)+1):
                all_cells = doc.xpath('//*[@id="player_profile_tabs_0"]/table['+str(i)+']/tbody/tr['+str(ii)+']//td')
                if len(all_cells)==22:
                    oppname = str(doc.xpath('//*[@id="player_profile_tabs_0"]/table['+str(i)+']/tbody/tr['+str(ii)+']/td[3]//a')[-1].attrib['href'])
                    oppname = oppname[oppname.find('=')+1:]
                    allgames.append([qb_id,season_type,str(all_cells[0].text_content()),str(all_cells[1].text_content()),oppname,str(all_cells[6].text_content()),str(all_cells[7].text_content()),str(all_cells[9].text_content()),str(all_cells[11].text_content()),str(all_cells[12].text_content())])

    return allgames






driver = webdriver.Chrome()
allqbs = getqblist(driver)
print allqbs
driver.close()
writecsv([],"qbgames2017.csv")
for qb_id in allqbs:
    print qb_id
    allgames = getgamedata(qb_id)
    writecsva(allgames,"qbgames2017.csv")


