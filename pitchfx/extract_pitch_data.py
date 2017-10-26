import time
import random
import csv
import math
import threading
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

allpitchdata = readcsv('pitch_table.csv')[1:]

allpitches = []
istr = 'int allpitches[] = {'
abstr = 'int allabs[] = {'
nabs = 0
for idx,i in enumerate(allpitchdata):
        allpitches.append([i[57],i[32],i[37],i[43],i[44],i[39],i[40]])
        if i[57] in ['FA','FF','FT','FC','FS','SI','SF']:
                ptype = 1
        elif i[57] in ['CU','KC','CB']:
                ptype = 2
        elif i[57]=='SL':
                ptype = 3
        elif i[57]=='CH':
                ptype = 4
        else:
                ptype = 5
        if i[32] in ['F','S','X']:
                swing = 1
        else:
                swing = 0
        if i[32] in ['B']:
                strike = 0
        else:
                strike = 1
        xcoord = 60/(1.416)*(float(i[43])+.708)+20.
        if xcoord<0:
                xcoord = 0
        elif xcoord>100:
                xcoord = 100
        else:
                xcoord = int(xcoord)
        szh = float(i[39])-float(i[40])
        ycoord = 60./szh*(float(i[44])-float(i[40]))+20.
        if ycoord<0:
                ycoord = 0
        elif ycoord>100:
                ycoord = 100
        else:
                ycoord = int(ycoord)
        ycoord=100-ycoord

        istr+= str(ptype*100+strike*10+swing)+','+str(xcoord)+','+str(ycoord)+','
        if idx > 0:
                if i[31]!=allpitchdata[idx-1][31]:
                        abstr += str(idx)+','+i[18]+','+i[19]+','
                        nabs+=1
        else:
                abstr += str(0)+','+i[18]+','+i[19]+','
                nabs+=1

istr = istr[:-1]+'};'
abstr += str(len(allpitchdata))+',0,0};'

writecsv(allpitches,'my_pitch_data.csv')

f = open('helloworld.txt','w')
f.write(istr+'\n'+abstr+'\n'+'int nabs = '+str(nabs)+';')
f.close()