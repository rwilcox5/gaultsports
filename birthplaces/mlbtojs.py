import time
import sys
import random
import csv
import math

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



allplayers = readcsv("../baseballdatabank-master/core/People.csv")[1:]

allwar = readcsv("../baseballdatabank-master/core/war_daily_bat.txt")[1:]

player_ids = []
player_abs = []
player_bfs = []
player_bref = []
for i in allplayers:
        if i[4]=='USA':
                player_ids.append(i[0])
                player_abs.append(0)
                player_bfs.append(0)
                player_bref.append(i[23])

allbatting = readcsv("../baseballdatabank-master/core/Batting.csv")[1:]
allpitching = readcsv("../baseballdatabank-master/core/Pitching.csv")[1:]

print len(player_ids)
print len(allbatting)
for idx,i in enumerate(allbatting):
        
        if int(i[1])>1900:
                if idx%10000==0:
                        print idx, time.time()
                for iidx,ii in enumerate(player_ids):
                        if player_ids[iidx]==i[0]:
                                try:
                                        player_abs[iidx]+=int(i[6])+int(i[15])+int(i[18])
                                except:
                                        pass
                                break
print len(allpitching)
for idx,i in enumerate(allpitching):
        
        if int(i[1])>1900:
                if idx%10000==0:
                        print idx, time.time()
                for iidx,ii in enumerate(player_ids):
                        if player_ids[iidx]==i[0]:
                                try:
                                        player_bfs[iidx]+=int(i[24])
                                except:
                                        pass
                                break

        
modifiedpeople = []
for i in allplayers:
        if i[0] in player_ids:
                modifiedpeople.append([i[0],i[1],i[5],i[6],i[23],i[13]+' '+i[14]])
writecsv(modifiedpeople,'modified/People.csv')

modifiedwar = []
for i in range(0,len(player_ids)):
        modifiedwar.append([i])
for i in allwar:
        if int(i[4])>1900:
                isgood = False
                for iidx,ii in enumerate(player_bref):
                        if ii==i[3]:
                                pid =iidx
                                isgood = True
                                break
                if isgood:
                        year = int(i[4])
                        modifiedwar[pid].append(year)
                        modifiedwar[pid].append(i[5])
                        try:
                                modifiedwar[pid].append(float(i[30]))
                        except:
                                modifiedwar[pid].append(0)

writecsv(modifiedwar,'modified/war_daily_bat.csv')


modifiedbatting = []
for idx,i in enumerate(allbatting):
        if int(i[1])>1900:
                if idx%10000==0:
                        print idx, time.time()
                for iidx,ii in enumerate(player_ids):
                        if player_ids[iidx]==i[0]:
                                war = 0
                                for iii in range(0,len(modifiedwar[iidx][1:])/3):
                                        if modifiedwar[iidx][iii*3+1]==int(i[1]) and modifiedwar[iidx][iii*3+2]==i[3]:
                                                war = modifiedwar[iidx][iii*3+3]
                                try:
                                        allbatting[idx][0]=allbatting[idx][1]
                                        allbatting[idx][1]=war
                                        allbatting[idx][2]=int(allbatting[idx][6])
                                        allbatting[idx] = [str(iidx)]+allbatting[idx][0:3]

                                        modifiedbatting.append(allbatting[idx])

                                except:
                                        pass
                                break
writecsv(modifiedbatting,'modified/Batting.csv')