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
def writenewcsv(parr, filen):
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

def combinedata():

        allpitchers = readcsv('core/Pitching.csv')[1:]
        allnames = readcsv('core/People.csv')[1:]
        allwar = readcsv('core/war_daily_pitch.txt')[1:]

        allpid = []
        for i in allpitchers:
                if i[0] not in allpid:
                        allpid.append(i[0])
        allbbref = []
        for i in allpid:
                for ii in allnames:
                        if ii[0]==i:
                                allbbref.append([ii[23],ii[4],ii[5],ii[16],ii[17],ii[19],ii[20]])
                                break
        print len(allpid)
        print len(allbbref)
        print len(allpitchers)
        allyears = []

        for idx,i in enumerate(allpitchers):

                if int(i[1])>=1900:
                        pid = i[0]
                        year = i[1]
                        stint = i[2]
                        yeardata = []
                        for iidx,ii in enumerate(allpid):
                                if ii==pid:
                                        yeardata.append(allbbref[iidx][0])
                                        yeardata.append(allbbref[iidx][1])
                                        yeardata.append(allbbref[iidx][2])
                                        yeardata.append(allbbref[iidx][3])
                                        yeardata.append(allbbref[iidx][4])
                                        yeardata.append(allbbref[iidx][5])
                                        yeardata.append(allbbref[iidx][6])
                                        break
                        for ii in allwar:
                                if ii[3]==yeardata[0] and ii[4]==year and ii[6]==stint:
                                        yeardata.append(ii[0])
                                        yeardata.append(ii[1])
                                        yeardata.append(ii[28])
                                        yeardata.append(ii[39])
                                        break
                        yeardata.append(i[1])
                        yeardata.append(i[3])
                        yeardata.append(i[4])
                        yeardata.append(i[5])
                        yeardata.append(i[9])
                        yeardata.append(i[10])
                        yeardata.append(i[11])
                        yeardata.append(i[12])
                        yeardata.append(i[13])
                        yeardata.append(i[14])
                        yeardata.append(i[15])
                        yeardata.append(i[16])
                        yeardata.append(i[17])
                        yeardata.append(i[26])

                        if len(yeardata)!=25:
                                print 'BAD', yeardata
                        else:
                                writecsv([yeardata],'allpitchdata.csv')
                        if idx%100==0:
                                print idx,

def sortdata(col_id):
        allpitchers = readcsv('allpitchdata.csv')
        sorted = False
        icount = 0
        year_index = []
        while not sorted:
                year_index = []
                for i in range(0,3000):
                        year_index.append(0)
                sorted = True
                icount += 1
                if icount %100==0:
                        print icount
                for idx,i in enumerate(allpitchers[:-1]):
                        year_index[int(i[11])]+=1
                        if allpitchers[idx][col_id]=='NULL':
                                allpitchers[idx][col_id]=0
                        if allpitchers[idx+1][col_id]=='NULL':
                                allpitchers[idx+1][col_id]=0
                        if int(allpitchers[idx][11])>int(allpitchers[idx+1][11]) or (float(allpitchers[idx][col_id])<float(allpitchers[idx+1][col_id]) and int(allpitchers[idx][11])==int(allpitchers[idx+1][11])) :
                                hold_row = allpitchers[idx+1]
                                allpitchers[idx+1]=allpitchers[idx]
                                allpitchers[idx]=hold_row
                                if icount < 1000:
                                        sorted = False
        writenewcsv([year_index]+allpitchers,'allpitchdata'+str(col_id)+'.csv')
sortdata(9)
sortdata(17)
sortdata(23)










