import time
import random
import csv
import math
import threading
from threading import Thread

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

alldata = readcsv('2017-18.csv')
teamstr = 'allteams = ['
teams = []
for i in alldata:
        if i[0] not in teams:
                teams.append(i[0])
                teamstr += '"'+i[0]+'",'
        else:
                print 'duplicate team', i[0]
                print soto
pstr = 'allplayed = ['
tstr = 'alltoplay = ['
for i in range(0,len(alldata)):

        pstr += '['+str(i)+','
        myteam = i
        for ii in range(0,len(alldata[i])/3):
                if len(alldata[i][ii*3+3])>0:
                        for iiidx,iii in enumerate(teams):
                                if iii==alldata[i][ii*3+2]:
                                        pstr += '"'+alldata[i][ii*3+1]+'",'
                                        pstr += str(iiidx)+','
                                        if alldata[i][ii*3+3].find('W')>-1:
                                                pstr +=str(alldata[i][ii*3+3][alldata[i][ii*3+3].find(' ')+1:alldata[i][ii*3+3].find('-')])+','+str(alldata[i][ii*3+3][alldata[i][ii*3+3].find('-')+1:])+','
                                        else:
                                                pstr +=str(alldata[i][ii*3+3][alldata[i][ii*3+3].find('-')+1:])+','+str(alldata[i][ii*3+3][alldata[i][ii*3+3].find(' ')+1:alldata[i][ii*3+3].find('-')])+','
                else:
                        for iiidx,iii in enumerate(teams):
                                if iii==alldata[i][ii*3+2]:
                                        if alldata[i][ii*3+1]=='':
                                                tstr += str(iiidx)+','
                                                tstr += str(myteam)+','
                                        elif alldata[i][ii*3+1]=='vs.':
                                                if myteam > iiidx:
                                                        tstr += str(10000+iiidx)+','
                                                        tstr += str(10000+myteam)+','

        pstr = pstr[:-1]+ '],'
f = open('helloworld.txt','w')
f.write(pstr[:-1]+'];\n'+tstr[:-1]+'];\n'+teamstr[:-1]+'];\n')
f.close()
