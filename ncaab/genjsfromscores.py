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

allgames = readcsv('allgames2017.csv')
for i in range(0,len(allgames)):
        allgames[i][0] = allgames[i][0].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell').replace('usc-upstate','sc-upstate')
        allgames[i][1] = allgames[i][1].replace('alcorn-st','alcorn').replace('long-island','liu-brooklyn').replace('st-francis-ny','st-francis-brooklyn').replace('st-francis-pa','saint-francis-pa').replace('loyola-il','loyola-chicago').replace('md-east-shore','umes').replace('st-peters','saint-peters').replace('umass-lowell','mass-lowell').replace('usc-upstate','sc-upstate')

allteams = readcsv('conflist.csv')
allteamnames = readcsv('abbrevTOnames.csv')

teamstr = 'allteams = ['
teamnamestr = 'allteamnames = ['
teams = []
clist = []
confstr = 'allconfs = ['
idx = 0
for i in allteams:
        confstr +='["'+i[0]+'",'+str(idx)+','
        for ii in i[1:]:
                if len(ii)>0:
                        teams.append(ii)
                        clist.append(i[0])
                        teamstr += '"'+ii+'",'
                        foundteam = False
                        for iii in allteamnames:
                                if iii[1]==ii:
                                        teamnamestr +='"'+iii[2]+'",'
                                        foundteam = True
                        if not foundteam:
                                print "DANGER", ii, i
                                print soto

                        ingames = False
                        for iii in allgames:
                                if iii[0]==ii:
                                        ingames = True
                                        break
                        if not ingames:
                                print ii
                        idx +=1
        confstr += str(idx)+',0],'
print confstr

allarenas = []
for i in teams:
        myarenas = []
        for ii in allgames:
                if ii[1]==i:
                        try:
                                nomatch = True
                                for iii in myarenas:
                                        if ii[7]==iii[0]:
                                                iii[1]+=1
                                                nomatch = False
                                                break
                                if nomatch:
                                        myarenas.append([ii[7],1])
                        except:
                                pass
        homemax = 2
        homearena = '???'
        for ii in myarenas:
                if ii[1]>homemax:
                        homemax = ii[1]
                        homearena = ii[0]
        allarenas.append(homearena)

for ii in allgames:
        if ii[0] in teams and ii[1] in teams and len(ii)>7:
                homearena = '???'
                for iiiidx in range(0,len(allarenas)):
                        if teams[iiiidx]==ii[1]:
                                homearena = allarenas[iiiidx]
                ishome = False
                if homearena =='???':
                        ishome = True
                if ii[7]==homearena:
                        ishome = True
                ii.append(ishome)
alldata = []
for i in teams:
        datarow = [i]
        for ii in allgames:
                if ii[0] in teams and ii[1] in teams:
                        ishome = True
                        if len(ii)>8:
                                ishome=ii[8]
                        if ii[0]==i:
                                if clist[teams.index(ii[0])]== clist[teams.index(ii[1])]:
                                        if ishome:
                                                datarow.append('@c')
                                        else:
                                                datarow.append('nc')
                                else:
                                        if ishome:
                                                datarow.append('@n')
                                        else:
                                                datarow.append('nn')
                                datarow.append(ii[1])
                                if len(ii)>5:
                                        if int(ii[2])>int(ii[3]):
                                                datarow.append('W '+str(ii[2])+'-'+str(ii[3]))
                                        else:
                                                datarow.append('L '+str(ii[3])+'-'+str(ii[2]))
                                else:
                                        datarow.append('')
                        if ii[1]==i:
                                if clist[teams.index(ii[0])]== clist[teams.index(ii[1])]:
                                        if ishome:
                                                datarow.append('hc')
                                        else:
                                                datarow.append('nc')
                                else:
                                        if ishome:
                                                datarow.append('hn')
                                        else:
                                                datarow.append('nn')
                                datarow.append(ii[0])
                                if len(ii)>5:
                                        if int(ii[3])>int(ii[2]):
                                                datarow.append('W '+str(ii[3])+'-'+str(ii[2]))
                                        else:
                                                datarow.append('L '+str(ii[2])+'-'+str(ii[3]))
                                else:
                                        datarow.append('')
        alldata.append(datarow)


print alldata[35]
print len(alldata)


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
                                        if alldata[i][ii*3+1]=='hc':
                                                tstr += str(iiidx)+','
                                                tstr += str(myteam)+','
                                                tstr += str(1)+','
                                        elif alldata[i][ii*3+1]=='hn':
                                                tstr += str(iiidx)+','
                                                tstr += str(myteam)+','
                                                tstr += str(0)+','
                                        elif alldata[i][ii*3+1]=='vs.':
                                                if myteam > iiidx:
                                                        tstr += str(10000+iiidx)+','
                                                        tstr += str(10000+myteam)+','

        pstr = pstr[:-1]+ '],'
f = open('helloworld.txt','w')
f.write(pstr[:-1]+'];\n'+tstr[:-1]+'];\n'+teamstr[:-1]+'];\n'+teamnamestr[:-1]+'];\n')
f.close()
