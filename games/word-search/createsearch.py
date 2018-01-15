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


def checkwordloc(words_entered,type,typeID,startID,direction,word,nsize):
        the_word = [[type,typeID]]
        for i in words_entered:
                if i[0][0]==type and i[0][1]==typeID:
                        return ['No']
        if type=='row':
                if direction =='forward':
                        for i in range(0,10):
                                the_word.append([word[i],typeID,startID+i]) 
                elif direction =='back':
                        for i in range(0,10):
                                the_word.append([word[9-i],typeID,startID+i]) 
        if type=='column':
                if direction =='forward':
                        for i in range(0,10):
                                the_word.append([word[i],startID+i,typeID]) 
                elif direction =='back':
                        for i in range(0,10):
                                the_word.append([word[9-i],startID+i,typeID]) 
        if type=='diagonal1':
                if direction =='forward':
                        for i in range(0,10):
                                the_word.append([word[i],nsize-10-typeID+startID+i,0+startID+i]) 
                elif direction =='back':
                        for i in range(0,10):
                                the_word.append([word[9-i],nsize-10-typeID+startID+i,0+startID+i])
        ngood = 0
        for i in the_word[1:]:
                for ii in words_entered:
                        for iii in ii[1:]:
                                if iii[1]==i[1] and iii[2]==i[2]:
                                        if iii[0]==i[0]:
                                                ngood+=1
                                        else:
                                                return ['No']
        return ['Yes',the_word,ngood]
def createletters(year_id):
        allplayers = readcsv('top10batting'+str(year_id)+'.csv')
        letters = []
        for i in allplayers:
                for ii in i[1:]:
                        if ii not in letters:
                                letters.append(ii)
        return letters

def createpuzzle(year_id,nsize):
        allplayers = readcsv('top10batting'+str(year_id)+'.csv')
        letters = []
        words = []
        rows = []
        columns = []
        diagonals = []
        allletters = createletters(year_id)
        for i in range(0,nsize):
                rows.append(True)
                columns.append(True)
                diagonals.append(True)
        for i in range(nsize,(nsize-10)*4+2):
                diagonals.append(True)
        for i in allplayers:
                for ii in i[1:]:
                        if ii not in letters:
                                letters.append(ii)
                words.append(i[1:])
        words_entered = []
        for i in words:
                poss_spots = []
                for ii in range(0,nsize):
                        for iii in range(0,nsize-9):
                                wordval = checkwordloc(words_entered,'row',ii,iii,'forward',i,nsize)
                                if wordval[0]=='Yes':
                                        poss_spots.append([wordval[1],wordval[2]])
                                wordval = checkwordloc(words_entered,'row',ii,iii,'back',i,nsize)
                                if wordval[0]=='Yes':
                                        poss_spots.append([wordval[1],wordval[2]])
                                wordval = checkwordloc(words_entered,'column',ii,iii,'forward',i,nsize)
                                if wordval[0]=='Yes':
                                        poss_spots.append([wordval[1],wordval[2]])
                                wordval = checkwordloc(words_entered,'column',ii,iii,'back',i,nsize)
                                if wordval[0]=='Yes':
                                        poss_spots.append([wordval[1],wordval[2]])
                for ii in range(0,6):
                        for iii in range(0,ii+1):
                                wordval = checkwordloc(words_entered,'diagonal1',ii,iii,'forward',i,nsize)
                                if wordval[0]=='Yes':
                                        poss_spots.append([wordval[1],wordval[2]])
                for ii in range(6,11):
                        for iii in range(ii-5,6):
                                wordval = checkwordloc(words_entered,'diagonal1',ii,iii,'forward',i,nsize)
                                if wordval[0]=='Yes':
                                        poss_spots.append([wordval[1],wordval[2]])
                maxgood = 0
                best_spots = []
                for ii in poss_spots:
                        if ii[1]>maxgood:
                                maxgood = ii[1]
                                best_spots = [ii[0]]
                        elif ii[1]==maxgood:
                                best_spots.append(ii[0])
                if len(best_spots)>1:
                        x = random.randint(0,len(best_spots)-1)
                else:
                        x = 0
                words_entered.append(best_spots[x])
        search_table = []
        nletters = 0
        for i in range(0,nsize):
                search_table.append([])
                for ii in range(0,nsize):
                        search_table[i].append('')
        for i in range(0,nsize):
                for ii in range(0,nsize):
                        for iii in words_entered:
                                for iiii in iii[1:]:
                                        if iiii[1]==i and iiii[2]==ii:
                                                if search_table[i][ii]=='':
                                                        nletters+=1
                                                search_table[i][ii]=iiii[0]
        markdown_str = '|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|\n'                                        
        markdown_str += '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n'
        for i in range(0,nsize):
                markdown_str += '|'
                for ii in range(0,nsize):
                        if len(search_table[i][ii])>0:
                                markdown_str += search_table[i][ii]+'|'
                        else:
                                search_table[i][ii]=allletters[random.randint(0,len(allletters)-1)]
                                markdown_str += search_table[i][ii]+'|'
                markdown_str += '\n'


        return [search_table,nletters]
                
minletters = 225
for i in range(0,100):
        try:
                puzz = createpuzzle(2016,14)
                print puzz[1]
                if puzz[1]<minletters:
                        minletters = puzz[1]
                        minpuzz = puzz[0]
        except:
                pass
print 'letters = ',
print minpuzz,
print ';'
warleaders = readcsv('top10batting'+str(2016)+'.csv')[0][1:]
hrleaders = readcsv('top10batting'+str(2016)+'.csv')[1][1:]
runsleaders = readcsv('top10batting'+str(2016)+'.csv')[2][1:]
hitsleaders = readcsv('top10batting'+str(2016)+'.csv')[3][1:]
rbileaders = readcsv('top10batting'+str(2016)+'.csv')[4][1:]
sbleaders = readcsv('top10batting'+str(2016)+'.csv')[5][1:]
bbleaders = readcsv('top10batting'+str(2016)+'.csv')[6][1:]
soleaders = readcsv('top10batting'+str(2016)+'.csv')[7][1:]
print 'stats = {"war":',
print warleaders,
print ', "homeruns":',
print hrleaders,
print ', "runs":',
print runsleaders,
print ', "hits":',
print hitsleaders,
print ', "rbi":',
print rbileaders,
print ', "sb":',
print sbleaders,
print ', "bb":',
print bbleaders,
print ', "so":',
print soleaders,
print '};'

