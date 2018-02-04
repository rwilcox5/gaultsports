import time
import sys
import random
import csv
import math
import threading
from threading import Thread
import lxml
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from lxml.cssselect import CSSSelector
import requests
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




def getreclist(linkurl,allsl,pstars):
    burl = ""
    pdata = []
    for i in linkurl:
        burl=burl+i
    plist = []
    res = requests.get(burl)
    doc = html.fromstring(res.content)
    schoollink= [burl,str(theyear),pstars]
    allrows = doc.xpath('//*[@id="college_choices"]//tr')

    for i in range(1,len(allrows)+1):
            alltds = doc.xpath('//*[@id="college_choices"]/tbody/tr['+str(i)+']//td')
            if len(alltds)>1:

                yt = alltds[0].text_content().replace('\n','')
                index = alltds[1].text_content().find('Committed',0)
                if index > -1:
                        schoollink.append(yt)
                else:
                        index = alltds[1].text_content().find('Enrolled',0)
                        if index > -1:
                                schoollink.append(yt)
                        else:
                            index = alltds[1].text_content().find('Signed',0)
                            if index > -1:
                                    schoollink.append(yt)

    #The losing schools
    for i in range(1,len(allrows)+1):
            alltds = doc.xpath('//*[@id="college_choices"]/tbody/tr['+str(i)+']//td')
            if len(alltds)>2:
                yt = alltds[0].text_content().replace('\n','')
                toffer = alltds[2].find_class('checkmark-gray')
                if len(toffer) > 0:
                        indexc = alltds[1].text_content().find('Committed',0)
                        indexe = alltds[1].text_content().find('Enrolled',0)
                        indexs = alltds[1].text_content().find('Signed',0)
                        if indexc == -1 and indexe == -1 and indexs == -1:
                                schoollink.append(yt)
                            
    try:
        pdata.append(burl)
        profile_data = str(doc.xpath('//*[@id="articles"]')[0].get('ng-init'))

        index = profile_data.find('"hometown"')+12
        index2 = profile_data.find('",',index)
        pdata.append(profile_data[index:index2])

        index = profile_data.find('"full_name"')+13
        index2 = profile_data.find('",',index)
        pdata.append(profile_data[index:index2])

        index = profile_data.find('"position"')+12
        index2 = profile_data.find('",',index)
        pdata.append(profile_data[index:index2])
        if len(schoollink)>3:
            pdata.append(schoollink[3])
    except:
        pass

    allsl.append(schoollink)

    return allsl,pdata
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
allplayers = allplayersa
print len(allplayers)


def runthis(driver,ii):
        lx =len(allplayers)
        for iiii in allplayers[(lx/nthreads+1)*ii:min((lx/nthreads+1)*(1+ii),lx)]:
                i = iiii[0]
                try:
                        allsl,pdata = getreclist(i,[],iiii[1])
                        writecsva(allsl,basefile+str(theyear)+'done'+str(ii)+".csv")
                        writecsva([pdata],basefile+str(theyear)+'done'+str(ii)+"-profile.csv")
                except:
                        allsl,pdata = getreclist(i,[],iiii[1])
                        writecsva(allsl,basefile+str(theyear)+'done'+str(ii)+".csv")
                        writecsva([pdata],basefile+str(theyear)+'done'+str(ii)+"-profile.csv")
                        print 'BAD', i
                        break
                        
        print ii, "DONE"


driver = [0,0,0,0,0]
t = []

for i in range(0,nthreads):
        t.append(0)

        t[i] = Thread(target=runthis,args=(driver[i],i))
        t[i].start()
        print "TAC=", threading.active_count()
        print "started", i


