import time
import random
import csv
import math
import threading
import json
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


def writecsv(parr, filen):
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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa


allpitchers = readcsv('core/Pitching.csv')[1:]
allbatters = readcsv('core/Batting.csv')[1:]
allnames = readcsv('core/People.csv')[1:]

istr = 'var pitcher_names = ['
allpids = []
for i in allpitchers:
        if int(i[12])>29 and int(i[1])>1899:
                if i[0] not in allpids:
                        allpids.append(i[0])
npitchers = 0
for pid in allpids:
        for ii in range(0,len(allnames)):
                if allnames[ii][0]==pid:
                        istr += '"'+allnames[ii][13]+' '+allnames[ii][14]+'",'
                        allnames.pop(ii)
                        npitchers += 1
                        break


f = open('helloworld.txt','w')
f.write(istr[:-1]+'];\nvar npitchers = '+str(npitchers)+';\n')
f.close()