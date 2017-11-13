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
pid = sys.argv[1]

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
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

allpitchdata = readcsv('pitch_table.csv')[1:]


if int(pid) == 0:
        allnamedata = readcsv('master.csv')
        all_pitcher_ids = []
        for idx,i in enumerate(allpitchdata):
                try:
                        if int(i[18]) not in all_pitcher_ids:
                                all_pitcher_ids.append(int(i[18]))
                except:
                        pass
        all_batter_ids = []
        for idx,i in enumerate(allpitchdata):
                try:
                        if int(i[19]) not in all_batter_ids:
                                all_batter_ids.append(int(i[19]))
                except:
                        pass
        f = open('gen-pitch-charts.sh','w')
        bashstr = '#!/bin/bash\nfor i in '
        for pitcher_id in all_pitcher_ids:
                bashstr += str(pitcher_id)+' '
        bashstr += '\ndo\n    python extract_pitch_data.py $i\ndone'
        f.write(bashstr)
        f.close()

        f = open('helloworld.txt','w')
        istr= 'pitcher_ids = ['
        iistr = 'pitcher_games = ['
        iiistr= 'pitcher_names = ['
        bstr ='batter_ids = ['
        bbstr = 'batter_names = ['
        tgames = 0
        for pitcher_id in all_pitcher_ids:
                pidgamelist = []
                for idx,i in enumerate(allpitchdata):
                        if str(i[18])==str(pitcher_id):
                                if i[0] not in pidgamelist:
                                        pidgamelist.append(i[0])
                istr += str(pitcher_id)+','+str(tgames)+','
                for pidgame in pidgamelist:
                        iistr += str(pidgame[3:7])+','+str(int(pidgame[7:9]))+','+str(int(pidgame[9:11]))+','
                        tgames+=1
                istr += str(tgames)+','
                for ii in allnamedata:
                        if str(ii[0])==str(pitcher_id):
                                iiistr += "'"+str(ii[1])+"',"
        for batter_id in all_batter_ids:
                bstr += str(batter_id)+','
                for ii in allnamedata:
                        if str(ii[0])==str(batter_id):
                                bname = str(ii[1])
                                bindex = bname.find(' ')
                                if bindex > -1:
                                        bname = bname[:1]+'.'+bname[bindex:min(bindex+11,len(bname))]
                                bbstr += "'"+bname+"',"
        istr = istr[:-1]+'];'
        iistr = iistr[:-1]+'];'
        iiistr = iiistr[:-1]+'];'
        bstr = bstr[:-1]+'];'
        bbstr = bbstr[:-1]+'];'
        f.write(istr+'\n'+iistr+'\n'+iiistr+'\n'+bstr+'\n'+bbstr+'\n'+'npitchers = '+str(len(all_pitcher_ids))+';')
        f.close()
        print soto
print pid

pidgamelist = []
for idx,i in enumerate(allpitchdata):
        if str(i[18])==str(pid):
                if i[0] not in pidgamelist:
                        pidgamelist.append(i[0])

for pidgame in pidgamelist:
        allpitches = []
        istr = 'var allpitches = ['
        abstr = 'var allabs = ['
        nabs = 0
        pididx = 0
        for idx,i in enumerate(allpitchdata):
                if str(i[18])==str(pid) and str(i[0])==str(pidgame):
                        allpitches.append([i[57],i[32],i[37],i[43],i[44],i[39],i[40]])
                        if i[57] in ['FA','FF','FT','FC','FS','SI','SF']:
                                ptype = 1
                        elif i[57] in ['CU','KC','CB']:
                                ptype = 2
                        elif i[57]=='SL':
                                ptype = 3
                        elif i[57]=='CH':
                                ptype = 4
                        else:
                                ptype = 5
                        if i[32] in ['F','S','X']:
                                swing = 1
                        else:
                                swing = 0
                        if i[32] in ['B']:
                                strike = 0
                        else:
                                strike = 1
                        if i[43]=='':
                                i[43]=0
                        if i[44]=='':
                                i[44]=0
                        xcoord = 60/(1.416)*(float(i[43])+.708)+20.
                        if xcoord<0:
                                xcoord = 0
                        elif xcoord>100:
                                xcoord = 100
                        else:
                                xcoord = int(xcoord)
                        szh = float(i[39])-float(i[40])
                        ycoord = 60./szh*(float(i[44])-float(i[40]))+20.
                        if ycoord<0:
                                ycoord = 0
                        elif ycoord>100:
                                ycoord = 100
                        else:
                                ycoord = int(ycoord)
                        ycoord=100-ycoord

                        istr+= str(ptype*100+strike*10+swing)+','+str(xcoord)+','+str(ycoord)+','+str(i[41])+','+str(i[42])+','+str(i[37])+','
                        if idx > 0:
                                if i[31]!=allpitchdata[idx-1][31]:
                                        abstr += str(pididx)+','+i[27]+','+i[19]+','+str(i[13])+','
                                        nabs+=1
                        else:
                                abstr += str(0)+','+i[27]+','+i[19]+','+str(i[13])+','
                                nabs+=1
                        pididx += 1



        istr = istr[:-1]+'];'
        abstr += str(pididx)+',0,0,0];'

        #writecsv(allpitches,'my_pitch_data.csv')
        reststr = 'var nabsc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];\nvar returnabs = [];\nfor (i=0;i<200;i++){returnabs.push(0);}\nfunction getData(){\nvar i; var iii = 0; var iiii;\nfor (i=0;i<num_abs;i++){\nif (iii<100){\nif (2==2){\nreturnabs[2*iii]=i*4;returnabs[2*iii+1]=i*4+4;for (iiii=allabs[i*4+3];iiii<30;iiii++){        nabsc[iiii]+=1;}\niii++;}}}\nreturn iii;}\nfunction sendAb(i){\nreturn allabs[returnabs[2*i+1]]-allabs[returnabs[2*i]];\n}\nfunction sendAge(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*6];\n}\nfunction sendX(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*6+1];\n}\nfunction sendY(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*6+2];\n}\nfunction sendXM(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*6+3];\n}\nfunction sendYM(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*6+4];\n}\nfunction sendVel(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*6+5];\n}\nfunction sendInn(i){\n        return nabsc[i];\n}\nfunction sendBatter(i){\n        var abn = returnabs[2*i];\n        return allabs[abn+2];\n}\nfunction sendEvent(i){var abn = returnabs[2*i]; return allabs[abn+1];}'

        f = open('../../gaultsports-site/mlb/pitchers/pitch-charts-'+str(pid)+'-'+str(pidgame[3:7])+'-'+str(pidgame[7:9])+'-'+str(pidgame[9:11])+'.js','w')
        f.write(istr+'\n'+abstr+'\n'+'var num_abs = '+str(nabs)+';\n'+reststr)
        f.close()

bidlist = []
for idx,i in enumerate(allpitchdata):
        if str(i[18])==str(pid):
                if i[19] not in bidlist:
                        bidlist.append(i[19])

for bid in bidlist:
        allpitches = []
        istr = 'var allpitches = ['
        abstr = 'var allabs = ['
        nabs = 0
        pididx = 0
        gamelist = []
        for idx,i in enumerate(allpitchdata):
                if str(i[18])==str(pid) and str(i[19])==str(bid):
                        alreadyin = False
                        for iidx,ii in enumerate(gamelist):
                                if ii==i[0]:
                                        game_id = iidx+1
                                        alreadyin = True
                        if not alreadyin:
                                game_id = len(gamelist)+1
                                gamelist.append(i[0])

                        allpitches.append([i[57],i[32],i[37],i[43],i[44],i[39],i[40]])
                        if i[57] in ['FA','FF','FT','FC','FS','SI','SF']:
                                ptype = 1
                        elif i[57] in ['CU','KC','CB']:
                                ptype = 2
                        elif i[57]=='SL':
                                ptype = 3
                        elif i[57]=='CH':
                                ptype = 4
                        else:
                                ptype = 5
                        if i[32] in ['F','S','X']:
                                swing = 1
                        else:
                                swing = 0
                        if i[32] in ['B']:
                                strike = 0
                        else:
                                strike = 1
                        if i[43]=='':
                                i[43]=0
                        if i[44]=='':
                                i[44]=0
                        xcoord = 60/(1.416)*(float(i[43])+.708)+20.
                        if xcoord<0:
                                xcoord = 0
                        elif xcoord>100:
                                xcoord = 100
                        else:
                                xcoord = int(xcoord)
                        szh = float(i[39])-float(i[40])
                        ycoord = 60./szh*(float(i[44])-float(i[40]))+20.
                        if ycoord<0:
                                ycoord = 0
                        elif ycoord>100:
                                ycoord = 100
                        else:
                                ycoord = int(ycoord)
                        ycoord=100-ycoord

                        istr+= str(ptype*100+strike*10+swing)+','+str(xcoord)+','+str(ycoord)+','
                        if idx > 0:
                                if i[31]!=allpitchdata[idx-1][31]:
                                        abstr += str(pididx)+','+i[0][3:]+','+i[27]+','+str(i[13])+','+str(game_id)+','
                                        nabs+=1
                        else:
                                abstr += str(0)+','+i[0][3:]+','+i[27]+','+str(i[13])+','+str(game_id)+','
                                nabs+=1
                        pididx += 1



        istr = istr[:-1]+'];'
        abstr += str(pididx)+',0,0,0];'

        #writecsv(allpitches,'my_pitch_data.csv')
        reststr = 'var nabsc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];\nvar returnabs = [];\nfor (i=0;i<200;i++){returnabs.push(0);}\nfunction getData(){\nvar i; var iii = 0; var iiii;\nfor (i=0;i<num_abs;i++){\nif (iii<100){\nif (2==2){\nreturnabs[2*iii]=i*5;returnabs[2*iii+1]=i*5+5;for (iiii=allabs[i*5+4];iiii<30;iiii++){        nabsc[iiii]+=1;}\niii++;}}}\nreturn iii;}\nfunction sendAb(i){\nreturn allabs[returnabs[2*i+1]]-allabs[returnabs[2*i]];\n}\nfunction sendAge(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*3];\n}\nfunction sendX(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*3+1];\n}\nfunction sendY(i, ii){\n        var firstp = allabs[returnabs[2*i]];\n        return allpitches[(firstp+ii)*3+2];\n}\nfunction sendInn(i){\n        return nabsc[i];\n}\nfunction sendEvent(i){\n        var abn = returnabs[2*i];\n        return allabs[abn+2];\n}\nfunction sendDate(i){var abn = returnabs[2*i]; return allabs[abn+1];}'

        f = open('../../gaultsports-site/mlb/pitchers/pitch-charts-vb-'+str(pid)+'-'+str(bid)+'.js','w')
        f.write(istr+'\n'+abstr+'\n'+'var num_abs = '+str(nabs)+';\n'+reststr)
        f.close()