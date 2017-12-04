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



allplayers = readcsv("core/People.csv")[1:]
player_ids = []
player_abs = []
for i in allplayers:
	player_ids.append(i[0])
	player_abs.append(0)

allbatting = readcsv("core/Batting.csv")[1:]

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
notdone = True
starti = 0
while notdone:
	notdone = False
	for idx in range(starti,len(player_ids)):
		if player_abs[idx]<1000:
			player_ids.pop(idx)
			player_abs.pop(idx)
			notdone = True
			starti = idx
			break
print len(player_ids)

modifiedpeople = []
for i in allplayers:
	if i[0] in player_ids:
		modifiedpeople.append(i)
writecsv(modifiedpeople,'modified/People.csv')

modifiedbatting = []
for idx,i in enumerate(allbatting):
	if int(i[1])>1900:
		if idx%10000==0:
			print idx, time.time()
		for iidx,ii in enumerate(player_ids):
			if player_ids[iidx]==i[0]:
				try:
					allbatting[idx][0]=allbatting[idx][1]
					allbatting[idx][1]=allbatting[idx][3]
					allbatting[idx][2]=allbatting[idx][4]
					allbatting[idx][3]='all'
					allbatting[idx][4]=allbatting[idx][5]
					allbatting[idx][5]=int(allbatting[idx][6])
					allbatting[idx][6]=int(allbatting[idx][7])
					allbatting[idx][7]=int(allbatting[idx][8])
					allbatting[idx][8]=int(allbatting[idx][7])-int(allbatting[idx][9])-int(allbatting[idx][10])-int(allbatting[idx][11])
					allbatting[idx][9]=int(allbatting[idx][9])
					allbatting[idx][10]=int(allbatting[idx][10])
					allbatting[idx][11]=int(allbatting[idx][11])
					allbatting[idx][12]=int(allbatting[idx][12])
					allbatting[idx][13]=int(allbatting[idx][13])
					allbatting[idx][14]=int(allbatting[idx][15])
					try:
						allbatting[idx][15]=int(allbatting[idx][16])
					except:
						allbatting[idx][15]=0
					try:
						allbatting[idx][16]=int(allbatting[idx][18])
					except:
						allbatting[idx][16]=0
					allbatting[idx][17]=round(int(allbatting[idx][7])*1./int(allbatting[idx][5]),3)
					allbatting[idx][18]=round((allbatting[idx][7]+allbatting[idx][14]+allbatting[idx][16])*1./(allbatting[idx][5]+allbatting[idx][14]+allbatting[idx][16]),3)
					allbatting[idx][19]=round((allbatting[idx][7]+allbatting[idx][9]+2*allbatting[idx][10]+3*allbatting[idx][11])*1./allbatting[idx][5],3)
					allbatting[idx][20]=round(allbatting[idx][18]+allbatting[idx][19],3)
					allbatting[idx][21]=5
					allbatting[idx] = [str(iidx)]+allbatting[idx]



					modifiedbatting.append(allbatting[idx])

				except:
					pass
				break
writecsv(modifiedbatting,'modified/Batting.csv')