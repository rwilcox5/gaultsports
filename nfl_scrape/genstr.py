import random
import csv
import time
import sys
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

alldata = readcsv('qbgames2017.csv')

allgames = []
allchars = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','_','_','_','_','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alldata:
    if i[6]!= '--':
        try:
            qbid = int(i[0])
        except:
            qbid = 0
        try:
            passcomp = int(i[5])
        except:
            passcomp = 0
        try:
            passatt = int(i[6])
        except:
            passatt = 0
        try:
            passyard = int(i[7])
        except:
            passyard = 0
        try:
            passtd = int(i[8])
        except:
            passtd = 0
        try:
            passint = int(i[9])
        except:
            passint = 0
        try:
            year = int(2017)
        except:
            year = 1900
        try:
            opponent = 0
            for iidx,ii in enumerate(i[4]):
                for iiidx,iii in enumerate(allchars):
                    if iii==ii:
                        opponent += 59**iidx*opponent+iiidx
                        break
        except:
            opponent = 0
        try:
            week = int(i[2])
        except:
            week = 0
        try:
            if i[1]=='Pre':
                gametype = 0
            elif i[1]=='Reg':
                gametype = 1
            elif i[1]=='Post':
                gametype = 2
            else:
                gametype = 3
        except:
            gametype = 0
            
        allgames.append([qbid,passatt,passcomp,passyard,passtd,passint,year,opponent,week,gametype])

allseasons = []
for i in allgames:
    alreadyin = False
    for iidx,ii in enumerate(allseasons):
        if i[0]==ii[0] and i[6]==ii[6] and i[9]==ii[7]:
            allseasons[iidx][1]+=i[1]
            allseasons[iidx][2]+=i[2]
            allseasons[iidx][3]+=i[3]
            allseasons[iidx][4]+=i[4]
            allseasons[iidx][5]+=i[5]
            alreadyin = True
    if not alreadyin:
        allseasons.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[9]])

istr = 'var gamedata = ['
dstr = 'var namedata = ['
ngames = len(allgames)
for i in range(0,ngames):
	istr += str(allgames[i][7])+","+str(allgames[i][1])+","+str(allgames[i][2])+","+str(allgames[i][3])+","+str(allgames[i][4])+","+str(allgames[i][5])+","+str(allgames[i][6])+","+str(allgames[i][8])+","+str(allgames[i][9])
	if i ==ngames-1:
		istr += "];"
	else:
		istr += ","
	dstr += str(allgames[i][0])
	if i ==ngames-1:
		dstr += "];"
	else:
		dstr += ","

sistr = 'var seasondata = ['
sdstr = 'var seasonname = ['
ngames = len(allseasons)
for i in range(0,ngames):

    sistr += str(allseasons[i][7])+","+str(allseasons[i][1])+","+str(allseasons[i][2])+","+str(allseasons[i][3])+","+str(allseasons[i][4])+","+str(allseasons[i][5])+","+str(allseasons[i][6])
    if i ==ngames-1:
        sistr += "];"
    else:
        sistr += ","
    sdstr += str(allseasons[i][0])
    if i ==ngames-1:
        sdstr += "];"
    else:
        sdstr += ","


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
qbnamestr = ''
for i in range(0,len(allqbs)/2):
    qbnamestr += str(allqbs[2*i])
    qbnamestr += ",'"
    qbnamestr += str(allqbs[2*i+1])
    qbnamestr += "',"
qbnamestr = qbnamestr[:-1]+'];'

f = open('helloworld.txt','w')
f.write(istr+'\n'+dstr+'\n'+sistr+'\n'+sdstr+'\nvar ngames = '+str(len(allgames))+';\nvar nseasons = '+str(len(allseasons))+';\nvar qbconvertNew = ['+qbnamestr)
f.close()
driver.close()

