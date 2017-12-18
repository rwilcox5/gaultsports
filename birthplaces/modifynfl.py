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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa



allplayers = readcsv("../nfl_data/Basic_Stats.csv")[1:]

allstats = readcsv("../nfl_data/Career_Stats_Defensive.csv")[1:]

player_ids = []
player_mps = []

state_list = ['Indiana', 'Kentucky', 'Idaho', 'Pennsylvania', 'New Jersey', 'Michigan', 'New York', 'Oklahoma', 'Louisiana', 'Texas', 'Ohio', 'Illinois', 'California', 'Minnesota', 'Montana', 'Tennessee', 'Georgia', 'Colorado', 'Wisconsin', 'Utah', 'Wyoming', 'Oregon', 'West Virginia', 'Kansas', 'North Dakota', 'Massachusetts', 'Missouri', 'North Carolina', 'Hawaii', 'Nebraska', 'Arizona', 'Iowa', 'Arkansas', 'South Dakota', 'Maryland', 'Connecticut', 'District of Columbia', 'Mississippi', 'Virginia', 'Alabama', 'New Mexico', 'Florida', 'Washington', 'South Carolina', 'Rhode Island', 'Delaware', 'Maine', 'Nevada', 'New Hampshire', 'Alaska']
state_convert = [["AK","Alaska"],["AL","Alabama"],["AR","Arkansas"],["AZ","Arizona"],["CA","California"],["CO","Colorado"],["CT","Connecticut"],["DC","District of Columbia"],["DE","Delaware"],["FL","Florida"],["GA","Georgia"],["HI","Hawaii"],["IA","Iowa"],["ID","Idaho"],["IL","Illinois"],["IN","Indiana"],["KS","Kansas"],["KY","Kentucky"],["LA","Louisiana"],["MA","Massachusetts"],["MD","Maryland"],["ME","Maine"],["MI","Michigan"],["MN","Minnesota"],["MO","Missouri"],["MS","Mississippi"],["MT","Montana"],["NC","North Carolina"],["ND","North Dakota"],["NE","Nebraska"],["NH","New Hampshire"],["NJ","New Jersey"],["NM","New Mexico"],["NV","Nevada"],["NY","New York"],["OH","Ohio"],["OK","Oklahoma"],["OR","Oregon"],["PA","Pennsylvania"],["RI","Rhode Island"],["SC","South Carolina"],["SD","South Dakota"],["TN","Tennessee"],["TX","Texas"],["UT","Utah"],["VA","Virginia"],["VT","Vermont"],["WA","Washington"],["WI","Wisconsin"],["WV","West Virginia"],["WY","Wyoming"]]

for i in allplayers:
        state = i[1][-2:]
        inus = False
        for ii in state_convert:
                if ii[0]==state:
                        inus = True

        if inus:
                if i[12] not in player_ids:
                        player_ids.append(i[12])
                        player_mps.append(0)
                else:
                        donot = 0
                        print 'duplicated name',i[12]


print len(player_ids)
print len(allstats)

for idx,i in enumerate(allstats):
        if idx%10000==0:
                print idx, time.time()
        for iidx,ii in enumerate(player_ids):
                if player_ids[iidx]==i[0]:
                        try:
                                if len(i[5])>0:
                                        player_mps[iidx]+=int(i[5])
                        except:
                                pass
                        break
modifiedpeople = []
for i in allplayers:
        if i[12] in player_ids:
                state_a = i[1][-2:]
                if len(state_a)>0:
                        modifiedpeople.append([i[12],i[2][-4:],state_a,i[1][:-4],i[10]])
                else:
                        print i[7]
writecsv(modifiedpeople,'modified/Football/People.csv')



modifiedstats = []
for idx,i in enumerate(allstats):
        if idx%10000==0:
                print idx, time.time()
        for iidx,ii in enumerate(player_ids):
                if player_ids[iidx]==i[0]:

                        try:
                                if len(i[5])>0:
                                        player_min=int(i[5])
                                else:
                                        player_min=0
                                if player_min >0:
                                        allstats[idx][0]=allstats[idx][3]
                                        allstats[idx][1]=0
                                        allstats[idx][2]=player_min
                                        allstats[idx] = [str(iidx)]+allstats[idx][0:3]

                                        modifiedstats.append(allstats[idx])

                        except:
                                pass
                        break
writecsv(modifiedstats,'modified/Football/Stats.csv')