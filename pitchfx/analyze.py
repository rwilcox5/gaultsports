import csv
import time
allpitches = []
badpitches = []
allabs = []
nbad = 0

#with open('atbat_table.csv', newline='') as csvfile:
#	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#	for row in spamreader:
#		allabs.append([row[0],row[22],row[33]])
#
#with open('pitch_table.csv', newline='') as csvfile:
#	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#	ii = 0
#	print(time.time())
#	for row in spamreader:
#		ii = ii+1
#		if ii%1000 == 0:
#			print(ii, len(allpitches),len(allabs),time.time())
#		if ii >= 0:
#			try:
#				for i in range(1,len(allabs)):
#					if row[0]== allabs[i][0]:
#						if int(row[31])==int(allabs[i][1]):
#							ab_result = allabs[i][2]
#							allabs.pop(i)
#							break
#
#				allpitches.append([row[20],row[21],int(row[22]),int(row[23]),row[32],row[33],float(row[39]),float(row[40]),float(row[43]),float(row[44]),int(row[60]),ab_result])
#			except:
#				badpitches.append([row[20],row[21],row[22],row[23],row[32],row[33],row[39],row[40],row[43],row[44],row[60],row[31],row[0]])
#				nbad = nbad+1
#
#with open('combined_table.csv', 'w', newline='') as csvfile:
#	spamwriter = csv.writer(csvfile,delimiter=',',quotechar='"')
#	for i in allpitches:
#		spamwriter.writerow(i)
with open('combined_table.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		allpitches.append([row[0],row[1],int(row[2]),int(row[3]),row[4],row[5],float(row[6]),float(row[7]),float(row[8]),float(row[9]),int(row[10]),row[11]])



print(nbad)

allzonesp = [[0,0,0],[0,0,0],[0,0,0],[0,0,0,0,0]]
allzoness = [[0,0,0],[0,0,0],[0,0,0],[0,0,0,0,0]]
ptotal = 0


all_plays = ['Single','Double','Triple','Home Run','Lineout','Groundout','Pop Out','Flyout','Fan interference','Grounded Into DP','Forceout','Field Error','Sac Bunt','Fielders Choice','Bunt Pop Out','Fielders Choice Out','Double Play','Sac Fly','Batter Interference','Walk','Strikeout','Bunt Groundout','Sac Fly DP','Hit By Pitch','Catcher Interference','Intent Walk','Bunt Lineout','Triple Play']
all_outs = []

count = [2,2]

for i in range(0,len(allpitches)):
	if allpitches[i][1]=='R':
		if allpitches[i][2]==count[0]:
			if allpitches[i][3]>=count[1]:
				if allpitches[i][4] in ['X','S','B','C','F']:
					zone = allpitches[i][10]
					if zone in range(1,13):
						allzonesp[int((zone-1)/3)][(zone-1)%3] = allzonesp[int((zone-1)/3)][(zone-1)%3]+1
						if allpitches[i][11] in ['Home Run']:
							allzoness[int((zone-1)/3)][(zone-1)%3] = allzoness[int((zone-1)/3)][(zone-1)%3]+1
						ptotal = ptotal+1
					if zone in [13,14]:
						allzonesp[3][zone-10] = allzonesp[3][zone-10]+1
						ptotal=ptotal+1



for zone in range(1,13):
	if allzonesp[int((zone-1)/3)][(zone-1)%3]>0:
		#print(allzoness[int((zone-1)/3)][(zone-1)%3]*1./allzonesp[int((zone-1)/3)][(zone-1)%3])
		print(allzonesp[int((zone-1)/3)][(zone-1)%3]*1./ptotal)
	else:
		print(0)
for zone in range(13,15):
	if allzonesp[3][zone-10]>0:
		#print(allzoness[int((zone-1)/3)][(zone-1)%3]*1./allzonesp[int((zone-1)/3)][(zone-1)%3])
		print(allzonesp[3][zone-10]*1./ptotal)
	else:
		print(0)
for zone in range(1,13):
	print(allzonesp[int((zone-1)/3)][(zone-1)%3])

