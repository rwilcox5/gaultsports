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



allplayers = readcsv("modified/Basketball/People.csv")
allstats = readcsv("modified/Basketball/Stats.csv")


allplayerdata = []
for idx,i in enumerate(allplayers):
        playerdata = []
        try:
                playerdata.append(int(i[1]))
        except:
                playerdata.append(0) 
        playerdata.append(i[2])
        playerdata.append(i[3])
        playerdata.append(0)
        playerdata.append(0)
        playerdata.append([])
        allplayerdata.append(playerdata)


topplayerdata = []
for idx,i in enumerate(allplayers):
        playerdata = [i[0]]
        try:
                playerdata.append(int(i[1]))
        except:
                playerdata.append(0) 
        playerdata.append(i[2])
        playerdata.append(i[3])
        playerdata.append(2150)
        playerdata.append(0)
        playerdata.append(0)
        playerdata.append(0)
        topplayerdata.append(playerdata)

for idx,i in enumerate(allstats):
        try:
                pid = int(i[0])
                atbats = int(i[3])
                year = int(i[1])
                war = float(i[2])
                if atbats>0:
                        allplayerdata[pid][3]+=atbats
                        allplayerdata[pid][4]+=war
                        allplayerdata[pid][5].append(year)
                        allplayerdata[pid][5].append(atbats)
                        topplayerdata[pid][6]+=atbats
                        topplayerdata[pid][7]+=war
                        if year < topplayerdata[pid][4]:
                                topplayerdata[pid][4]=year
                        if year > topplayerdata[pid][5]:
                                topplayerdata[pid][5]=year


        except:
                pass

allstatedata = []
allstateyears = []
for idx,i in enumerate(allplayerdata):
        if i[3]>0:
                if i[1]+str(i[0]) not in allstateyears:
                        allstateyears.append(i[1]+str(i[0]))
                        allstatedata.append([idx])
                else:
                        for iidx,ii in enumerate(allstateyears):
                                if ii==i[1]+str(i[0]):
                                        allstatedata[iidx].append(idx)
                                        break
statearray = []
for idx,i in enumerate(allstateyears):
        statedata = []
        statedata.append(i[2:])
        statedata.append(i[:2])
        statedata.append('')
        statedata.append(0)
        statedata.append(0)
        statedata.append([])
        for ii in allstatedata[idx]:
                statedata[3]+=allplayerdata[ii][3]
                statedata[4]+=allplayerdata[ii][4]
                for iii in range(0,len(allplayerdata[ii][5])/3):
                        alreadyin = False
                        for iiii in range(0,len(statedata[5])/3):
                                if allplayerdata[ii][5][iii*3]==statedata[5][iiii*3]:
                                        statedata[5][iiii*3+1]+=allplayerdata[ii][5][iii*3+1]
                                        statedata[5][iiii*3+2]+=allplayerdata[ii][5][iii*3+2]
                                        alreadyin = True
                                        break
                        if not alreadyin:
                                statedata[5].append(allplayerdata[ii][5][iii*3])
                                statedata[5].append(allplayerdata[ii][5][iii*3+1])
                                statedata[5].append(allplayerdata[ii][5][iii*3+2])

        statearray.append(statedata)






statelist = []
mlb_str = 'players.push(['

for i in statearray:
        if len(i[5])>0:
                mlb_str += '['
                mlb_str += str(i[0])+',"'
                mlb_str += i[1]+'","'
                mlb_str += i[2]+'",'
                mlb_str += str(i[3])+','
                mlb_str += str(i[4])+',['
                for ii in i[5]:
                        mlb_str += str(ii)+','
                mlb_str = mlb_str[:-1]+']],'

                if i[1] not in statelist:
                        statelist.append(i[1])

top_str = 'topplayers.push(['
for i in topplayerdata:
        if i[4]>0:
                top_str += '["'
                top_str += i[0]+'",'
                top_str += str(i[1])+',"'
                top_str += i[2]+'","'
                top_str += i[3]+'",'
                top_str += str(i[4])+','
                top_str += str(i[5])+','
                top_str += str(i[6])+','
                top_str += str(i[7])+','
                top_str = top_str[:-1]+'],'

state_str = '{'
for i in statelist:
        state_str+="'"+i+"':0,"
state_str = state_str[:-1]+'};'
print state_str



f = open('nbadata.js','w')
f.write(mlb_str[:-1]+']);\n'+top_str[:-1]+']);\n')
f.close()

