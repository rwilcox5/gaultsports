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

def getgamedata(driver,qb_id):
    b_url = "http://www.nfl.com/player/tombrady/"+str(qb_id)+"/gamelogs"
    driver.get(b_url)
    time.sleep(2)
    alltables = driver.find_elements_by_class_name('data-table1')
    allgames = []
    for data_table in alltables:
        season_type = 'Not'
        all_cells = data_table.find_elements_by_tag_name('td')
        for cell in all_cells:
            if cell.get_attribute('innerHTML')=='Preseason':
                season_type = 'Pre'
            if cell.get_attribute('innerHTML')=='Regular Season':
                season_type = 'Reg'
            if cell.get_attribute('innerHTML')=='Postseason':
                season_type = 'Post'
        if season_type != 'Not':
            table_body = data_table.find_element_by_tag_name('tbody')
            all_rows = table_body.find_elements_by_tag_name('tr')
            for row in all_rows:
                all_cells = row.find_elements_by_tag_name('td')
                if len(all_cells)==22:
                    oppname = str(all_cells[2].find_elements_by_tag_name('a')[-1].get_attribute('href'))
                    oppname = oppname[oppname.find('=')+1:]
                    allgames.append([qb_id,season_type,str(all_cells[0].get_attribute('innerHTML')),str(all_cells[1].get_attribute('innerHTML')),oppname,str(all_cells[6].get_attribute('innerHTML')),str(all_cells[7].get_attribute('innerHTML')),str(all_cells[9].get_attribute('innerHTML')),str(all_cells[11].get_attribute('innerHTML')),str(all_cells[12].get_attribute('innerHTML'))])

    return allgames






driver = webdriver.Chrome()
allqbs = getqblist(driver)
print allqbs

writecsv([],"qbgames2017.csv")
for qb_id in allqbs:
    print qb_id
    allgames = getgamedata(driver,qb_id)
    writecsva(allgames,"qbgames2017.csv")
driver.close()

