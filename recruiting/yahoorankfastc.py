import time

import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
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

pagen = 10
theyear = 2017

#combine()



allplayers = []
try:
    with open('allplayers'+str(theyear)+'.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            allplayers.append(row)
except:
    pass


##This gets all the owners from the conferences to check if sims or not.

def getplayerlist(driver,pagen):
    plist = []
    ap = []
    for nstars in range(0,3):
            b_url = "http://sports.yahoo.com/ncaa/football/recruiting/recruit-search"
            driver.get(b_url)
            yearselect = Select(driver.find_element_by_id("class-year-football"))
            yearselect.select_by_visible_text(str(theyear))
            uncselect = driver.find_element_by_id("uncommitted-football").click()
            nstarselect= Select(driver.find_element_by_id("star-level-type-football"))
            if nstars ==0:
                    nstarselect.select_by_visible_text("Greater than")
            elif nstars ==1:
                    nstarselect.select_by_visible_text("Exactly")
            else:
                    nstarselect.select_by_visible_text("Less than")
            nstarselect= Select(driver.find_element_by_id("star-level-football"))
            nstarselect.select_by_visible_text("2 stars")
            subselect = driver.find_element_by_class_name("ysr-submit-advanced-search").click()
            for i in range(0,200):

                getplayers = driver.find_element_by_id("ysr-search-results")
                allplayers = getplayers.find_elements_by_tag_name("th")
                for ii in allplayers:
                        try:
                                ap.append(ii.find_element_by_tag_name("a").get_attribute("href"))
                        except:
                                pass
                
                
               
                        

                nextselect = driver.find_elements_by_xpath("//button[@name='start'][@type='submit']")
                ntl = len(nextselect)-2
                if nextselect[ntl].get_attribute('class')!="inactive":
                        print nextselect[ntl].get_attribute('innerHTML')
                        nextselect[ntl].click()
                else:
                        break
    print len(ap)
        
    return ap
def getfrontteam(all_links,all_no):
    plist = []
    indexen = all_no.find("/TimelineEvents",0)
    indexs = all_no.find("<th>Recruited By</th>",0)
    yt = all_no[indexs:indexen]
    index = 0
    for i in range(0,10):
            index = yt.find(".247sports.com/Season/"+str(theyear)+"-Football/Commits",index+1)
            if index != -1:
                inds = yt.find("http://",0)
                indes = inds
                while inds < index:
                        inds = yt.find("http://",inds+1)
                        if inds < index:
                                if inds > -1:
                                        indes = inds
                        if inds == -1:
                                inds = 10000000
                ytt = ""
                for iii in range(indes+7,index):
                    ytt=ytt+yt[iii]
                try:
                    plist.append([ytt])
                except:
                    donot = 0
            else:
                    break

    yt = ""
    index = 0
    list1 = []
   
    if all_no.find("<span>-</span>",0)>-1:
            while index < indexen:
                index = all_no.find("<span>-</span>",index+1)
                if index < indexen:
                        if index > indexs:
                                list1.append(index)
                if index == -1:
                        index = 10000000
    index = 0
    list2 = []
    if all_no.find('<b class="grey" ',0)>-1:
            while index < indexen:
                index = all_no.find('<b class="grey" ',index+1)
                if index < indexen:
                    if index > indexs:
                        list2.append(index)
                if index == -1:
                        index = 10000000
    listn = []
    comm= 0
    index = all_no.find('<span> Committed <span>',0)
    indexe = all_no.find('<span> Enrolled <span>',0)
    indexsign = all_no.find('<span> Signed <span>',0)
    if index >-1:
        comm = 1
    if indexe >-1:
        comm=1
    if indexsign > -1:
        comm=1
    if comm ==1:
            if plist != []:
                    plist.remove(plist[0])
    n1 = 0
    n2 = 0
    for ii in range(0,len(list1)+len(list2)):
        if n1 < len(list1):
            if n2 < len(list2):
                if list1[n1]<list2[n2]:
                    listn.append(0)
                    n1 = n1+1
                else:
                    listn.append(1)
                    n2=n2+1
            else:
                listn.append(0)
                n1=n1+1
        else:
            listn.append(1)
            n2=n2+1
    index = 0
    if len(listn)>len(plist):
            print "prob129", listn, plist
    for i in range(0,len(listn)):
        plist[i].append(listn[i])
    for i in range(len(listn),len(plist)):
        plist[i].append(0)
    if comm == 0:
        plist = []
    return plist

def getreclist2(playerid,instid):
    plist = []
    driver1 = webdriver.Firefox()
    driver1.implicitly_wait(30)
    b_url = "http://247sports.com/Player/"+str(int(playerid))+str(instid)
    driver1.get(b_url)
    all_links = driver1.find_elements_by_tag_name("a")
    plisti = getfrontteam(all_links,driver1.page_source)
    for ii in all_links:
        yt = ii.get_attribute("href")
        if yt is not None:
            index = yt.find("/Recruitment/",0)
            if index != -1:
                index2 = 0
                while index2 > -1:
                    index2 = yt.find("-",index2+1)
                    if index2>-1:
                        inds = index2
                ytt = ""
                indexend = yt.find("/",inds)
                for iii in range(inds+1,indexend):
                    ytt=ytt+yt[iii]
                try:
                    pid = int(ytt)
                    if pid not in plist:
                        plist.append(pid)
                        break
                except:
                    donot = 0
    driver1.close()
    tret = [plisti,plist]
    return tret

def getreclist(driver,linkurl,allsl):
    burl = ""
    for i in linkurl:
        burl=burl+i
    plist = []
    driver.get(burl)
    getcollegetable = driver.find_element_by_id("college_choices")

    getschools = getcollegetable.find_elements_by_tag_name("tr")
    schoollink= [burl,str(theyear)]

    for ii in getschools[1:]:
            

            trow = ii.find_elements_by_tag_name("td")

            yt = trow[0].text
            toffer = trow[2].get_attribute("innerHTML")
            if len(toffer) > 1:
                    
                    indexcd = trow[1].text.find('Committed',0)
                    
                    indexcds = trow[1].text.find('(',indexcd)
                    indexcde = trow[1].text.find(')',indexcds)
                    if indexcd > -1:
                            if indexcds > -1:
                                    if indexcde > -1:
                                            ytt=""
                                            for iytt in range(indexcds+1,indexcde):
                                                    ytt=ytt+trow[1].text[iytt]
                                            schoollink.append(ytt)
                                    else:
                                            schoollink.append("03/01/"+str(theyear))
                            else:
                                    schoollink.append("03/01/"+str(theyear))
                            schoollink.append(yt)
            else:
                    index = trow[1].text.find('Committed',0)
                    if index > -1:
                            indexcd = trow[1].text.find('Committed',0)
                    
                            indexcds = trow[1].text.find('(',indexcd)
                            indexcde = trow[1].text.find(')',indexcds)
                            if indexcd > -1:
                                    if indexcds > -1:
                                            if indexcde > -1:
                                                    ytt=""
                                                    for iytt in range(indexcds+1,indexcde):
                                                            ytt=ytt+trow[1].text[iytt]
                                                    schoollink.append(ytt)
                                            else:
                                                    schoollink.append("03/01/"+str(theyear))
                                    else:
                                            schoollink.append("03/01/"+str(theyear))
                            else:
                                    schoollink.append("03/01/"+str(theyear))
                            schoollink.append(yt)
                    else:
                            index = trow[1].text.find('Enrolled',0)
                            if index > -1:
                                    indexcd = trow[1].text.find('Enrolled',0)
                                    indexcds = trow[1].text.find('(',indexcd)
                                    indexcde = trow[1].text.find(')',indexcds)
                                    if indexcd > -1:
                                            if indexcds > -1:
                                                    if indexcde > -1:
                                                            ytt=""
                                                            for iytt in range(indexcds+1,indexcde):
                                                                    ytt=ytt+trow[1].text[iytt]
                                                            schoollink.append(ytt)
                                                    else:
                                                            schoollink.append("03/01/"+str(theyear))
                                            else:
                                                    schoollink.append("03/01/"+str(theyear))
                                    else:
                                            schoollink.append("03/01/"+str(theyear))
                                    schoollink.append(yt)

    for ii in getschools[1:]:
            trow = ii.find_elements_by_tag_name("td")
            yt = trow[0].text
            toffer = trow[2].get_attribute("innerHTML")
            if len(toffer) > 1:
                    indexcd = trow[1].text.find('Committed',0)
                    
                    indexcds = trow[1].text.find('(',indexcd)
                    indexcde = trow[1].text.find(')',indexcds)
                    if indexcd == -1:
                            schoollink.append(yt)
                            
                    
            
    allsl.append(schoollink)

    return allsl
    #print schoollink


#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.download.folderList",2)
#firefox_profile.set_preference("permissions.default.stylesheet",2)
#firefox_profile.set_preference("permissions.default.image",2)
#firefox_profile.set_preference("javascript.enabled", False)

driver = webdriver.Chrome("C:\Python27\Chrome\chromedriver")
allplayers = getplayerlist(driver,0)
writecsv(allplayers,"allplayers2016act"+str(theyear)+".csv")
#allplayers = ["https://n.rivals.com/content/prospects/maple/138337"]
print len(allplayers)
def runthis(driver,ii):
        allsl = []
        iii = 0
        lx =len(allplayers)
        for i in allplayers[(lx/5+1)*ii:(lx/5+1)*(1+ii)]:
                #allsl = getreclist(driver,i,allsl)
                try:
                        allsl = getreclist(driver,i,allsl)
                except:
                        pass
                print iii, ii
                iii=iii+1
                writecsv(allsl,"allrecs"+str(theyear)+str(ii)+".csv")
        driver.close()
for ii in range(0,1):
        driver = []
        t = []
        for i in range(0,5):
                t.append(0)
                #firefox_profile = webdriver.FirefoxProfile()
                #firefox_profile.set_preference("browser.download.folderList",2)
                #firefox_profile.set_preference("permissions.default.stylesheet",2)
                #firefox_profile.set_preference("permissions.default.image",2)
                #firefox_profile.set_preference("javascript.enabled", False)
                driver.append(webdriver.Chrome("C:\Python27\Chrome\chromedriver"))
                driver[i].implicitly_wait(30)
                t[i] = Thread(target=runthis,args=(driver[i],i))
                t[i].start()
                print "TAC=", threading.active_count()
                print "started", i


