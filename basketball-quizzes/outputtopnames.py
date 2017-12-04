import time
import random
import sys
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



def toendyear(cat_year_end,allistr,allcstr,allqstr,allsstr,cat_id,cat_year,cat_type,pitcherraw,year_index):
        top100 = []
        top100data = []
        nrows = 100
        for i in range(0,len(year_index)):
                year_index[i]=int(year_index[i])
        allpitchers = []
        for ii in range(0,nrows):
                for i in range(cat_year,cat_year_end+1):
                        sindex = sum(year_index[:i-1])
                        allpitchers = allpitchers+allpitcherraw[sindex+ii:sindex+ii+1]
        istr = 'var pitcher_names = ['
        allnames = []

        for i in allpitchers:
                if i[1] not in allnames:
                        allnames.append(i[1])

        for i in allnames:
                istr += ' "'+i+'",'
        allistr += istr[:-1]+']; '
        allistr += '\nvar npitchers = '+str(len(allnames))+';'
        return allistr,allcstr,allqstr,allsstr
print time.time(),
cat_id = int(sys.argv[1])
cat_type = sys.argv[2]

allistr = ''
allcstr = ''
allqstr = ''
allsstr = ''

allpitcherraw = readcsv('alldata'+str(cat_id)+'.csv')[1:]
year_index = readcsv('alldata'+str(cat_id)+'.csv')[0]
allistr,allcstr,allqstr,allsstr = toendyear(2999,allistr,allcstr,allqstr,allsstr,cat_id,1950,cat_type,allpitcherraw,year_index)
f = open('namedata.txt','w')
f.write(allistr+'\nvar stat_id = "bball-'+str(cat_id)+'";')
f.close()


print time.time()
