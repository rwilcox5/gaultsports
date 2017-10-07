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



#combine()
#print stopit


#allplayers = []
#try:
#    with open('allplayers'+str(theyear)+'.csv', 'rb') as csvfile:
#        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#        for row in spamreader:
#            allplayers.append(row)
#except:
#    pass


##This gets all the owners from the conferences to check if sims or not.

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
        print len(allbtn)
        for ii in allbtn:
                if ii.text=='Next':
                        try:
                                ii.click()
                                time.sleep(3)
                                print i, len(ap)
                        except:
                                pass


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


    #The losing schools
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

driver = webdriver.Chrome()
allplayers = getplayerlist(driver)
writecsvstr(allplayers,basefile+str(theyear)+str(nstars)+".csv")
print stopit
#allplayers = ["https://n.rivals.com/content/prospects/maple/138337"]
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
try:
        playersdone = readcsva("allplayers2016act"+str(theyear)+"done.csv")
except:
        playersdone = []
allplayersa = readcsva("allplayers2016act"+str(theyear)+".csv")
allplayers = []
print allplayersa[:3]
print playersdone[:3]
for i in allplayersa:
        if i not in playersdone:
                allplayers.append(i)
print len(allplayers)

#print stopit
def runthis(driver,ii,adone,allsl):
        iii = 0
        lx =len(allplayers)
        lx = 1000
        nerror = 0
        nodone = 0
        for i in allplayers[(lx/5+1)*ii:(lx/5+1)*(1+ii)]:
                #allsl = getreclist(driver,i,allsl)
                if i not in adone:
                        try:
                                allsl = getreclist(driver,i,[])
                                adone = [[i,"Y"]]
                                writecsva(allsl,"allrecs"+str(theyear)+str(ii)+".csv")
                                writecsva(adone,"allplayers2016act"+str(theyear)+"done.csv")
                        except:
                                nodone = 1
                                break
                        iii=iii+1
                        
        print ii, "DONE", nodone
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
                options = webdriver.ChromeOptions() 

                driver.append(webdriver.Chrome(chrome_options=options))
                driver[i].implicitly_wait(30)
                t[i] = Thread(target=runthis,args=(driver[i],i,[],[]))
                t[i].start()
                print "TAC=", threading.active_count()
                print "started", i


