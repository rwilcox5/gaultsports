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



allplayers = readcsv("modified/PlayerTeams.csv")[1:]
def get33(allplayers):
        for team7 in ['LAN','NYA','NYN','MIN','MIL','SDN','CHA','SLN','WAS','PIT','SFN','LAA','TOR','TEX','TBA','MIA','KCA','COL','HOU','OAK','CIN','DET']:
                for team8 in ['LAN','NYA','NYN','MIN','MIL','SDN','CHA','SLN','WAS','PIT','SFN','LAA','TOR','TEX','TBA','MIA','KCA','COL','HOU','OAK','CIN','DET']:
                        team7 = 'PIT'
                        team8 = 'TOR'
                        if team7 != team8:
                                eight_teams = ['CHN','BAL','SEA','PHI','ATL','BOS',team7,team8]
                                found1 = []
                                found2 = []
                                found3 = []
                                found4 = []
                                found5 = []
                                found6 = []
                                found7 = []
                                found8 = []
                                found9 = []
                                for i in allplayers:
                                        team1_list = []
                                        team_list = []
                                        if len(i)>2:
                                                for ii in i[1:]:
                                                        if ii not in team1_list and ii in eight_teams:
                                                                team1_list.append(ii)
                                                        elif ii not in team_list and ii in eight_teams:
                                                                team_list.append(ii)
                                                if len(team_list)>1:
                                                        if eight_teams[0] in team_list and eight_teams[1] in team_list and eight_teams[2] in team_list and eight_teams[3] in team_list:
                                                                found1.append(i[0])
                                                        elif eight_teams[0] in team_list and eight_teams[4] in team_list and eight_teams[5] in team_list:
                                                                found2.append(i[0])
                                                        elif eight_teams[0] in team_list and eight_teams[6] in team_list and eight_teams[7] in team_list:
                                                                found3.append(i[0])
                                                        elif eight_teams[1] in team_list and eight_teams[5] in team_list and eight_teams[7] in team_list:
                                                                found4.append(i[0])
                                                        elif eight_teams[1] in team_list and eight_teams[4] in team_list and eight_teams[6] in team_list:
                                                                found5.append(i[0])
                                                        elif eight_teams[2] in team_list and eight_teams[5] in team_list:
                                                                found6.append(i[0])
                                                        elif eight_teams[3] in team_list and eight_teams[4] in team_list:
                                                                found7.append(i[0])
                                                        elif eight_teams[2] in team_list and eight_teams[6] in team_list:
                                                                found8.append(i[0])
                                                        elif eight_teams[3] in team_list and eight_teams[7] in team_list:
                                                                found9.append(i[0])
                                if len(found1)*len(found2)*len(found3)*len(found4)*len(found5)*len(found6)*len(found7)*len(found8)*len(found9)>0:
                                        print found1
                                        print found2
                                        print found3
                                        print found4
                                        print found5
                                        print found6
                                        print found7
                                        print found8
                                        print found9

def get1010(allplayers):
        teams1 = ['LAN','LAA','NYN','MIN','MIL','COL','CHA','SLN','WAS','PIT']
        teams2 = ['SFN','NYA','TOR','TEX','KCA','SDN','HOU','OAK','CIN','DET']

        for team1 in teams1:
                for team2 in teams2:
                        match = False
                        for i in allplayers:
                                if len(i)>2:
                                        match1 = False
                                        match2 = False
                                        match11 = False
                                        match22 = False
                                        for ii in i[1:]:
                                                if ii==team1:
                                                        if match1:
                                                                match11 = True
                                                        else:
                                                                match1 = True
                                                elif ii==team2:
                                                        if match2:
                                                                match22 = True
                                                        else:
                                                                match2 = True
                                        if match11 and match22:
                                                match = True
                                                break
                        if not match:
                                print team1, team2
greatmatches = readcsv('magicmatches.csv')

def getgreatmatches(greatmatches):
        teams= ['LAN','NYA','NYN','MIN','MIL','SDN','CHA','SLN','WAS','PIT','SFN','LAA','TOR','TEX','TBA','MIA','KCA','COL','HOU','OAK','CIN','DET','ATL','BAL','ARI','CHN','SEA','PHI','BOS']
        for team1 in teams:
                for team2 in teams:
                        runthis = True
                        for i in greatmatches:
                                if [i[0],i[1]]==[team1,team2] or [i[0],i[1]]==[team2,team1]:
                                        runthis = False
                        if team1 != team2 and runthis:
                                match = False
                                allmatches = []
                                for i in allplayers:
                                        if len(i)>2:
                                                match1 = False
                                                match2 = False
                                                match11 = False
                                                match22 = False
                                                match111 = False
                                                match222 = False
                                                match1111 = False
                                                match2222 = False
                                                nomatch = True
                                                for iib in i[1:]:
                                                        ii = iib.replace('FLO','MIA').replace('MON','WAS').replace('TBD','TBA').replace('TBR','TBA')
                                                        if ii==team1:
                                                                if match111:
                                                                        match1111 = True
                                                                elif match11:
                                                                        match111 = True
                                                                elif match1:
                                                                        match11 = True
                                                                else:
                                                                        match1 = True
                                                        elif ii==team2:
                                                                if match222:
                                                                        match2222 = True
                                                                elif match22:
                                                                        match222 = True
                                                                elif match2:
                                                                        match22 = True
                                                                else:
                                                                        match2 = True
                                                        elif ii=='NYN':
                                                                nomatch = False
                                                if match2222 and match1111:
                                                        match = True
                                                        allmatches.append([i[0],i])
                                for i in allmatches:
                                        print team1, team2, i[1]
                                        x = raw_input()
                                        if x=='y':
                                                greatmatches.append([team1,team2,i[0]])
                                                writecsv(greatmatches,'magicmatches.csv')

                                if not match:
                                        print team1, team2
getgreatmatches(greatmatches)

def get55(allplayers):
        teams1 = ['ATL','NYN','BAL','BOS','TBA']
        teams2 = ['MIA','TOR','NYA','PHI','WAS']

        for team1 in teams1:
                for team2 in teams2:
                        if team1 != team2:
                                match = False
                                allmatches = []
                                for i in allplayers:
                                        if len(i)>2:
                                                match1 = False
                                                match2 = False
                                                match11 = False
                                                match22 = False
                                                match111 = False
                                                match222 = False
                                                match1111 = False
                                                match2222 = False
                                                nomatch = True
                                                for iib in i[1:]:
                                                        ii = iib.replace('FLO','MIA').replace('MON','WAS').replace('TBD','TBA').replace('TBR','TBA')
                                                        if ii==team1:
                                                                if match111:
                                                                        match1111 = True
                                                                elif match11:
                                                                        match111 = True
                                                                elif match1:
                                                                        match11 = True
                                                                else:
                                                                        match1 = True
                                                        elif ii==team2:
                                                                if match222:
                                                                        match2222 = True
                                                                elif match22:
                                                                        match222 = True
                                                                elif match2:
                                                                        match22 = True
                                                                else:
                                                                        match2 = True
                                                        elif ii=='NYN':
                                                                nomatch = False
                                                if match2222 and match1111:
                                                        match = True
                                                        allmatches.append(i[0])
                                print team1, team2, allmatches
                                if not match:
                                        print team1, team2
def get77(allplayers):
        teams1 = ['PIT','COL','ARI','LAN','CIN','ATL','MIL']
        teams2 = ['MIA','SFN','SLN','PHI','CHN','WAS','SDN']

        for team1 in teams1:
                for team2 in teams2:
                        if team1 != team2:
                                match = False
                                allmatches = []
                                for i in allplayers:
                                        if len(i)>2:
                                                match1 = False
                                                match2 = False
                                                match11 = False
                                                match22 = False
                                                match111 = False
                                                match222 = False
                                                match1111 = False
                                                match2222 = False
                                                nomatch = True
                                                for iib in i[1:]:
                                                        ii = iib.replace('FLO','MIA').replace('MON','WAS')
                                                        if ii==team1:
                                                                if match111:
                                                                        match1111 = True
                                                                elif match11:
                                                                        match111 = True
                                                                elif match1:
                                                                        match11 = True
                                                                else:
                                                                        match1 = True
                                                        elif ii==team2:
                                                                if match222:
                                                                        match2222 = True
                                                                elif match22:
                                                                        match222 = True
                                                                elif match2:
                                                                        match22 = True
                                                                else:
                                                                        match2 = True
                                                        elif ii=='NYN':
                                                                nomatch = False
                                                if match22 and match11:
                                                        match = True
                                                        allmatches.append(i[0])
                                print team1, team2, allmatches
                                if not match:
                                        print team1, team2

def get77NL(allplayers):
        teamsNL = ['LAN','NYN','MIL','COL','CHN','SLN','WAS','PIT','SFN','SDN','CIN','ATL','MIA','PHI','ARI']

        for tidx, team1 in enumerate(teamsNL):
                match = False
                poss_pairs = []
                player_pair = []
                for i in allplayers:
                        if len(i)>2:
                                other_teams = []
                                other_teams2 = []
                                match = False
                                match2 = False
                                for iib in i[1:]:
                                        ii = iib.replace('FLO','MIA')
                                        if ii==team1:
                                                if match:
                                                        match2 = True
                                                else:
                                                        match = True
                                        elif ii in teamsNL:
                                                if ii in other_teams and ii not in other_teams2:
                                                        other_teams2.append(ii)
                                                if ii not in other_teams:
                                                        other_teams.append(ii)
                                if len(other_teams2)==2 and match2:
                                        for ii in range(0,len(other_teams2)):
                                                for iii in range(ii+1,len(other_teams2)):
                                                        if [other_teams2[ii],other_teams2[iii]] not in poss_pairs:
                                                                poss_pairs.append([other_teams2[ii],other_teams2[iii]])
                                                                player_pair.append([i[0]])
                                                        elif [other_teams2[ii],other_teams2[iii]] in poss_pairs:
                                                                for iiii in range(0,len(poss_pairs)):
                                                                        if poss_pairs[iiii]==[other_teams2[ii],other_teams2[iii]]:
                                                                                player_pair[iiii].append(i[0])
                teamscount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                for i in poss_pairs:
                        for ii in range(0,15):
                                if i[0]==teamsNL[ii]:
                                        teamscount[ii]+=1 
                                if i[1]==teamsNL[ii]:
                                        teamscount[ii]+=1 
                notposs = False
                for i in range(0,15):
                        if i != tidx:
                                if teamscount[i]==0:
                                        notposs = True
                if not notposs:
                        print ''
                        print teamscount
                        print ''
                        for ii in range(0,15):
                                if ii!=tidx:
                                        print teamsNL[ii],
                                        for i in range(0,len(poss_pairs)):
                                                if poss_pairs[i][0]==teamsNL[ii]:
                                                        print poss_pairs[i][1], player_pair[i],
                                                if poss_pairs[i][1]==teamsNL[ii]:
                                                        print poss_pairs[i][0], player_pair[i],
                                        print ''
get55(allplayers)
