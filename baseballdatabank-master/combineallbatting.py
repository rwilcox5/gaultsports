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

        allbatters = readcsv('core/Batting.csv')[1:]
        allnames = readcsv('core/People.csv')[1:]
        allwar = readcsv('core/war_daily_bat.txt')[1:]

        allpid = []
        for i in allbatters:
                if i[0] not in allpid:
                        allpid.append(i[0])
        allbbref = []
        for i in allpid:
                for ii in allnames:
                        if ii[0]==i:
                                allbbref.append([ii[23],ii[4],ii[5],ii[16],ii[17],ii[18],ii[19],ii[20]])
                                break
        print len(allpid)
        print len(allbbref)
        print len(allbatters)
        allyears = []

        for idx,i in enumerate(allbatters):

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
                                        yeardata.append(allbbref[iidx][7])
                                        break
                        for ii in allwar:
                                if ii[3]==yeardata[0] and ii[4]==year and ii[6]==stint:
                                        yeardata.append(ii[0])
                                        yeardata.append(ii[1])
                                        yeardata.append(ii[30])
                                        yeardata.append(ii[46])
                                        break
                        yeardata.append(i[1])
                        yeardata.append(i[3])
                        yeardata.append(i[4])
                        yeardata.append(i[6])
                        yeardata.append(i[7])
                        yeardata.append(i[8])
                        yeardata.append(i[9])
                        yeardata.append(i[10])
                        yeardata.append(i[11])
                        yeardata.append(i[12])
                        yeardata.append(i[13])
                        yeardata.append(i[14])
                        yeardata.append(i[15])
                        yeardata.append(i[16])

                        if len(yeardata)!=26:
                                print 'BAD', yeardata
                        else:
                                writecsv([yeardata],'allbattingdata.csv')
                        if idx%100==0:
                                print idx,

def sortdata(col_id,minab=0):
        allbatters = readcsv('allbattingdata.csv')
        sorted = False
        icount = 0
        year_index = []
        for idx,i in enumerate(allbatters[:-1]):
                if int(allbatters[idx][15])<=minab:
                        allbatters[idx][col_id] /= 100
        while not sorted:
                year_index = []
                for i in range(0,3000):
                        year_index.append(0)
                sorted = True
                icount += 1
                if icount %100==0:
                        print icount
                for idx,i in enumerate(allbatters[:-1]):
                        year_index[int(i[12])]+=1
                        if allbatters[idx][col_id]=='NULL':
                                allbatters[idx][col_id]=0
                        if allbatters[idx+1][col_id]=='NULL':
                                allbatters[idx+1][col_id]=0
                        if int(allbatters[idx][12])>int(allbatters[idx+1][12]) or (float(allbatters[idx][col_id])<float(allbatters[idx+1][col_id]) and int(allbatters[idx][12])==int(allbatters[idx+1][12])) :
                                hold_row = allbatters[idx+1]
                                allbatters[idx+1]=allbatters[idx]
                                allbatters[idx]=hold_row
                                if icount < 2000:
                                        sorted = False
        writenewcsv([year_index]+allbatters,'allbattingdata'+str(col_id)+'.csv')
#combinedata()


sortdata(11,500)










