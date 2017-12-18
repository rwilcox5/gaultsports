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
for team7 in ['LAN','NYY','NYN','MIN','MIL','SDN','CHA','STL','WAS','PIT','SFN','LAA','TOR','TEX','TBA','MIA','KCA','COL','HOU','OAK','CIN','DET']:
        for team8 in ['LAN','NYY','NYN','MIN','MIL','SDN','CHA','STL','WAS','PIT','SFN','LAA','TOR','TEX','TBA','MIA','KCA','COL','HOU','OAK','CIN','DET']:
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

