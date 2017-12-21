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
allawards = readcsv("core/AwardsPlayers.csv")[1:]
allstars = readcsv("core/AllstarFull.csv")[1:]
allhof = readcsv("core/HallOfFame.csv")[1:]
allteams = readcsv("core/Teams.csv")[1:]
allwar = readcsv("core/war_daily_bat.txt")[1:]

player_ids = []
player_abs = []
player_bfs = []
player_bref = []
for i in allplayers:
	player_ids.append(i[0])
	player_abs.append(0)
	player_bfs.append(0)
	player_bref.append(i[23])

allbatting = readcsv("core/Batting.csv")[1:]
allpitching = readcsv("core/Pitching.csv")[1:]

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
notdone = True
starti = 0
while notdone:
	notdone = False
	for idx in range(starti,len(player_ids)):
		if player_abs[idx]<1000 or player_bfs[idx]>player_abs[idx]:
			player_ids.pop(idx)
			player_abs.pop(idx)
			player_bref.pop(idx)
			player_bfs.pop(idx)
			notdone = True
			starti = idx
			break
print len(player_ids)



modifiedhof = []
for i in allhof:
	if i[0] in player_ids and i[7]=='Player':
		notin = True
		for iidx,ii in enumerate(modifiedhof):
			if ii[0]==i[0]:
				notin = False
				if i[6]=='Y':
					if len(i[3])>0:
						modifiedhof[iidx].append(int(i[5])*1./int(i[3]))
						modifiedhof[iidx].append(i[1])
					else:
						modifiedhof[iidx].append(i[1])
				else:
					if len(i[3])>0:
						modifiedhof[iidx].append(int(i[5])*1./int(i[3]))

				break
		if notin:
			modifiedhof.append([i[0]])
			iidx = len(modifiedhof)-1
			if i[6]=='Y':
				if len(i[3])>0:
					modifiedhof[iidx].append(int(i[5])*1./int(i[3]))
					modifiedhof[iidx].append(int(i[1]))
				else:
					modifiedhof[iidx].append(int(i[1]))
			else:
				if len(i[3])>0:
					modifiedhof[iidx].append(int(i[5])*1./int(i[3]))
	
modifiedpeople = []
for i in allplayers:
	if i[0] in player_ids:
		hofelig = False
		for ii in modifiedhof:
			if ii[0]==i[0]:
				hofelig = True
				maxp = -1
				yearInducted = -1
				for iii in ii[1:]:
					if iii>1000:
						yearInducted = iii
					elif iii>maxp:
						maxp = iii

		if hofelig:
			modifiedpeople.append([i[0],i[1],i[4],i[5],i[7],i[16],i[17],i[18],i[19],i[20],i[21],i[23],yearInducted,maxp])
		else:
			modifiedpeople.append([i[0],i[1],i[4],i[5],i[7],i[16],i[17],i[18],i[19],i[20],i[21],i[23],-1,-1])
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

modifiedteams = []
teamyears = []
for i in range(0,150):
	teamyears.append([])
for i in allteams:
	if int(i[0])>1900:
		modifiedteams.append([i[0],i[2],i[3],i[4],i[5],i[8],i[9],i[10],i[11],i[12],i[13],i[40],i[41]])
		teamyears[int(i[0])-1900].append([i[2],i[4],i[5],i[8],i[9],i[10],i[11],i[12],i[13]])
writecsv(modifiedteams,'modified/Teams.csv')

modifiedstars = []
for idx,i in enumerate(allstars):
	if i[0] in player_ids:
		if idx > 1000 and idx < 2000:
			addthis = True
			for ii in range(idx-100,idx):
				if allstars[ii][0]==i[0] and allstars[ii][1]==i[1]:
					addthis = False
					break
			if addthis:
				onlyone = True
				for ii in range(idx+1,idx+100):
					if allstars[ii][0]==i[0] and allstars[ii][1]==i[1]:
						if len(i[7])>0 and len(allstars[ii][7])>0:
							modifiedstars.append([i[0],i[1],2,2,i[7]])
						elif len(i[7])>0 and len(allstars[ii][7])==0:
							modifiedstars.append([i[0],i[1],2,1,i[7]])
						elif len(i[7])==0 and len(allstars[ii][7])>0:
							modifiedstars.append([i[0],i[1],2,1,allstars[ii][7]])
						else:
							modifiedstars.append([i[0],i[1],1,0,0])

						onlyone = False
						break
				if onlyone:
					if len(i[7])>0:
						modifiedstars.append([i[0],i[1],1,1,i[7]])
					else:
						modifiedstars.append([i[0],i[1],1,0,0])

		else:
			if len(i[7])>0:
				modifiedstars.append([i[0],i[1],1,1,i[7]])
			else:
				modifiedstars.append([i[0],i[1],1,0,0])
writecsv(modifiedstars,'modified/AllstarFull.csv')

modifiedawards = []
my_awards = ['Silver Slugger','Gold Glove','Triple Crown','Pitching Triple Crown','Most Valuable Player','Rookie of the Year','Cy Young Award','World Series MVP','NLCS MVP','ALCS MVP','Baseball Magazine All-Star','TSN All-Star','Rolaids Relief Man Award']
no_award = []
for i in allawards:
	if i[0] in player_ids:
		if int(i[2])>1900:
			if i[1] in my_awards:
				modifiedawards.append([i[0],i[1],i[2],i[3],i[5]])
	if i[1] not in no_award:
		no_award.append(i[1])
		print i[1]
writecsv(modifiedawards,'modified/AwardsPlayers.csv')


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
				teamdivision = ''
				teamlgchamp = 'N'
				teamwschamp = 'N'
				teamwins = 0
				teamdivfinish = 0
				for iii in range(0,len(teamyears[int(i[1])-1900])):
					if teamyears[int(i[1])-1900][iii][0]==i[3]:
						teamdivision=teamyears[int(i[1])-1900][iii][1]
						teamlgchamp=teamyears[int(i[1])-1900][iii][7]
						teamwschamp=teamyears[int(i[1])-1900][iii][8]
						teamwins=teamyears[int(i[1])-1900][iii][3]
						teamdivfinish=teamyears[int(i[1])-1900][iii][2]
						break
				try:
					allbatting[idx][0]=allbatting[idx][1]
					allbatting[idx][1]=allbatting[idx][3]
					allbatting[idx][2]=allbatting[idx][4]
					allbatting[idx][3]=war
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
					allbatting[idx] = [str(iidx)]+allbatting[idx][:21]+[teamdivision,teamlgchamp,teamwschamp,teamwins,teamdivfinish]



					modifiedbatting.append(allbatting[idx])

				except:
					pass
				break
writecsv(modifiedbatting,'modified/Batting.csv')