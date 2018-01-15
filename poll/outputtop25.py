import time
import sys
import random
import csv
import math
import threading
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
nteams = 130
this_week = int(sys.argv[1])

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


apconvert = [["ACC","boston-college",103],["ACC","clemson",228],["ACC","duke",150],["ACC","florida-state",52],["ACC","georgia-tech",59],["ACC","louisville",97],["ACC","miami-fl",2390],["ACC","north-carolina",153],["ACC","north-carolina-state",152],["ACC","pittsburgh",221],["ACC","syracuse",183],["ACC","virginia",258],["ACC","virginia-tech",259],["ACC","wake-forest",154],["Big 12","baylor",239],["Big 12","iowa-state",66],["Big 12","kansas",2305],["Big 12","kansas-state",2306],["Big 12","oklahoma",201],["Big 12","oklahoma-state",197],["Big 12","tcu",2628],["Big 12","texas",251],["Big 12","texas-tech",2641],["Big 12","west-virginia",277],["Big Ten","illinois",356],["Big Ten","indiana",84],["Big Ten","iowa",2294],["Big Ten","maryland",120],["Big Ten","michigan",130],["Big Ten","michigan-state",127],["Big Ten","minnesota",135],["Big Ten","nebraska",158],["Big Ten","northwestern",77],["Big Ten","ohio-state",194],["Big Ten","penn-state",213],["Big Ten","purdue",2509],["Big Ten","rutgers",164],["Big Ten","wisconsin",275],["Conference USA","fiu",2229],["Conference USA","florida-atlantic",2226],["Conference USA","louisiana-tech",2348],["Conference USA","marshall",276],["Conference USA","middle-tennessee",2393],["Conference USA","north-texas",249],["Conference USA","old-dominion",295],["Conference USA","rice",242],["Conference USA","southern-miss",2572],["Conference USA","utep",2638],["Conference USA","utsa",2636],["Conference USA","western-kentucky",98],["Division I FBS Independents","army",349],["Division I FBS Independents","brigham-young",252],["Division I FBS Independents","charlotte",2429],["Division I FBS Independents","notre-dame",87],["Division I FBS Independents","ua-birmingham",5],["Mid-American","akron",2006],["Mid-American","ball-state",2050],["Mid-American","bowling-green",189],["Mid-American","buffalo",2084],["Mid-American","central-michigan",2117],["Mid-American","eastern-michigan",2199],["Mid-American","kent-state",2309],["Mid-American","massachusetts",113],["Mid-American","miami-ohio",193],["Mid-American","northern-illinois",2459],["Mid-American","ohio",195],["Mid-American","toledo",2649],["Mid-American","western-michigan",2711],["Mountain West","air-force",2005],["Mountain West","boise-state",68],["Mountain West","colorado-state",36],["Mountain West","fresno-state",278],["Mountain West","hawaii",62],["Mountain West","nevada",2440],["Mountain West","new-mexico",167],["Mountain West","san-diego-state",21],["Mountain West","san-jose-state",23],["Mountain West","unlv",2439],["Mountain West","utah-state",328],["Mountain West","wyoming",2751],["Pac-12","arizona",12],["Pac-12","arizona-state",9],["Pac-12","california",25],["Pac-12","colorado",38],["Pac-12","oregon",2483],["Pac-12","oregon-state",204],["Pac-12","stanford",24],["Pac-12","ucla",26],["Pac-12","usc",30],["Pac-12","utah",254],["Pac-12","washington",264],["Pac-12","washington-state",265],["SEC","alabama",333],["SEC","arkansas",8],["SEC","auburn",2],["SEC","florida",57],["SEC","georgia",61],["SEC","kentucky",96],["SEC","lsu",99],["SEC","mississippi",145],["SEC","mississippi-state",344],["SEC","missouri",142],["SEC","south-carolina",2579],["SEC","tennessee",2633],["SEC","texas-am",245],["SEC","vanderbilt",238],["Sun Belt","appalachian-state",2026],["Sun Belt","arkansas-state",2032],["Sun Belt","coastal-carolina",324],["Sun Belt","georgia-southern",290],["Sun Belt","georgia-state",2247],["Sun Belt","idaho",70],["Sun Belt","louisiana-lafayette",309],["Sun Belt","louisiana-monroe",2433],["Sun Belt","new-mexico-state",166],["Sun Belt","south-alabama",6],["Sun Belt","texas-state",326],["Sun Belt","troy",2653],["The American","cincinnati",2132],["The American","connecticut",41],["The American","east-carolina",151],["The American","houston",248],["The American","memphis",235],["The American","navy",2426],["The American","southern-methodist",2567],["The American","south-florida",58],["The American","temple",218],["The American","tulane",2655],["The American","tulsa",202],["The American","ucf",2116]]
apmassey = [["ACC","boston-college",783],["ACC","clemson",1603],["ACC","duke",2265],["ACC","florida-state",2666],["ACC","georgia-tech",2911],["ACC","louisville",4224],["ACC","miami-fl",4719],["ACC","north-carolina",5492],["ACC","north-carolina-state",5511],["ACC","pittsburgh",6236],["ACC","syracuse",7729],["ACC","virginia",8432],["ACC","virginia-tech",8459],["ACC","wake-forest",8508],["Big 12","baylor",557],["Big 12","iowa-state",3554],["Big 12","kansas",3717],["Big 12","kansas-state",3731],["Big 12","oklahoma",5886],["Big 12","oklahoma-state",5912],["Big 12","tcu",7878],["Big 12","texas",7840],["Big 12","texas-tech",7918],["Big 12","west-virginia",8716],["Big Ten","illinois",3425],["Big Ten","indiana",3484],["Big Ten","iowa",3540],["Big Ten","maryland",4474],["Big Ten","michigan",4741],["Big Ten","michigan-state",4757],["Big Ten","minnesota",4858],["Big Ten","nebraska",5279],["Big Ten","northwestern",5704],["Big Ten","ohio-state",5850],["Big Ten","penn-state",6114],["Big Ten","purdue",6393],["Big Ten","rutgers",6696],["Big Ten","wisconsin",9031],["Conference USA","fiu",2652],["Conference USA","florida-atlantic",2638],["Conference USA","louisiana-tech",4218],["Conference USA","marshall",4436],["Conference USA","middle-tennessee",4785],["Conference USA","north-texas",5584],["Conference USA","old-dominion",5925],["Conference USA","rice",6535],["Conference USA","southern-miss",7365],["Conference USA","utep",7933],["Conference USA","utsa",7900],["Conference USA","western-kentucky",8761],["Division I FBS Independents","army",356],["Division I FBS Independents","brigham-young",891],["Division I FBS Independents","charlotte",8156],["Division I FBS Independents","notre-dame",5749],["Division I FBS Independents","ua-birmingham",87],["Mid-American","akron",66],["Mid-American","ball-state",501],["Mid-American","bowling-green",821],["Mid-American","buffalo",979],["Mid-American","central-michigan",1404],["Mid-American","eastern-michigan",2353],["Mid-American","kent-state",3771],["Mid-American","massachusetts",4548],["Mid-American","miami-ohio",4725],["Mid-American","northern-illinois",5634],["Mid-American","ohio",5825],["Mid-American","toledo",7978],["Mid-American","western-michigan",8767],["Mountain West","air-force",55],["Mountain West","boise-state",771],["Mountain West","colorado-state",1753],["Mountain West","fresno-state",2776],["Mountain West","hawaii",3197],["Mountain West","nevada",5316],["Mountain West","new-mexico",5371],["Mountain West","san-diego-state",7002],["Mountain West","san-jose-state",7024],["Mountain West","unlv",5323],["Mountain West","utah-state",8325],["Mountain West","wyoming",9162],["Pac-12","arizona",294],["Pac-12","arizona-state",304],["Pac-12","california",1098],["Pac-12","colorado",1715],["Pac-12","oregon",5961],["Pac-12","oregon-state",5970],["Pac-12","stanford",7582],["Pac-12","ucla",8141],["Pac-12","usc",8251],["Pac-12","utah",8315],["Pac-12","washington",8551],["Pac-12","washington-state",8588],["SEC","alabama",74],["SEC","arkansas",316],["SEC","auburn",402],["SEC","florida",2625],["SEC","georgia",2881],["SEC","kentucky",3781],["SEC","lsu",4206],["SEC","mississippi",4920],["SEC","mississippi-state",4936],["SEC","missouri",4948],["SEC","south-carolina",7242],["SEC","tennessee",7801],["SEC","texas-am",7848],["SEC","vanderbilt",8367],["Sun Belt","appalachian-state",275],["Sun Belt","arkansas-state",333],["Sun Belt","coastal-carolina",1637],["Sun Belt","georgia-southern",2899],["Sun Belt","georgia-state",2907],["Sun Belt","idaho",3415],["Sun Belt","louisiana-lafayette",4194],["Sun Belt","louisiana-monroe",4200],["Sun Belt","new-mexico-state",5387],["Sun Belt","south-alabama",7237],["Sun Belt","texas-state",7911],["Sun Belt","troy",8068],["The American","cincinnati",1529],["The American","connecticut",1872],["The American","east-carolina",2292],["The American","houston",3347],["The American","memphis",4636],["The American","navy",5253],["The American","southern-methodist",7358],["The American","south-florida",7278],["The American","temple",7788],["The American","tulane",8092],["The American","tulsa",8099],["The American", "ucf",1380]]
nameconvert = [['boston-college', 'Boston College'], ['clemson', 'Clemson'], ['duke', 'Duke'], ['florida-state', 'Florida State'], ['georgia-tech', 'Georgia Tech'], ['louisville', 'Louisville'], ['miami-fl', 'Miami (FL)'], ['north-carolina', 'North Carolina'], ['north-carolina-state', 'North Carolina State'], ['pittsburgh', 'Pittsburgh'], ['syracuse', 'Syracuse'], ['virginia', 'Virginia'], ['virginia-tech', 'Virginia Tech'], ['wake-forest', 'Wake Forest'], ['baylor', 'Baylor'], ['iowa-state', 'Iowa State'], ['kansas', 'Kansas'], ['kansas-state', 'Kansas State'], ['oklahoma', 'Oklahoma'], ['oklahoma-state', 'Oklahoma State'], ['tcu', 'TCU'], ['texas', 'Texas'], ['texas-tech', 'Texas Tech'], ['west-virginia', 'West Virginia'], ['illinois', 'Illinois'], ['indiana', 'Indiana'], ['iowa', 'Iowa'], ['maryland', 'Maryland'], ['michigan', 'Michigan'], ['michigan-state', 'Michigan State'], ['minnesota', 'Minnesota'], ['nebraska', 'Nebraska'], ['northwestern', 'Northwestern'], ['ohio-state', 'Ohio State'], ['penn-state', 'Penn State'], ['purdue', 'Purdue'], ['rutgers', 'Rutgers'], ['wisconsin', 'Wisconsin'], ['fiu', 'FIU'], ['florida-atlantic', 'Florida Atlantic'], ['louisiana-tech', 'Louisiana Tech'], ['marshall', 'Marshall'], ['middle-tennessee', 'Middle Tennessee'], ['north-texas', 'North Texas'], ['old-dominion', 'Old Dominion'], ['rice', 'Rice'], ['southern-miss', 'Southern Miss'], ['utep', 'UTEP'], ['utsa', 'UTSA'], ['western-kentucky', 'Western Kentucky'], ['army', 'Army'], ['ua-birmingham', 'UA-Birmingham'], ['brigham-young', 'Brigham Young'], ['charlotte', 'Charlotte'], ['notre-dame', 'Notre Dame'], ['akron', 'Akron'], ['ball-state', 'Ball State'], ['bowling-green', 'Bowling Green'], ['buffalo', 'Buffalo'], ['central-michigan', 'Central Michigan'], ['eastern-michigan', 'Eastern Michigan'], ['kent-state', 'Kent State'], ['massachusetts', 'Massachusetts'], ['miami-ohio', 'Miami (Ohio)'], ['northern-illinois', 'Northern Illinois'], ['ohio', 'Ohio'], ['toledo', 'Toledo'], ['western-michigan', 'Western Michigan'], ['air-force', 'Air Force'], ['boise-state', 'Boise State'], ['colorado-state', 'Colorado State'], ['fresno-state', 'Fresno State'], ['hawaii', 'Hawaii'], ['nevada', 'Nevada'], ['new-mexico', 'New Mexico'], ['san-diego-state', 'San Diego State'], ['san-jose-state', 'San Jose State'], ['unlv', 'UNLV'], ['utah-state', 'Utah State'], ['wyoming', 'Wyoming'], ['arizona', 'Arizona'], ['arizona-state', 'Arizona State'], ['california', 'California'], ['colorado', 'Colorado'], ['oregon', 'Oregon'], ['oregon-state', 'Oregon State'], ['stanford', 'Stanford'], ['ucla', 'UCLA'], ['usc', 'USC'], ['utah', 'Utah'], ['washington', 'Washington'], ['washington-state', 'Washington State'], ['alabama', 'Alabama'], ['arkansas', 'Arkansas'], ['auburn', 'Auburn'], ['florida', 'Florida'], ['georgia', 'Georgia'], ['kentucky', 'Kentucky'], ['lsu', 'LSU'], ['mississippi', 'Mississippi'], ['mississippi-state', 'Mississippi State'], ['missouri', 'Missouri'], ['south-carolina', 'South Carolina'], ['tennessee', 'Tennessee'], ['texas-am', 'Texas A&amp;M'], ['vanderbilt', 'Vanderbilt'], ['appalachian-state', 'Appalachian State'], ['arkansas-state', 'Arkansas State'], ['coastal-carolina', 'Coastal Carolina'], ['georgia-southern', 'Georgia Southern'], ['georgia-state', 'Georgia State'], ['idaho', 'Idaho'], ['louisiana-lafayette', 'Louisiana-Lafayette'], ['new-mexico-state', 'New Mexico State'], ['louisiana-monroe', 'Louisiana-Monroe'], ['south-alabama', 'South Alabama'], ['texas-state', 'Texas State'], ['troy', 'Troy'], ['cincinnati', 'Cincinnati'], ['connecticut', 'Connecticut'], ['east-carolina', 'East Carolina'], ['houston', 'Houston'], ['navy', 'Navy'], ['memphis', 'Memphis'], ['southern-methodist', 'Southern Methodist'], ['south-florida', 'South Florida'], ['tulane', 'Tulane'], ['temple', 'Temple'], ['tulsa', 'Tulsa'], ['ucf', 'UCF'], ['north-dakota-state', 'North Dakota State'], ['alabama', 'Alabama'], ['penn-state', 'Penn State'], ['georgia', 'Georgia'], ['tcu', 'TCU'], ['wisconsin', 'Wisconsin'], ['ohio-state', 'Ohio State'], ['clemson', 'Clemson'], ['miami-fl', 'Miami (FL)'], ['notre-dame', 'Notre Dame'], ['oklahoma', 'Oklahoma']]

def getranking(voterranks,week):
    masseyrankraw = readcsv('massey2017/masseyweek'+str(week-1)+'.csv')
    masseyranks = []
    for i in range(0,nteams):
        masseyranks.append(int(masseyrankraw[i][0]))
    myrank = []
    for i in voterranks:
        team = str(i)
        for ii in apmassey:
            if ii[1]==team:
                masseyranks.remove(ii[2])
                myrank.append(ii[2])
    for i in masseyranks:
        myrank.append(i)
    return myrank

def sse(x):
    tse = 0.
    nse = 0.
    for i in x:
        tse+=i**2.
        nse+=1.
    if nse==0:
        return 0.
    else:
        return tse*1./nse

def genbias(voter,this_week,apmassey,apgames):
    allranks = []
    for i in range(1,this_week+1):
        allvotes = readcsv('ap2017/week'+str(i)+'.csv')
        for ii in allvotes:
            if ii[0]==voter:
                voterranks = getranking(ii[1:],i)
                allranks.append(voterranks)

    teambias = []
    for i in apmassey:
        teambias.append([i[0],i[1],0])
    if this_week>0:
        for iiii in range(0,2):
            for week in range(1,this_week+1):
                myrank = allranks[week-1]
                teams = []
                for idx,ii in enumerate(myrank):
                    for idxbias,i in enumerate(apmassey):
                        if i[2]==ii:
                            teams.append([i[1],-4.160255889*(idx+1)**.5+102.8304061+teambias[idxbias][2]])
                if week != this_week:
                    for i in apgames:
                        if i[0]==week:
                            ateam = i[1][0]
                            hteam = i[1][1]
                            ateamrate = 55.
                            hteamrate = 55.
                            for ii in teams:
                                if ii[0]==ateam:
                                    ateamrate = ii[1]
                                    break
                            for ii in teams:
                                if ii[0]==hteam:
                                    hteamrate = ii[1]
                                    break
                            if i[4]==1:
                                if hteamrate>ateamrate:
                                    predoutcome = math.log(hteamrate-ateamrate+1)
                                else:
                                    predoutcome = -1.*math.log(-hteamrate+ateamrate+1)
                            else:
                                if hteamrate+2>ateamrate:
                                    predoutcome = math.log(hteamrate+2-ateamrate+1)
                                else:
                                    predoutcome = -1.*math.log(-hteamrate-2+ateamrate+1)
                            if int(i[3][1])>int(i[3][0]):
                                actoutcome = math.log(int(i[3][1])*1.+int(i[3][0])*-1.+1.)
                            else:
                                actoutcome = -1.*math.log(int(i[3][1])*-1.+int(i[3][0])*1.+1.)
                            for idx,ii in enumerate(teambias):
                                if ii[1]==ateam:
                                    teambias[idx].append(1.*(predoutcome-actoutcome))
                                    break
                            for idx,ii in enumerate(teambias):
                                if ii[1]==hteam:
                                    teambias[idx].append(-1.*(predoutcome-actoutcome))
                                    break
            if iiii==0:
                for idx, i in enumerate(teambias):
                    if sum(teambias[idx][3:])>0:
                        teambias[idx][2]=1.5**(sum(teambias[idx][3:])/len(teambias[idx][3:]))
                    elif sum(teambias[idx][3:])<0:
                        teambias[idx][2]=-1.*.667**(sum(teambias[idx][3:])/len(teambias[idx][3:]))
                    else:
                        teambias[idx][2]=0.

                    #if i[1]=='ohio-state':
                    #    print teambias[idx], sum(teambias[idx][3:]), len(teambias[idx][3:])
                    teambias[idx]=[teambias[idx][0],teambias[idx][1],teambias[idx][2]]
            else:
                for idx, i in enumerate(teambias):
                    if len(teambias[idx])>3:
                        teambias[idx][3]=sse(teambias[idx][3:])
                    else:
                        teambias[idx].append(0.)

                    myrank = allranks[this_week-1]
                    teams = []
                    for idxb,ii in enumerate(myrank):
                        for idxbias,ibias in enumerate(apmassey):
                            if ibias[2]==ii:
                                teams.append([ibias[1],-4.160255889*(idxb+1)**.5+102.8304061])
                    for ii in teams:
                        if ii[0]==i[1]:
                            if len(teambias[idx])>4:
                                teambias[idx][4]=ii[1]
                            elif len(teambias[idx])==4:
                                teambias[idx].append(ii[1])
                    
                    teambias[idx]=[teambias[idx][0],teambias[idx][1],teambias[idx][2],teambias[idx][3],teambias[idx][4]]


    return teambias

def createRank(my_week):
    allgames = readcsv('results.csv')
    apgames = []
    for game in allgames:
        if len(game)>4:
            gameday = game[3]
            mindex = gameday.find(' ',2)
            month = gameday[1:mindex]
            date = int(gameday[mindex+1:-1])
            week = 0
            if month=='Aug':
                week = 1
            elif month=='Sept':
                if date < 5:
                    week = 1
                elif date < 10:
                    week = 2
                elif date < 17:
                    week = 3
                elif date < 24:
                    week = 4
                elif date < 31:
                    week = 5
            elif month=='Oct':
                if date < 8:
                    week = 6
                elif date < 15:
                    week = 7
                elif date < 22:
                    week = 8
                elif date < 29:
                    week = 9
                elif date < 32:
                    week = 10
            elif month=='Nov':
                if date < 5:
                    week= 10
                elif date < 12:
                    week = 11
                elif date < 19:
                    week = 12
                elif date < 26:
                    week = 13
                elif date < 32:
                    week = 14
            elif month=='Dec':
                if date < 3:
                    week= 15
                else:
                    week = 16
            elif month=='Jan':
                week = 16
            ateam = 'FCS'
            aconf = 'FCS'
            hteam = 'FCS'
            hconf = 'FCS'
            for i in apconvert:
                if i[2]==int(game[0]):
                    ateam = i[1]
                    aconf = i[0]
                    break
            for i in apconvert:
                if i[2]==int(game[1]):
                    hteam = i[1]
                    hconf = i[0]
                    break
            if game[4].find(' ')>-1:
                game[4]=game[4][:game[4].find(' ')]
            if game[5].find(' ')>-1:
                game[5]=game[5][:game[5].find(' ')]
            donotadd = False
            nsite = 0
            for i in apgames:
                if i[0]==week and i[1]==[ateam,hteam]:
                    donotadd = True
                if i[0]==week and i[1]==[hteam,ateam]:
                    apgames.remove(i)
                    nsite = 1
            if not donotadd:
                apgames.append([week,[ateam,hteam],[aconf,hconf],[game[4],game[5]],nsite])

    allvoters = []
    allvotes = readcsv('ap2017/week1.csv')
    for i in allvotes:
        allvoters.append(i[0])

    for i in range(2,my_week+1):
        allvotes = readcsv('ap2017/week'+str(i)+'.csv')
        for ii in allvoters:
            voterin = False
            for iii in allvotes:
                if iii[0]==ii:
                    voterin = True
            if not voterin:
                allvoters.remove(ii)

    allvoterbias = []
    for voter in allvoters:
        allvoterbias.append(genbias(voter,my_week,apmassey,apgames))

    for voter in allvoterbias:
        confs = []
        for i in apmassey:
            if i[0] not in confs:
                confs.append([i[0],0,0,0])
        toterror = 0.
        for i in voter:
            toterror+=i[3]
            for idx,ii in enumerate(confs):
                if ii[0]==i[0]:
                    confs[idx][1]+=i[3]
                    confs[idx][2]+=i[2]
                    confs[idx][3]+=1

        for idx,i in enumerate(voter):
            for ii in confs:
                if ii[0]==i[0]:
                    voter[idx].append(ii[1]*1./ii[3])
                    voter[idx].append(ii[2]*1./ii[3])
                    voter[idx].append(toterror*1./nteams)




    top25 = []
    expweight = 1.0
    teambiaschg = 2.
    confbiaschg = 2.
    for i in apmassey:
        rating = 0
        adjrating = 0
        totalweight = 0
        tvoters = 0
        tbias = 0
        for voter in allvoterbias:
            for ii in voter:
                if ii[1]==i[1]:
                    totalweight += 1./(.000001+ii[3]**expweight+ii[5]**expweight+ii[7]**expweight)
                    tvoters += 1
        for voter in allvoterbias:
            for ii in voter:
                if ii[1]==i[1]:
                    rating += 1./tvoters*(ii[4])
                    adjrating += (1./(.000001+ii[3]**expweight+ii[5]**expweight+ii[7]**expweight))/totalweight*(ii[4]+ii[2]/teambiaschg+ii[6]/confbiaschg)
                    tbias += ii[2]/tvoters
        top25.append([i[1], rating, adjrating,tbias])

    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0,len(top25)-1):
            if top25[i][2]<top25[i+1][2]:
                holdit = top25[i]
                top25[i]=top25[i+1]
                top25[i+1]=holdit
                unsorted = True
    return top25

def unbiasedRank(my_week):
    allvoters = []
    allvotes = readcsv('ap2017/week1.csv')
    for i in allvotes:
        allvoters.append(i[0])

    for i in range(2,my_week+1):
        allvotes = readcsv('ap2017/week'+str(i)+'.csv')
        for ii in allvoters:
            voterin = False
            for iii in allvotes:
                if iii[0]==ii:
                    voterin = True
            if not voterin:
                allvoters.remove(ii)
    allvoterdata = []
    for voter in allvoters:
        allvotes = readcsv('ap2017/week'+str(my_week)+'.csv')
        for ii in allvotes:
            if ii[0]==voter:
                voterranks = getranking(ii[1:],my_week)
                allranks = voterranks
        allvoterdata.append(allranks)

    top25 = []
    for i in apmassey:
        rating = 0
        for voter in allvoterdata:
            for iidx,ii in enumerate(voter):
                if ii==i[2]:
                    rating += max(0,25-iidx)
        top25.append([i[1], rating, rating,0])

    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0,len(top25)-1):
            if top25[i][2]<top25[i+1][2]:
                holdit = top25[i]
                top25[i]=top25[i+1]
                top25[i+1]=holdit
                unsorted = True
    return top25

all_ranks = []
for my_week in range(1,int(this_week)+1):
    print my_week
    if my_week<6:
        top25ap = unbiasedRank(my_week)
        top25 = unbiasedRank(my_week)
    else:
        top25ap = unbiasedRank(my_week)
        top25 = createRank(int(my_week))
    all_ranks.append(top25)
    istr = 'top25 = ['
    for i in top25[:25]:
        teamname = i[0]
        for ii in apmassey:
            if ii[1]==teamname:
                confname = ii[0]
        for iidx,ii in enumerate(top25ap):
            if ii[0]==teamname:
                aprank = str(iidx+1)
        weightedpoints = str(i[2])
        for ii in nameconvert:
            if ii[0]==teamname:
                namename = ii[1]
        if str(confname).find('Independents')>-1:
            confname = 'Ind.'
        if str(confname).find('The American')>-1:
            confname = 'American'
        istr +='["'+namename+'","'+confname+'",'+weightedpoints+','+aprank+','+'['
        for iii in range(0,len(all_ranks)):
            for iiiidx,iiii in enumerate(all_ranks[iii]):
                if iiii[0]==teamname:
                    istr += str(26-min(iiiidx+1,26))+','
        istr = istr[:-1]+']],'
    istr = istr[:-1]+'];'

    


f = open('helloworld.txt','w')
f.write(istr+'\n')
f.close()
