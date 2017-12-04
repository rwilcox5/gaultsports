import time
import sys
import random
import csv
import math

def writecsv(parr, filen):
        with open(filen, 'ab') as csvfile:
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



question_teams = ["Did you ever play for the ","Did you only play for the "]
for i in range(2,30):
	question_teams.append("Did you play at least "+str(i)+" seasons for the ")

question_stats = ["Did you ever have at least ","Did you ever have fewer than "]



question_str = 'question_teams = ['
for i in question_teams:
	question_str += '"'+i+'",'
question_str = question_str[:-1]+'];\nquestion_stats = ['
for i in question_stats:
	question_str += '"'+i+'",'
question_str = question_str[:-1]+'];'


team_ids = []
team_name = []
allteamnames = readcsv("core/Teams.csv")[1:]
for idx,i in enumerate(allteamnames):
	allteamnames[idx][40]=allteamnames[idx][40].replace('Redlegs','Reds').replace('Orphans','Cubs').replace('Devil Rays','Rays').replace("Colt .45's",'Astros').replace("Bees",'Braves').replace("Beaneaters",'Braves').replace("Doves",'Braves').replace("Rustlers",'Braves').replace("Naps",'Indians').replace("Americans",'Red Sox').replace("Superbas",'Dodgers').replace("Robins",'Dodgers').replace('Highlanders','Yankees').replace('Bronchos','Indians').replace('Blues','Indians')
	if allteamnames[idx][40].find('Angels')>-1:
		allteamnames[idx][40]='Los Angeles Angels'
	if allteamnames[idx][2]=='BLA':
		allteamnames[idx][40]='New York Yankees'
	if allteamnames[idx][2]=='MLA':
		allteamnames[idx][40]='St. Louis Browns'
for i in allteamnames:
	if int(i[0])>1900 and i[1] in ['NL','AL']:
		if i[2] not in team_ids or i[40] not in team_name:
			team_ids.append(i[2])
			team_name.append(i[40])
team_nicknames = []
for idx,i in enumerate(team_ids):
	name = team_name[idx]
	index1 = name.find(' ')
	index2 = name.find(' ',index1+1)
	if index1 >-1 and index2 ==-1:
		team_nicknames.append([name[index1+1:],i,name])
	elif index1 >-1 and name[:index2] in ['New York','St. Louis','Tampa Bay','Los Angeles','San Diego','San Francisco','Kansas City']:
		team_nicknames.append([name[index2+1:],i,name])
	else:
		print name
		team_nicknames.append([name[index1+1:],i,name])
print len(team_nicknames)
nickname_str = "team_nicknames = ["
for i in team_nicknames:
	nickname_str += '"'+i[0]+'",'

stat_names = []
stats_str = 'stat_names = ['
stat_array = [['homers',11],['triples',10],['doubles',9],['singles',8],['hits',7],['runs',6],['at-bats',5],['games',4],['rbi',12],['sb',13],['walks',14],['strikeouts',15],['hbp',16],['average',17],['onbase',18],['slugging',19]]
other_array = [['year',0],['league',2],['division',3]];
for stat in stat_array:
	stat_name = stat[0]
	stats_str += '"'+stat_name+'",'

f = open('helloworld.txt','w')
f.write(question_str+'\n'+nickname_str[:-1]+'];'+'\n'+stats_str[:-1]+'];')
f.close()


allplayers = readcsv("modified/People.csv")
player_years = []
player_ids = []
for i in allplayers:
	player_ids.append(i[0])
	player_years.append([])

allbatting = readcsv("modified/Batting.csv")
for idx,i in enumerate(allbatting):
	player_years[int(i[0])].append(idx)

print len(player_years)
print player_years[1000]

for player_id_n in range(0,10):	


	answer_str = 'player_array = ['
	for pyear in player_years[player_id_n]:
		year_data = allbatting[pyear][1:]
		answer_str += '{'
		for ii in range(0,len(team_nicknames)):
			if team_nicknames[ii][1]==year_data[1]:
				answer_str += "'nickname':'"+team_nicknames[ii][0]+"',"+"'teamname':'"+team_nicknames[ii][2]+"',"

		for ii in stat_array:
			answer_str += "'"+ii[0]+"':"+str(year_data[ii[1]])+','
		for ii in other_array:
			if ii[0]=='year':
				answer_str += "'"+ii[0]+"':"+str(year_data[ii[1]])+','
			else:
				answer_str += "'"+ii[0]+"':'"+str(year_data[ii[1]])+"',"
		answer_str = answer_str[:-1]+'},'


	answer_str = answer_str[:-1]+'];'
	f = open('../../triplelog/mlb/questions/answers/'+str((player_id_n+7777777)*7777777)+'.js','w')
	f.write(answer_str)
	f.close()




