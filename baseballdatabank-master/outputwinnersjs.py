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
        nrows = 50
        for i in range(0,nrows):
                top100.append(0)
                top100data.append({'year':2017,'team':'','answer':'','points':6,'number':0})
        cat_name = 'most-'
        cat_stat = ''
        name_stat = ''
        if cat_borp=='p':
                if cat_id==9:
                        cat_stat = 'war-pitcher'
                        name_stat = 'WAR'
                if cat_id==14:
                        cat_stat = 'wins'
                        name_stat = 'Wins'
                if cat_id==17:
                        cat_stat = 'saves'
                        name_stat = 'Saves'
                if cat_id==23:
                        cat_stat = 'strikeouts'
                        name_stat = 'Strikeouts'

        else:
                if cat_id==10:
                        cat_stat = 'war-batter'
                        name_stat = 'WAR'
                if cat_id==16:
                        cat_stat = 'runs'
                        name_stat = 'Runs'
                if cat_id==17:
                        cat_stat = 'hits'
                        name_stat = 'Hits'
                if cat_id==20:
                        cat_stat = 'home-runs'
                        name_stat = 'Home Runs'
                if cat_id==21:
                        cat_stat = 'rbi'
                        name_stat = 'RBI'
                if cat_id==22:
                        cat_stat = 'stolen-bases'
                        name_stat = 'Stolen Bases'

        cat_name += cat_stat+'-season-'+str(cat_year/20+50)+str(cat_year_end/20+50)
        if cat_borp=='p':
                question_str = "What pitchers have the most "+str(name_stat)+" in one season "
        else:
                question_str = "What batters have the most "+str(name_stat)+" in one season "

        if cat_borp=='p':
                other_stats = ['wins','war-pitcher','saves','strikeouts']
        else:
                other_stats = ['war-batter','runs','hits','home-runs','rbi','stolen-bases']
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
                if cat_borp=='p':
                        for i in allpitchers:
                                istr += "'"+i[7].replace("'","\\'")+"','"+i[12]+"',"+str(i[11])+","+str(float(i[cat_id]))+","
                else:
                        for i in allpitchers:
                                istr += "'"+i[8].replace("'","\\'")+"','"+i[13]+"',"+str(i[12])+","+str(float(i[cat_id]))+","

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
                if cat_borp=='p':
                        for i in allpitchers:
                                if int(i[18])>29 and int(i[11])>=cat_year+21 and int(i[11])<=cat_year_end-21:
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
                
                        for i in allpitchers:
                                if float(i[cat_id])>=top100[nrows-1]:
                                        istr += "'"+i[7].replace("'","\\'")+"','"+i[12]+"',"+str(i[11])+","+str(float(i[cat_id]))+","
                else:
                        for i in allpitchers:
                                if int(i[15])>29 and int(i[12])>=cat_year+21 and int(i[12])<=cat_year_end-21:
                                        for ii in range(0,nrows):
                                                if float(i[cat_id])>top100[ii]:
                                                        for iii in range(0,nrows-1-ii):
                                                                top100[nrows-1-iii]=top100[nrows-1-iii-1]
                                                                top100data[nrows-1-iii]['year']=top100data[nrows-1-iii-1]['year']
                                                                top100data[nrows-1-iii]['answer']=top100data[nrows-1-iii-1]['answer']
                                                                top100data[nrows-1-iii]['team']=top100data[nrows-1-iii-1]['team']
                                                                top100data[nrows-1-iii]['number']=top100data[nrows-1-iii-1]['number']
                                                        top100[ii]=float(i[cat_id])
                                                        top100data[ii]['year']=int(i[12])
                                                        top100data[ii]['team']=i[13]
                                                        top100data[ii]['number']=float(i[cat_id])
                                                        top100data[ii]['answer']=i[8].replace("'","\\'")
                                                        break
                        for i in allpitchers:
                                if float(i[cat_id])>=top100[nrows-1]:
                                        istr += "'"+i[8].replace("'","\\'")+"','"+i[13]+"',"+str(i[12])+","+str(float(i[cat_id]))+","


                allistr += ' "'+istr[:-1]+'];" '
                allcstr += ' "'+cat_name+'"'
                allqstr += ' "'+question_str+'"'   
                allsstr += suggested_str 
                return allistr,allcstr,allqstr,allsstr

print time.time(),
cat_id = int(sys.argv[1])
cat_year = int(sys.argv[3])
cat_type = sys.argv[2]
cat_borp = sys.argv[4]
allistr = ''
allcstr = ''
allqstr = ''
allsstr = ''
if cat_borp=='p':
        allpitcherraw = readcsv('allpitchdata'+str(cat_id)+'.csv')[1:]
        year_index = readcsv('allpitchdata'+str(cat_id)+'.csv')[0]
else:
        allpitcherraw = readcsv('allbattingdata'+str(cat_id)+'.csv')[1:]
        year_index = readcsv('allbattingdata'+str(cat_id)+'.csv')[0]
for i in range((cat_year+20)/20,2017/20+2):
        allistr,allcstr,allqstr,allsstr = toendyear(i*20,allistr,allcstr,allqstr,allsstr,cat_id,cat_year,cat_type,allpitcherraw,year_index,cat_borp)

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
