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
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                pp = parr[i]
                                spamwriter.writerow(pp)
                        except:
                                print parr[i], i




def getteamlist(driver,conf_name):
    plist = []
    ap = []
    b_url = "https://n.rivals.com/team_rankings/2018/"+conf_name+"/football"
    driver.get(b_url)
    time.sleep(3)
    allteams = driver.find_elements_by_class_name('school-name')
    for team in allteams:
        try:
            teamname = team.find_element_by_class_name('ng-scope')
            if teamname.get_attribute('href') != None:
                ap.append([teamname.get_attribute('innerHTML').replace('&amp;','&'),conf_name])
            elif len(str(teamname.get_attribute('innerHTML')))<50:
                ap.append([teamname.get_attribute('innerHTML').replace('&amp;','&'),conf_name])

        except:
            pass
        
    return ap




driver = webdriver.Chrome()
confs = ['acc','sbelt','big10','aac','ia','midam','mwest','sec','wac','bige','big12','pac12','cusa']
allteams = []
for conf_name in confs:
    allteams = getteamlist(driver,conf_name)
    writecsv(allteams,'conflist.csv')
driver.close()

