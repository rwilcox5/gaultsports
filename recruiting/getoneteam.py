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
team = str(sys.argv[1])

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



allplayersa = readcsv("football2018done.csv")
for i in allplayersa:
    if i[3]==team:
        print i[0]
