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



def sortdata(year_id,minab=0):
        
        all_stats = []
        stat_cats = [['WAR',10],['HR',20],['R',16],['H',17],['RBI',21],['SB',22],['BB',24],['SO',25]]
        for scat in stat_cats:
                col_id = scat[1]
                allbatters = readcsv('../../baseballdatabank-master/allbattingdata.csv')
                sorted = False
                icount = 0
                yearbatters = []
                for idx,i in enumerate(allbatters):
                        if int(allbatters[idx][15])<=minab:
                                allbatters[idx][col_id] /= 100
                        if int(i[12])==year_id:
                                yearbatters.append(i)
                while not sorted:
                        sorted = True
                        icount += 1
                        if icount %100==0:
                                print icount
                        for idx,i in enumerate(yearbatters[:-1]):
                                
                                if yearbatters[idx][col_id]=='NULL':
                                        yearbatters[idx][col_id]=0
                                if yearbatters[idx+1][col_id]=='NULL':
                                        yearbatters[idx+1][col_id]=0
                                if float(yearbatters[idx][col_id])<float(yearbatters[idx+1][col_id]) or (float(yearbatters[idx][col_id])==float(yearbatters[idx+1][col_id]) and str(yearbatters[idx][0])>str(yearbatters[idx+1][0])):
                                        hold_row = yearbatters[idx+1]
                                        yearbatters[idx+1]=yearbatters[idx]
                                        yearbatters[idx]=hold_row
                                        if icount < 2000:
                                                sorted = False
                stat_year = [scat[0]]
                for i in yearbatters[:10]:
                        stat_year.append(i[8])
                all_stats.append(stat_year)
        writenewcsv(all_stats,'top10batting'+str(year_id)+'.csv')
#combinedata()


sortdata(2016,-1)
