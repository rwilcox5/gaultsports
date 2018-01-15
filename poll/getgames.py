import time
import sys
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


def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i

def writecsva(parr, filen):
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i


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

def getapteamsconfs(driver):
    b_url = "http://collegefootball.ap.org/conferences"
    allhrefs = []
    driver.get(b_url)
    time.sleep(1)
    allcontent = driver.find_elements_by_class_name('content')
    allteamarray = []
    for content in allcontent:
        try:
            alldivs = content.find_elements_by_tag_name('div')
            if str(alldivs[0].get_attribute('innerHTML')).find('ACC')==-1:
                print soto
            for div in alldivs:
                try:
                    confname = div.find_element_by_tag_name('h2').find_element_by_tag_name('a').get_attribute('innerHTML')
                    allteams = div.find_element_by_tag_name('div').find_elements_by_tag_name('a')
                    for team in allteams:
                        tlink = team.get_attribute('href')
                        index = 0
                        while index >-1:
                            index = tlink.find('/',index+1)
                            if index>-1:
                                index0 = index 
                        teamarray = [str(confname),str(tlink[index0+1:])]
                        allteamarray.append(teamarray)
                except:
                    pass
            break
        except:
            pass
    return allteamarray


def getmasseyids(driver,b_url):
    
    allhrefs = []
    driver.get(b_url)
    time.sleep(1)
    allcontent = driver.find_element_by_tag_name('pre')
    allteamarray = []
    data_str = str(allcontent.get_attribute('innerHTML'))
    index = 0
    allhrefs = []
    while index>-1:
        index = data_str.find('<a href=',index+1)
        allhrefs.append(index)
    allteams = []
    for index in allhrefs:
        sindex = data_str.find('?t=',index)
        eindex = data_str.find('&',sindex)
        eeindex = data_str.find('>',eindex)
        eeeindex = data_str.find('<',eeindex)
        if eindex >-1 and sindex > -1 and eeindex > -1 and eeeindex > -1:
            addteam = True
            for i in allteams:
                if data_str[sindex+3:eindex]==i[0]:
                    addteam = False
                    break
            if addteam:
                allteams.append([data_str[sindex+3:eindex], data_str[eeindex+1:eeeindex]])
    return allteams

driver = webdriver.PhantomJS()
this_week = int(sys.argv[1])
for week in range(0,this_week-1):
    b_url = "https://www.masseyratings.com/cf/arch/compare2017-"+str(week)+".htm"
    allteams = getmasseyids(driver,b_url)
    writecsv(allteams,'massey2017/masseyweek'+str(week)+'.csv')
b_url = "https://www.masseyratings.com/cf/compare.htm"
allteams = getmasseyids(driver,b_url)
writecsv(allteams,'massey2017/masseyweek'+str(this_week-1)+'.csv')
driver.close()



def getteams(driver,with_names):
    b_url = "http://www.espn.com/college-football/standings"
    allhrefs = []
    driver.get(b_url)
    time.sleep(2)
    alltrs = driver.find_elements_by_class_name('standings-row')
    for cell in alltrs:
        td = cell.find_element_by_tag_name('td')
        link = td.find_element_by_tag_name('a')
        teamlink = link.get_attribute('href')
        sindex = teamlink.find('/id')
        eindex = teamlink.find('/',sindex+4)
        if with_names==0:
            allhrefs.append(str(teamlink[sindex+4:eindex]))
        else:
            allhrefs.append([str(teamlink[sindex+4:eindex]),str(teamlink[eindex+1:])])

    return allhrefs

def getgames(teamid):
    burl = 'http://www.espn.com/college-football/team/schedule?id='+teamid+'&year=2017'
    res = requests.get(burl)
    doc = html.fromstring(res.content)


    voteTable = doc.xpath('//*[@id="showschedule"]/div/table//tr')
    allgames = []
    print teamid
    for i in range(3,len(voteTable)+1):
        try:
            game = []
            isheader = doc.xpath('//*[@id="showschedule"]/div/table/tr['+str(i)+']//td')
            tname = doc.xpath('//*[@id="showschedule"]/div/table/tr['+str(i)+']/td[2]//a')[0].attrib['href']
            sindex = tname.find('/id')
            eindex = tname.find('/',sindex+4)

            
            if str(isheader[1].find_class('game-status')[0].text_content())=='@':
                game.append(teamid)
                game.append(str(tname[sindex+4:eindex]))
            else:
                game.append(str(tname[sindex+4:eindex]))
                game.append(teamid)
            game.append(str(isheader[0].text_content()))

            score_str = str(doc.xpath('//*[@id="showschedule"]/div/table/tr['+str(i)+']/td[3]//a')[0].text_content())
            dindex = score_str.find('-')

            if str(isheader[1].find_class('game-status')[0].text_content())=='@':
                if str(isheader[2].text_content()).find('L')>-1:
                    game.append(score_str[dindex+1:])
                    game.append(score_str[:dindex])
                else:
                    game.append(score_str[:dindex])
                    game.append(score_str[dindex+1:])
            else:
                if str(isheader[2].text_content()).find('L')==-1:
                    game.append(score_str[dindex+1:])
                    game.append(score_str[:dindex])
                else:
                    game.append(score_str[:dindex])
                    game.append(score_str[dindex+1:])

            allgames.append(game)
        except:
            try:
                game = []
                isheader = doc.xpath('//*[@id="showschedule"]/div/table/tr['+str(i)+']//td')
                tname = doc.xpath('//*[@id="showschedule"]/div/table/tr['+str(i)+']/td[2]//a')[0].attrib['href']
                sindex = tname.find('/id')
                eindex = tname.find('/',sindex+4)

                
                if str(isheader[1].find_class('game-status')[0].text_content())=='@':
                    game.append(teamid)
                    game.append(str(tname[sindex+4:eindex]))
                else:
                    game.append(str(tname[sindex+4:eindex]))
                    game.append(teamid)
                game.append(str(isheader[0].text_content()))
                allgames.append(game)
            except:
                pass


    return allgames



import sys
driver = webdriver.PhantomJS()
allteams = getteams(driver,0)
print len(allteams)
driver.close()
allvotes = []


#This gets team ids-change getteams 2nd argument to 1
#writecsv(allteams,'convert.csv')
#print soto

writecsv('','results.csv')
getgamesyet = True
teamagain = []
for team in allteams:
    if getgamesyet:
        try:
            allvotes = getgames(team)
            writecsva(allvotes,'results.csv')
        except:
            teamagain.append(team)
teamagain2 = []
for team in teamagain:
    if getgamesyet:
        try:
            allvotes = getgames(team)
            writecsva(allvotes,'results.csv')
        except:
            teamagain2.append(team)
teamagain3 = []
for team in teamagain2:
    if getgamesyet:
        try:
            allvotes = getgames(team)
            writecsva(allvotes,'results.csv')
        except:
            teamagain3.append(team)
print teamagain3




