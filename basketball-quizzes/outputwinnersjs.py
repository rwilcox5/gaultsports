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
        name_stat = ''

        if cat_id==9:
                cat_stat = 'points'
                name_stat = 'Points'

        cat_name += cat_stat+'-season-'+str(cat_year/20+50)+str(cat_year_end/20+50)

        question_str = "What players have the most "+str(name_stat)+" in one season "


        other_stats = ['points','rebounds']

        other_stats.remove(cat_stat)
        suggested_str = '"'
        for i in other_stats:
                suggested_str += "<a href='"+cat_name.replace(cat_stat,i)+".html'>"+question_str.replace(name_stat,i)+'</a> '
        suggested_str += '" '



        if cat_year_end-cat_year<50:

                for i in range(0,len(year_index)):
                        year_index[i]=int(year_index[i])
                allpitchers = []
                for i in range(cat_year,cat_year_end+1):
                        sindex = sum(year_index[:i-1])
                        allpitchers = allpitchers+allpitcherraw[sindex:sindex+nrows]
                istr = 'var rawDataArray = ['

                for i in allpitchers:
                        istr += "'"+i[1].replace("'","\\'")+"','"+i[4]+"',"+str(i[0])+","+str(float(i[cat_id]))+","

                allistr += ' "'+istr[:-1]+'];" '
                allcstr += ' "'+cat_name+'"'
                allqstr += ' "'+question_str+'"'   
                allsstr += suggested_str 
                return allistr,allcstr,allqstr,allsstr
        else:

                for i in range(0,len(year_index)):
                        year_index[i]=int(year_index[i])
                allpitchers = []
                for i in range(cat_year,cat_year_end+1):
                        sindex = sum(year_index[:i-1])
                        allpitchers = allpitchers+allpitcherraw[sindex:sindex+nrows]
                istr = 'var rawDataArray = ['

                for i in allpitchers:
                        if int(i[5])>9 and int(i[0])>=cat_year+21 and int(i[0])<=cat_year_end-21:
                                for ii in range(0,nrows):
                                        if float(i[cat_id])>top100[ii]:
                                                for iii in range(0,nrows-1-ii):
                                                        top100[nrows-1-iii]=top100[nrows-1-iii-1]
                                                        top100data[nrows-1-iii]['year']=top100data[nrows-1-iii-1]['year']
                                                        top100data[nrows-1-iii]['answer']=top100data[nrows-1-iii-1]['answer']
                                                        top100data[nrows-1-iii]['team']=top100data[nrows-1-iii-1]['team']
                                                        top100data[nrows-1-iii]['number']=top100data[nrows-1-iii-1]['number']
                                                top100[ii]=float(i[cat_id])
                                                top100data[ii]['year']=int(i[0])
                                                top100data[ii]['team']=i[4]
                                                top100data[ii]['number']=float(i[cat_id])
                                                top100data[ii]['answer']=i[1].replace("'","\\'")
                                                break
        
                for i in allpitchers:
                        if float(i[cat_id])>=top100[nrows-1]:
                                istr += "'"+i[1].replace("'","\\'")+"','"+i[4]+"',"+str(i[0])+","+str(float(i[cat_id]))+","


                allistr += ' "'+istr[:-1]+'];" '
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

allpitcherraw = readcsv('alldata'+str(cat_id)+'.csv')[1:]
year_index = readcsv('alldata'+str(cat_id)+'.csv')[0]

for i in range((cat_year+20)/20,2017/20+2):
        allistr,allcstr,allqstr,allsstr = toendyear(i*20,allistr,allcstr,allqstr,allsstr,cat_id,cat_year,cat_type,allpitcherraw,year_index)

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
