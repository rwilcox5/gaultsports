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

theyear = int(sys.argv[1])
basefile = sys.argv[2]
nthreads = 5

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




def getreclist(driver,linkurl,allsl,pstars):
    burl = ""
    for i in linkurl:
        burl=burl+i
    plist = []
    driver.get(burl)
    getcollegetable = driver.find_element_by_id("college_choices")

    getschools = getcollegetable.find_elements_by_tag_name("tr")
    schoollink= [burl,str(theyear),pstars]

    for ii in getschools[1:]:
            
            trow = ii.find_elements_by_tag_name("td")
            yt = trow[0].text
            toffer = trow[2].get_attribute("innerHTML")
            index = trow[1].text.find('Committed',0)
            if index > -1:
                    schoollink.append(yt)
            else:
                    index = trow[1].text.find('Enrolled',0)
                    if index > -1:
                            schoollink.append(yt)
                    else:
                        index = trow[1].text.find('Signed',0)
                        if index > -1:
                                schoollink.append(yt)


    #The losing schools
    for ii in getschools[1:]:
            trow = ii.find_elements_by_tag_name("td")
            yt = trow[0].text
            toffer = trow[2].get_attribute("innerHTML")
            if len(toffer) > 1:
                    indexc = trow[1].text.find('Committed',0)
                    indexe = trow[1].text.find('Enrolled',0)
                    indexs = trow[1].text.find('Signed',0)
                    if indexc == -1 and indexe == -1 and indexs == -1:
                            schoollink.append(yt)
                            
                    
            
    allsl.append(schoollink)

    return allsl
    #print schoollink





def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa
def readcsva(filen):
        allgamesa  =[]
        for ii in range(0,nthreads):
            try:
                with open(filen+str(ii)+'.csv', 'rb') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                        for row in spamreader:
                                allgamesa.append(row[0])
            except:
                pass
        return allgamesa

playersdone = readcsva(basefile+str(theyear)+"done")

allplayersa = readcsv(basefile+str(theyear)+".csv")
allplayers = []

for i in allplayersa:
        if i[0] not in playersdone:
                allplayers.append(i)
print len(allplayers)


def runthis(driver,ii):
        lx =len(allplayers)
        for iiii in allplayers[(lx/nthreads+1)*ii:min((lx/nthreads+1)*(1+ii),lx)]:
                i = iiii[0]
                try:
                        allsl = getreclist(driver,i,[],iiii[1])
                        writecsva(allsl,basefile+str(theyear)+'done'+str(ii)+".csv")
                except:
                        break
                        
        print ii, "DONE"
        driver.close()

driver = []
t = []

for i in range(0,nthreads):
        t.append(0)

        options = webdriver.ChromeOptions() 

        driver.append(webdriver.Chrome(chrome_options=options))
        driver[i].implicitly_wait(30)
        t[i] = Thread(target=runthis,args=(driver[i],i))
        t[i].start()
        print "TAC=", threading.active_count()
        print "started", i


