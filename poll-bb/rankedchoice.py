import time

import random
import csv
import math

import lxml
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from lxml.cssselect import CSSSelector
import requests


def writecsv(parr, filen):
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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa



def getvotes(burl):
    allvotes = [[],[],[],[],[],[],[],[],[],[]]
    res = requests.get(burl)
    doc = html.fromstring(res.content)
    voteTable = doc.xpath("//tbody//td")
    for idx,vote in enumerate(voteTable):
        if idx%13>=3:
            allvotes[idx%13-3].append(vote.text_content())
    return allvotes

def unbiasedRank(my_week):
    allvoters = []
    allvotes = readcsv('ap1718/week'+str(my_week)+'.csv')
    for i in allvotes:
        allvoters.append(i[0])


    allvoterdata = []
    for voter in allvoters:
        allvotes = readcsv('ap1718/week'+str(my_week)+'.csv')
        for ii in allvotes:
            if ii[0]==voter:
                voterranks = ii[1:]
                allranks = voterranks
        allvoterdata.append(allranks)

    top25 = []
    for i in apmassey:
        rating = 0
        for voter in allvoterdata:
            for iidx,ii in enumerate(voter):
                if ii==i[1]:
                    rating += max(0,25-iidx)
        top25.append([i[1], rating, rating,0])

    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0,len(top25)-1):
            if top25[i][2]<top25[i+1][2]:
                holdit = top25[i]
                top25[i]=top25[i+1]
                top25[i+1]=holdit
                unsorted = True
    return top25

import sys
this_week = int(sys.argv[1])

allranks = []
for week in range(1,this_week+1):
    #allvotes = getvotes('https://bbwaa.com/17-nl-'+award+'-ballots/')
    #writecsv(allvotes,'nlmvp17.csv')
    goodteams = []
    for iiiiii in range(0,25):


        rawvotes = readcsv('ap1718/week'+str(week)+'.csv')
        allvotes = []
        for i in range(0,25):
            allvotes.append([])
        for i in rawvotes:
            if len(i)>25:
                for ii in range(0,25):
                    allvotes[ii].append(i[ii+1])


        orderedvotes = []
        for ii in range(0,len(allvotes[0])):
            orderedvotes.append([])
        for i in range(0,len(allvotes)):
            for ii in range(0,len(allvotes[0])):
                orderedvotes[ii].append(allvotes[i][ii])
        allvotes = orderedvotes



        allteams = []
        for i in allvotes:
            for ii in i:
                if ii not in allteams:
                    allteams.append(ii)

        for i in goodteams:
                allteams.remove(i[0])
                for ii in range(0,len(allvotes)):
                    for iii in range(0,len(allvotes[ii])):
                        if allvotes[ii][iii]==i[0]:
                            allvotes[ii].remove(allvotes[ii][iii])
                            break

        anyoneleft = True
        while anyoneleft:
            allwp = []
            for idx,i in enumerate(allteams):
                mywins = 0
                mylosses = 0
                myties = 0
                for ii in allteams:
                    if ii != i:
                        p1wins = 0
                        p1losses = 0
                        for iii in range(0,len(allvotes)):
                            player1 = len(allvotes[iii])
                            player2 = len(allvotes[iii])
                            for iiii in range(0,len(allvotes[iii])):
                                if allvotes[iii][iiii]==i:
                                    player1 = iiii
                                elif allvotes[iii][iiii]==ii:
                                    player2 = iiii
                            if player1<player2:
                                p1wins += 1
                            elif player2<player1:
                                p1losses += 1

                        if p1wins*1./(p1wins+p1losses)>.5:
                            mywins += 1
                        elif p1wins*1./(p1wins+p1losses)<.5:
                            mylosses += 1
                        else:
                            myties +=1
                if mywins+mylosses ==0:
                    allwp.append(.5)
                else:
                    allwp.append(mywins*1./(mywins+mylosses))
            minwp = 2.
            minindex = []
            for idx,i in enumerate(allwp):
                if i<minwp:
                    minwp = i
                    minindex = [allteams[idx]]
                elif i==minwp:
                    minindex.append(allteams[idx])
            if len(minindex)==len(allteams):
                anyoneleft = False
                print minindex
                for idx,i in enumerate(minindex):
                    goodteams.append([i,idx])
            
            for i in minindex:
                allteams.remove(i)
                for ii in range(0,len(allvotes)):
                    for iii in range(0,len(allvotes[ii])):
                        if allvotes[ii][iii]==i:
                            allvotes[ii].remove(allvotes[ii][iii])
                            break
            if 1==len(allteams):
                anyoneleft = False
                print allteams
                goodteams.append([allteams[0],0])

    allranks.append(goodteams)




csvapmassey = readcsv('convertedapmassey.csv')
apmassey = []
nameconvert = []
for i in csvapmassey:
    apmassey.append([i[0],i[3],int(i[2])])
    nameconvert.append([i[3],i[1]])

top25un = unbiasedRank(this_week)

top25 = allranks[-1]
allteams = []
for i in top25:
    for ii in apmassey:
        if ii[1]==i[0]:
            conf = ii[0]
    for ii in nameconvert:
        if ii[0]==i[0]:
            namename = ii[1]
    unrank = 'NR'
    for iidx,ii in enumerate(top25un[:25]):
        if ii[0]==i[0]:
            unrank = iidx+1

    this_team = [namename,conf,i[1],unrank,[]]

    for ii in allranks:
        isranked = False
        for iiidx,iii in enumerate(ii):
            if iii[0]==i[0]:
                this_team[4].append(max(0,25-(iiidx-iii[1])))
                isranked = True
                break
        if not isranked:
            this_team[4].append(0)
    allteams.append(this_team)
print allteams


istr = 'top25RC = ['
for i in allteams:
    namename = i[0].replace('"','')
    confname = i[1].replace('"','')
    weightedpoints = str(i[2])
    aprank = str(i[3])
    allranks = i[4]
    istr +='["'+namename+'","'+confname+'",'+weightedpoints+','+aprank+','+'['
    for iii in range(0,len(allranks)):
        istr += str(allranks[iii])+','
    istr = istr[:-1]+']],'
istr = istr[:-1]+'];'

f = open('helloworldRC.txt','w')
f.write(istr+'\n')
f.close()












