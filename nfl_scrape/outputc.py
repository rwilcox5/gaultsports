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

year = int(sys.argv[1])


def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

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


teamdata = readcsv("nflg.csv")

teams = []
teamstats = []
for idx,i in enumerate(teamdata):
    teamname = str(i[0])

    if teamname not in teams:
        teams.append(teamname)
        tstats = []
        for ii in i[1:]:
            tstats.append(int(ii))
        teamstats.append(tstats)
    else:
        for iidx,ii in enumerate(teams):
            if ii==teamname:
                teamid = iidx
        tstats = []
        for ii in i[1:]:
            tstats.append(int(ii))
        teamstats[teamid]+=tstats

istr = 'int teamdata[] = {'
tstr = 'int teams[] = {0,'
runii = 0
for idx,i in enumerate(teamstats):
    for ii in i:
        istr += str(ii)+','
        runii+=1
    tstr +=str(runii)+','
istr = istr[:-1]+'};'
tstr = tstr[:-1]+'};'
testr = 'int teamelo[] = {'
for i in range(0,32*6):
    testr += str(1500)+','
testr = testr[:-1]+'};'
f = open('helloworld.txt','w')
f.write(istr+'\n'+tstr+'\n'+testr)
f.close()

for i in range(0,801):
    print math.trunc(1./(1.+10.**(i/400.))*10000)/10000., ",",


