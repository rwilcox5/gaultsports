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



allplayers = readcsv("../basketball-quizzes/core/Players.csv")[1:]

allstats = readcsv("../basketball-quizzes/core/Seasons_Stats.csv")[1:]

player_ids = []
player_mps = []

state_list = ['Indiana', 'Kentucky', 'Idaho', 'Pennsylvania', 'New Jersey', 'Michigan', 'New York', 'Oklahoma', 'Louisiana', 'Texas', 'Ohio', 'Illinois', 'California', 'Minnesota', 'Montana', 'Tennessee', 'Georgia', 'Colorado', 'Wisconsin', 'Utah', 'Wyoming', 'Oregon', 'West Virginia', 'Kansas', 'North Dakota', 'Massachusetts', 'Missouri', 'North Carolina', 'Hawaii', 'Nebraska', 'Arizona', 'Iowa', 'Arkansas', 'South Dakota', 'Maryland', 'Connecticut', 'District of Columbia', 'Mississippi', 'Virginia', 'Alabama', 'New Mexico', 'Florida', 'Washington', 'South Carolina', 'Rhode Island', 'Delaware', 'Maine', 'Nevada', 'New Hampshire', 'Alaska']

for i in allplayers:
        if i[7] in state_list:
                if i[1] not in player_ids:
                        player_ids.append(i[1])
                        player_mps.append(0)
                else:
                        print 'duplicated name',i[1]


print len(player_ids)
print len(allstats)

for idx,i in enumerate(allstats):
        if idx%10000==0:
                print idx, time.time()
        for iidx,ii in enumerate(player_ids):
                if player_ids[iidx]==i[2]:
                        try:
                                if len(i[8])>0:
                                        player_mps[iidx]+=int(i[8])
                                else:
                                        if len(i[52])>0:
                                                player_mps[iidx]+=int(i[52])*2.36
                        except:
                                pass
                        break
state_convert = [["AK","Alaska"],["AL","Alabama"],["AR","Arkansas"],["AZ","Arizona"],["CA","California"],["CO","Colorado"],["CT","Connecticut"],["DC","District of Columbia"],["DE","Delaware"],["FL","Florida"],["GA","Georgia"],["HI","Hawaii"],["IA","Iowa"],["ID","Idaho"],["IL","Illinois"],["IN","Indiana"],["KS","Kansas"],["KY","Kentucky"],["LA","Louisiana"],["MA","Massachusetts"],["MD","Maryland"],["ME","Maine"],["MI","Michigan"],["MN","Minnesota"],["MO","Missouri"],["MS","Mississippi"],["MT","Montana"],["NC","North Carolina"],["ND","North Dakota"],["NE","Nebraska"],["NH","New Hampshire"],["NJ","New Jersey"],["NM","New Mexico"],["NV","Nevada"],["NY","New York"],["OH","Ohio"],["OK","Oklahoma"],["OR","Oregon"],["PA","Pennsylvania"],["RI","Rhode Island"],["SC","South Carolina"],["SD","South Dakota"],["TN","Tennessee"],["TX","Texas"],["UT","Utah"],["VA","Virginia"],["VT","Vermont"],["WA","Washington"],["WI","Wisconsin"],["WV","West Virginia"],["WY","Wyoming"]]
modifiedpeople = []
for i in allplayers:
        if i[1] in player_ids:
                state_a=''
                for ii in state_convert:
                        if ii[1]==i[7]:
                                state_a = ii[0]
                if len(state_a)>0:
                        modifiedpeople.append([i[1],i[5],state_a,i[6]])
                else:
                        print i[7]
writecsv(modifiedpeople,'modified/Basketball/People.csv')



modifiedstats = []
for idx,i in enumerate(allstats):
        if idx%10000==0:
                print idx, time.time()
        for iidx,ii in enumerate(player_ids):
                if player_ids[iidx]==i[2]:

                        try:
                                if len(i[8])>0:
                                        player_min=int(i[8])
                                else:
                                        if len(i[52])>0:
                                                player_min=int(int(i[52])*2.36)
                                        else:
                                                player_min=0
                                if player_min >0:
                                        allstats[idx][0]=allstats[idx][1]
                                        allstats[idx][1]=allstats[idx][24]
                                        allstats[idx][2]=player_min
                                        allstats[idx] = [str(iidx)]+allstats[idx][0:3]

                                        modifiedstats.append(allstats[idx])

                        except:
                                pass
                        break
writecsv(modifiedstats,'modified/Basketball/Stats.csv')