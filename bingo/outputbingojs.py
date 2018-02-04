import time
import sys
import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select

pagen = 10
theyear = sys.argv[1]
basefile = sys.argv[2]



def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i

def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

allgames = readcsv('nbaschedule.csv')

teamevents = [['>=110 Points',2],['<90 Points',2],['>=120 Points',1],['<80 Points',2],['>=20 Pt Margin',1],['>=10 Steals',1],['>=10 Blocks',1],['>=5 Pt Upset',1],['Overtime',1],['Buzzer Beater',1],['4th Q Comeback',1],['>=17 3 Pointers',1]]
indevents = [['>=40 Points',2],['>=20 Rebounds',2],['>=15 Assists',2],['Triple Double',2],['>=5 3 Pointers',2],['',2]]

istr = 'recruits = {'
teams = []
for i in allrecruits:
    notin = True
    if len(i)>4:
        for iidx,ii in enumerate(teams):
            if i[4].lower().replace(' ','-')==ii[0]:
                losers = []
                value = 0
                for iii in allrecdata:
                    if iii[0]==i[0]:
                        losers = iii[4:min(7,len(iii)-1)]
                        value = iii[1]

                if len(losers)>0:
                    teams[iidx][1].append(i[:4]+[value]+losers)
                else:
                    teams[iidx][1].append(i[:4]+[0]+losers)
                notin = False
        if notin:
            losers = []
            value = 0
            for iii in allrecdata:
                if iii[0]==i[0]:
                    losers = iii[4:min(7,len(iii)-1)]
                    value = iii[1]

            if len(losers)>0:
                teams.append([i[4].lower().replace(' ','-'),[i[:4]+[value]+losers]])
            else:
                teams.append([i[4].lower().replace(' ','-'),[i[:4]+[0]+losers]])
            
    else:
        print i
for i in teams:
    istr += '"'+i[0]+'":['
    for ii in i[1]:
        istr += '["'+ii[0]+'","'+ii[1]+'","'+ii[2]+'","'+ii[3]+'",'+str(ii[4])
        for iii in ii[5:]:
            istr += ',"'+iii+'"'

        istr+='],'

    istr = istr[:-1]+'],'
istr = istr[:-1]+'};'


f = open('hello_recruits.txt','w')
f.write(istr+'\n')
f.close()