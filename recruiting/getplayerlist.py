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

theyear = int(sys.argv[2])
nstars = int(sys.argv[1])
basefile = sys.argv[3]


def writecsvstr(parr, filen):
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                pp = [parr[i]]
                                spamwriter.writerow(pp)
                        except:
                                print parr[i], i




def getplayerlist(driver):
    plist = []
    ap = []
    burlarr = ["https://n.rivals.com/search#?formValues=%257B%2522sport%2522:%2522Football%2522,%2522stars%2522:%257B%2522range%2522:%2522lte%2522,%2522number%2522:1%257D,%2522status%2522:%255B%2522signed%2522,%2522verbal%2522%255D,%2522recruit_year%2522:"+str(theyear)+",%2522page_number%2522:1%257D"]
    burlarr.append("https://n.rivals.com/search#?formValues=%257B%2522sport%2522:%2522Football%2522,%2522stars%2522:%257B%2522range%2522:%2522eq%2522,%2522number%2522:2%257D,%2522status%2522:%255B%2522signed%2522,%2522verbal%2522%255D,%2522recruit_year%2522:"+str(theyear)+",%2522page_number%2522:1%257D")
    burlarr.append("https://n.rivals.com/search#?formValues=%257B%2522sport%2522:%2522Football%2522,%2522stars%2522:%257B%2522range%2522:%2522eq%2522,%2522number%2522:3%257D,%2522status%2522:%255B%2522signed%2522,%2522verbal%2522%255D,%2522recruit_year%2522:"+str(theyear)+",%2522page_number%2522:1%257D")
    burlarr.append("https://n.rivals.com/search#?formValues=%257B%2522sport%2522:%2522Football%2522,%2522stars%2522:%257B%2522range%2522:%2522eq%2522,%2522number%2522:4%257D,%2522status%2522:%255B%2522signed%2522,%2522verbal%2522%255D,%2522recruit_year%2522:"+str(theyear)+",%2522page_number%2522:1%257D")
    burlarr.append("https://n.rivals.com/search#?formValues=%257B%2522sport%2522:%2522Football%2522,%2522stars%2522:%257B%2522range%2522:%2522eq%2522,%2522number%2522:5%257D,%2522status%2522:%255B%2522signed%2522,%2522verbal%2522%255D,%2522recruit_year%2522:"+str(theyear)+",%2522page_number%2522:1%257D")
    
    b_url = "https://news.ycombinator.com/item?id=12792928"
    driver.get(b_url)
    b_url = burlarr[nstars-1]
    driver.get(b_url)
    driver.find_element_by_class_name('btn-primary').click()
    time.sleep(3)
    for i in range(0,30):

        getplayers = driver.find_elements_by_class_name("player-name-prospects")
        for ii in getplayers:
                try:
                        if ii.find_element_by_tag_name("a").get_attribute("href") not in ap:
                                ap.append(ii.find_element_by_tag_name("a").get_attribute("href"))
                        #print ii.find_element_by_tag_name("a").get_attribute("href")
                except:
                        pass
     

        allbtn = driver.find_elements_by_tag_name("a")
        print len(allbtn),
        for ii in allbtn:
                if ii.text=='Next':
                        try:
                                ii.click()
                                time.sleep(3)
                        except:
                                pass


    print '\n',len(ap)
        
    return ap




driver = webdriver.Chrome()
allplayers = getplayerlist(driver)
writecsvstr(allplayers,basefile+str(theyear)+str(nstars)+".csv")
driver.close()

