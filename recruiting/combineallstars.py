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

theyear = int(sys.argv[1])
basefile = sys.argv[2]

def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                if parr[i][0]!='""':
                                    spamwriter.writerow([parr[i][0],parr[i][1]])
                        except:
                                print parr[i], i

def combine():
        allrecs = []
        for ii in range(1,6):
            starrecs = []
            with open(basefile+str(theyear)+str(ii)+'.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    starrecs.append(row)
            for i in starrecs:
                i.append(ii)
            allrecs=allrecs+starrecs
        writecsv(allrecs,basefile+str(theyear)+".csv")



combine()

