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



import sys

for award in ['mvp']:
    #allvotes = getvotes('https://bbwaa.com/17-nl-'+award+'-ballots/')
    #writecsv(allvotes,'nlmvp17.csv')
    goodteams = []
    for iiiiii in range(0,20):


        allvotes = readcsv('nlmvp17.csv')

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
                allteams.remove(i)
                for ii in range(0,len(allvotes)):
                    for iii in range(0,len(allvotes[ii])):
                        if allvotes[ii][iii]==i:
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
                for i in minindex:
                    goodteams.append(i)
            
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
                goodteams.append(allteams[0])













