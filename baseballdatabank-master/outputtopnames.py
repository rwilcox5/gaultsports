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



def toendyear(cat_year_end,allistr,allcstr,allqstr,allsstr,cat_id,cat_year,cat_type,pitcherraw,year_index,cat_borp):
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
        if cat_borp=='p':
                for i in allpitchers:
                        if i[7] not in allnames:
                                allnames.append(i[7])
        else:
                for i in allpitchers:
                        if i[8] not in allnames:
                                allnames.append(i[8])
        for i in allnames:
                istr += ' "'+i+'",'
        allistr += istr[:-1]+']; '
        allistr += '\nvar npitchers = '+str(len(allnames))+';'
        return allistr,allcstr,allqstr,allsstr
print time.time(),
cat_id = int(sys.argv[1])
cat_type = sys.argv[2]
cat_borp = sys.argv[3]
allistr = ''
allcstr = ''
allqstr = ''
allsstr = ''
if cat_borp == 'p':
        allpitcherraw = readcsv('allpitchdata'+str(cat_id)+'.csv')[1:]
        year_index = readcsv('allpitchdata'+str(cat_id)+'.csv')[0]
else:
        allpitcherraw = readcsv('allbattingdata'+str(cat_id)+'.csv')[1:]
        year_index = readcsv('allbattingdata'+str(cat_id)+'.csv')[0]   
allistr,allcstr,allqstr,allsstr = toendyear(2999,allistr,allcstr,allqstr,allsstr,cat_id,1900,cat_type,allpitcherraw,year_index,cat_borp)
f = open('namedata.txt','w')
if cat_borp == 'p':
        f.write(allistr+'\nvar stat_id = "pitcher-'+str(cat_id)+'";')
else:
        f.write(allistr+'\nvar stat_id = "batter-'+str(cat_id)+'";')
f.close()


print time.time()
