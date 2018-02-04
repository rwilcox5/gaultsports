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
    b_url = "http://collegebasketball.ap.org/conferences"
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

#driver = webdriver.Chrome()
#allteams = getapteamsconfs(driver)
#writecsv(allteams,'aplist.csv')
#driver.close()
#print soto

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

driver = webdriver.Chrome()
this_week = int(sys.argv[1])
for week in range(0,this_week-1):
    b_url = "https://www.masseyratings.com/cb/arch/compare2018-"+str(week)+".htm"
    allteams = getmasseyids(driver,b_url)
    writecsv(allteams,'massey1718/masseyweek'+str(week)+'.csv')
b_url = "https://www.masseyratings.com/cb/compare.htm"
masseyteams = getmasseyids(driver,b_url)
writecsv(masseyteams,'massey1718/masseyweek'+str(this_week-1)+'.csv')
allteams = []
for i in masseyteams[:351]:
    if i[0] not in allteams:
        allteams.append(i[0])
print len(allteams)

#driver.close()


def getgames(teamid,driver):
    b_url = 'https://www.masseyratings.com/team.php?t='+str(teamid)+'&s=298892'

    time.sleep(1)
    driver.get(b_url)

    time.sleep(1)
    voteTable = driver.find_elements_by_class_name('bodyrow')
    print len(voteTable)
    allgames = []
    for vote in voteTable:

        game = []
        isheader = vote.find_elements_by_tag_name('td')
        if isheader[4].get_attribute('innerHTML').find('W')>-1 or isheader[4].get_attribute('innerHTML').find('L')>-1:
            tname = isheader[2].find_element_by_tag_name('a').get_attribute('href')
            sindex = tname.find('?t=')
            eindex = tname.find('&',sindex+3)

            
            if str(isheader[1].get_attribute('innerHTML'))=='at':
                game.append(teamid)
                game.append(str(tname[sindex+3:eindex]))
            else:
                game.append(str(tname[sindex+3:eindex]))
                game.append(teamid)


            game.append(str(isheader[0].find_element_by_class_name('detail').get_attribute('innerHTML'))) #Date of Game



            if str(isheader[1].get_attribute('innerHTML'))=='at':

                game.append(isheader[5].get_attribute('innerHTML'))
                game.append(isheader[6].get_attribute('innerHTML'))

            else:
                game.append(isheader[6].get_attribute('innerHTML'))
                game.append(isheader[5].get_attribute('innerHTML'))
            if str(isheader[1].get_attribute('innerHTML')).find('vs')>-1:
                game.append('neutral')


            allgames.append(game)


    return allgames




allvotes = []


#This gets team ids-change getteams 2nd argument to 1
#writecsv(allteams,'convert.csv')
#print soto

writecsv('','results.csv')
for team in allteams:
    print team

    allvotes = getgames(team,driver)
    writecsva(allvotes,'results.csv')


driver.close()



