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

        allbatters = readcsv('core/Seasons_Stats.csv')[1:]

        print len(allbatters)
        allyears = []

        for idx,i in enumerate(allbatters):
                try:

                        yeardata = []

                        yeardata.append(int(i[1]))
                        yeardata.append(i[2])
                        yeardata.append(i[3])
                        yeardata.append(int(i[4]))
                        yeardata.append(i[5])
                        yeardata.append(int(i[6]))
                        yeardata.append(float(i[22]))
                        yeardata.append(float(i[23]))
                        yeardata.append(float(i[24]))
                        yeardata.append(int(i[52]))

                        if len(yeardata)!=10:
                                print 'BAD', yeardata
                        else:
                                writecsv([yeardata],'alldata.csv')
                except:
                        pass


def sortdata(col_id,minab=0):
        allbatters = readcsv('alldata.csv')
        sorted = False
        icount = 0
        year_index = []
        for idx,i in enumerate(allbatters):
                try:
                        if int(allbatters[idx][5])<=minab:
                                allbatters[idx][col_id] /= 100
                except:
                        pass
        while not sorted:
                year_index = []
                for i in range(0,3000):
                        year_index.append(0)
                sorted = True
                icount += 1
                if icount %100==0:
                        print icount
                for idx,i in enumerate(allbatters[:-1]):
                        year_index[int(i[0])]+=1
                        if allbatters[idx][col_id]=='NULL':
                                allbatters[idx][col_id]=0
                        if allbatters[idx+1][col_id]=='NULL':
                                allbatters[idx+1][col_id]=0
                        if int(allbatters[idx][0])>int(allbatters[idx+1][0]) or (float(allbatters[idx][col_id])<float(allbatters[idx+1][col_id]) and int(allbatters[idx][0])==int(allbatters[idx+1][0])) :
                                hold_row = allbatters[idx+1]
                                allbatters[idx+1]=allbatters[idx]
                                allbatters[idx]=hold_row
                                if icount < 2000:
                                        sorted = False
        writenewcsv([year_index]+allbatters,'alldata'+str(col_id)+'.csv')
combinedata()


sortdata(9,500)










