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



allplayers = readcsv("../../baseballdatabank-master/core/People.csv")[1:]


player_ids = []
player_abs = []
player_bfs = []
player_bref = []
player_teams = []
for i in allplayers:
        player_ids.append(i[0])
        player_abs.append(0)
        player_bfs.append(0)
        player_bref.append(i[23])
        player_teams.append([i[13]+' '+i[14]])

allbatting = readcsv("../../baseballdatabank-master/core/Batting.csv")[1:]
allpitching = readcsv("../../baseballdatabank-master/core/Pitching.csv")[1:]

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
                modifiedpeople.append([i[0],i[23],i[13]+' '+i[14]])
writecsv(modifiedpeople,'modified/People.csv')



modifiedbatting = []
for idx,i in enumerate(allbatting):
        if int(i[1])>1900 and i[4] in ['NL','AL']:
                if idx%10000==0:
                        print idx, time.time()
                for iidx,ii in enumerate(player_ids):
                        if player_ids[iidx]==i[0] and (player_abs[iidx]>500 or player_bfs[iidx]>500):
                                try:
                                        if int(i[6])+int(i[15])+int(i[18])>99:
                                                player_teams[iidx].append(allbatting[idx][3])
                                except:
                                        pass
                                break

for idx,i in enumerate(allpitching):
        if int(i[1])>1900 and i[4] in ['NL','AL']:
                if idx%10000==0:
                        print idx, time.time()
                for iidx,ii in enumerate(player_ids):
                        if player_ids[iidx]==i[0] and (player_abs[iidx]>500 or player_bfs[iidx]>500):
                                try:
                                        if int(i[24])>99:
                                                player_teams[iidx].append(allpitching[idx][3])

                                except:
                                        pass
                                break

writecsv(player_teams,'modified/PlayerTeams.csv')