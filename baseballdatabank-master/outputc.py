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
        nrows = 50
        for i in range(0,nrows):
                top100.append(0)
                top100data.append({'year':2017,'team':'','answer':'','points':6,'number':0})
        cat_name = 'most-'
        cat_stat = ''
        if cat_id==9:
                cat_stat = 'war'
        if cat_id==14:
                cat_stat = 'wins'
        if cat_id==17:
                cat_stat = 'saves'
        if cat_id==23:
                cat_stat = 'strikeouts'

        cat_name += cat_stat+'-'
        if cat_year_end != 0:
                cat_name += cat_type+'-between-'+str(cat_year)+'-and-'+str(cat_year_end)
                question_str = "What pitchers have the most "+str(cat_stat)+" in one season between "+str(cat_year)+' and '+str(cat_year_end)+"?"
        else:
                cat_name += cat_type+'-since-'
                cat_name += str(cat_year)
                cat_year_end = 2999
                question_str = "What pitchers have the most "+str(cat_stat)+" in one season since "+str(cat_year)+"?"

        other_stats = ['wins','war','saves','strikeouts']
        other_stats.remove(cat_stat)
        suggested_str = '"'
        for i in other_stats:
                suggested_str += "<a href='"+cat_name.replace(cat_stat,i)+".html'>"+question_str.replace(cat_stat,i)+'</a> '
        suggested_str += '" '



        for i in range(0,len(year_index)):
                year_index[i]=int(year_index[i])
        allpitchers = []
        for i in range(cat_year,cat_year_end+1):
                sindex = sum(year_index[:i-1])
                allpitchers = allpitchers+allpitcherraw[sindex:sindex+50]
        for i in allpitchers:
                if int(i[18])>29 and int(i[11])>=cat_year and int(i[11])<=cat_year_end:
                        for ii in range(0,nrows):
                                if float(i[cat_id])>top100[ii]:
                                        for iii in range(0,nrows-1-ii):
                                                top100[nrows-1-iii]=top100[nrows-1-iii-1]
                                                top100data[nrows-1-iii]['year']=top100data[nrows-1-iii-1]['year']
                                                top100data[nrows-1-iii]['answer']=top100data[nrows-1-iii-1]['answer']
                                                top100data[nrows-1-iii]['team']=top100data[nrows-1-iii-1]['team']
                                                top100data[nrows-1-iii]['number']=top100data[nrows-1-iii-1]['number']
                                        top100[ii]=float(i[cat_id])
                                        top100data[ii]['year']=int(i[11])
                                        top100data[ii]['team']=i[12]
                                        top100data[ii]['number']=float(i[cat_id])
                                        top100data[ii]['answer']=i[7].replace("'","\\'")
                                        break

        istr = 'var dataArray = ['
        for i in range(0,nrows):
                istr += json.dumps(top100data[i])+','
        allistr += ' "'+istr[:-1].replace('"',"'")+'];" '
        allcstr += ' "'+cat_name+'"'
        allqstr += ' "'+question_str+'"'   
        allsstr += suggested_str 
        return allistr,allcstr,allqstr,allsstr
print time.time(),
cat_id = int(sys.argv[1])
cat_year = int(sys.argv[3])
cat_type = sys.argv[2]
allistr = ''
allcstr = ''
allqstr = ''
allsstr = ''
allpitcherraw = readcsv('allpitchdata'+str(cat_id)+'.csv')[1:]
year_index = readcsv('allpitchdata'+str(cat_id)+'.csv')[0]
for i in range(cat_year,2017):
        allistr,allcstr,allqstr,allsstr = toendyear(i,allistr,allcstr,allqstr,allsstr,cat_id,cat_year,cat_type,allpitcherraw,year_index)
allistr,allcstr,allqstr,allsstr = toendyear(0,allistr,allcstr,allqstr,allsstr,cat_id,cat_year,cat_type,allpitcherraw,year_index)
f = open('datadata.txt','w')
f.write(allistr)
f.close()

f = open('namedata.txt','w')
f.write(allcstr)
f.close()

f = open('questiondata.txt','w')
f.write(allqstr)
f.close()

f = open('suggesteddata.txt','w')
f.write(allsstr)
f.close()
print time.time()
