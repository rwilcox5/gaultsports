import time
import random
import csv
import math

matched_abbrev = [['BOL','BOL'],['TKM','TKM'],['YEM','YEM'],['SOL','SLB'],['TLS','TLS'],['PLE','PSX'],['BIH','BIH'],['ALB','ALB'],['ESA','SLV'],['BHU','BTN'],['BAN','BGD'],['OMA','OMN'],['LAO','LAO'],['CAM','KHM'],['GEQ','GNQ'],['GBS','GNB'],['PNG','PNG'],['JOR','JOR'],['GUI','GIN'],['MTN','MRT'],['LAT','LVA'],['TOG','TGO'],['TPE','TWN'],['BAH','BHS'],['PUR','PRI'],['PHI','PHL'],['RU1','RUS'],['URS','RUS'],['TCH','CZE'],['SCG','SRB'],['YUG','SRB'],['EUA','DEU'],['EUN','DEU'],['FRG','DEU'],['GDR','DEU'],['BWI','JAM'],['ANZ','AUS'],['KSA','SAU'],['KUW','KWT'],['NEP','NPL'],['MGL','MNG'],['MAD','MDG'],['LES','LSO'],['VIE','VNM'],['VAN','VUT'],['LIB','LBN'],['NCA','NIC'],['BIZ','BLZ'],['SLO','SVN'],['SRI','LKA'],['HON','HND'],['MYA','MMR'],['MAS','MYS'],['INA','IDN'],['IRI','IRN'],['FIJ','FJI'],['CRO','HRV'],['GUA','GTM'],['HAI','HTI'],['URU','URY'],['SUD','SDN'],['SWZ','SWZ'],['NIG','NER'],['NGR','NGA'],['GAM','GMB'],['SLE','SLE'],['SOM','SOM'],['CHA','TCD'],['CHI','CHL'],['CRC','CRI'],['BUR','BFA'],['BUL','BGR'],['BEN','BEN'],['ZIM','ZWE'],['ZAM','ZMB'],['UAE','ARE'],['SUI','CHE'],['RSA','ZAF'],['RWA','RWA'],['PAR','PRY'],['POR','PRT'],['BOH','CZE'],['LBA','LBY'],['LBR','LBR'],['MLI','MLI'],['MAW','MWI'],['ALG','DZA'],['CAF','CAF'],['ANG','AGO'],['BOT','BWA'],['COD','COD'],['CGO','COG'],['TAN','TZA'],['NED','NLD'],['GRE','GRC'],['DEN','DNK'],['GER','DEU'],['HUN', 'HUN'], ['AUT', 'AUT'], ['USA', 'USA'], ['GBR', 'GBR'], ['FRA', 'FRA'], ['AUS', 'AUS'], ['BEL', 'BEL'], ['IND', 'IND'], ['CAN', 'CAN'], ['SWE', 'SWE'], ['NOR', 'NOR'], ['ESP', 'ESP'], ['ITA', 'ITA'], ['CUB', 'CUB'], ['FIN', 'FIN'], ['EST', 'EST'], ['NZL', 'NZL'], ['BRA', 'BRA'], ['JPN', 'JPN'], ['LUX', 'LUX'], ['ARG', 'ARG'], ['POL', 'POL'], ['ROU', 'ROU'], ['EGY', 'EGY'], ['IRL', 'IRL'], ['MEX', 'MEX'], ['TUR', 'TUR'], ['PAN', 'PAN'], ['JAM', 'JAM'], ['KOR', 'KOR'], ['PER', 'PER'], ['VEN', 'VEN'], ['ISL', 'ISL'], ['PAK', 'PAK'], ['ETH', 'ETH'], ['MAR', 'MAR'], ['GHA', 'GHA'], ['IRQ', 'IRQ'], ['TUN', 'TUN'], ['KEN', 'KEN'], ['UGA', 'UGA'], ['CMR', 'CMR'], ['PRK', 'PRK'], ['COL', 'COL'], ['THA', 'THA'], ['GUY', 'GUY'], ['CHN', 'CHN'], ['CIV', 'CIV'], ['DOM', 'DOM'], ['SYR', 'SYR'], ['SUR', 'SUR'], ['SEN', 'SEN'], ['DJI', 'DJI'], ['NAM', 'NAM'], ['QAT', 'QAT'], ['LTU', 'LTU'], ['ISR', 'ISR'], ['RUS', 'RUS'], ['UKR', 'UKR'], ['ECU', 'ECU'], ['BDI', 'BDI'], ['MOZ', 'MOZ'], ['CZE', 'CZE'], ['BLR', 'BLR'], ['KAZ', 'KAZ'], ['UZB', 'UZB'], ['SVK', 'SVK'], ['MDA', 'MDA'], ['GEO', 'GEO'], ['ARM', 'ARM'], ['AZE', 'AZE'], ['KGZ', 'KGZ'], ['MKD', 'MKD'], ['ERI', 'ERI'], ['SRB', 'SRB'], ['TJK', 'TJK'], ['AFG', 'AFG'], ['BRN', 'BRN'], ['TTO', 'TTO'], ['MNE', 'MNE'], ['CYP', 'CYP'], ['GAB', 'GAB']]
allabbrev = []
alldata = []


for i in matched_abbrev:
        if i[1] not in allabbrev:
                allabbrev.append(i[1])
                alldata.append(0)

                

istr = "      map_main({'"
for idx,i in enumerate(allabbrev[:-1]):
        istr += i
        istr += "':{'points':255-_sendColor("
        istr += str(idx)
        istr += "),'gold':(_sendGold("
        istr += str(idx)
        istr += ")/10000).toFixed(2),'silver':(_sendSilver("
        istr += str(idx)
        istr += ")/10000).toFixed(2),'bronze':(_sendBronze("
        istr += str(idx)
        istr += ")/10000).toFixed(2),'value':(_sendValue("
        istr += str(idx)
        istr += ")/10000).toFixed(2),'rank':_sendRank("
        istr += str(idx)
        istr += ")},'"
        

istr += allabbrev[-1]
istr += "':{'points':255-_sendColor("
istr += str(len(allabbrev)-1)
istr += "),'gold':(_sendGold("
istr += str(len(allabbrev)-1)
istr += ")/10000).toFixed(2),'silver':(_sendSilver("
istr += str(len(allabbrev)-1)
istr += ")/10000).toFixed(2),'bronze':(_sendBronze("
istr += str(len(allabbrev)-1)
istr += ")/10000).toFixed(2),'value':(_sendValue("
istr += str(len(allabbrev)-1)
istr += ")/10000).toFixed(2),'rank':_sendRank("
istr += str(len(allabbrev)-1)
istr += ")}});"
f = open('helloworld.txt','w')
f.write(istr)
f.close()
print soto

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

allmedals = readcsv('summer.csv')
for i in allmedals:
        if i[0]=='2012':
                if i[6]=='Men':
                        if i[5] in ['BAN']:
                                print i[5],i[2],i[3],i[7],i[8]

allsports = [[],[]]
for i in allmedals:
        if i[0]=='2012':
                if i[6]=='Men':
                        if i[2] not in allsports[1]:
                                allsports[1].append(i[2])
                elif i[6]=='Women':
                        if i[2] not in allsports[0]:
                                allsports[0].append(i[2])
                else:
                        print i[6]

print len(allsports[0]), len(allsports[1])

alldisp = [[],[]]
for i in allsports[0]:
        alldisp[0].append([])
for i in allsports[1]:
        alldisp[1].append([])

for i in allmedals:
        if i[0]=='2012':
                if i[6]=='Men':
                        for iidx,ii in enumerate(allsports[1]):
                                if ii==i[2]:
                                        if i[3] not in alldisp[1][iidx]:
                                                alldisp[1][iidx].append(i[3])

allevents = [[],[]]
for idx,i in enumerate(allsports[1]):
        allevents[1].append([])
        for ii in alldisp[1][idx]:
                allevents[1][idx].append([])

nevents = [[],[]]
for idx,i in enumerate(allsports[1]):
        nevents[1].append([])
        for ii in alldisp[1][idx]:
                nevents[1][idx].append(0)


sportlist = [0,4,1,5,2,3,9,6,6,3,2,7,2,2,3,8,9,9,4,5,3,5,8,2,1,3];
displist = [];
displist.append([])

allcountrymedals = []
for i in allmedals:
        if i[0]=='2012':
                if i[6]=='Men':
                        the_country = ''
                        for ii in matched_abbrev:
                                if i[5]==ii[0]:
                                        the_country = ii[1]
                        countryid = -1
                        for iidx,ii in enumerate(allabbrev):
                                if ii==the_country:
                                        countryid = iidx
                        medalid = -1
                        if i[8]=='Gold':
                                medalid = 2
                        if i[8]=='Silver':
                                medalid = 1
                        if i[8]=='Bronze':
                                medalid = 0
                        for iidx,ii in enumerate(allsports[1]):
                                sportid = iidx
                                if ii==i[2]:
                                        for iiidx, iii in enumerate(alldisp[1][iidx]):
                                                if iii==i[3]:
                                                        if i[7] not in allevents[1][iidx][iiidx]:
                                                                allevents[1][iidx][iiidx].append(i[7])
                                                                nevents[1][iidx][iiidx]+=1
                                                                if [sportid, iiidx, len(allevents[1][iidx][iiidx])-1, countryid,1,medalid] not in allcountrymedals:
                                                                        allcountrymedals.append([sportid, iiidx, len(allevents[1][iidx][iiidx])-1, countryid,1,medalid])
                                                        else:
                                                                for iiiidx, iiii in enumerate(allevents[1][iidx][iiidx]):
                                                                        if i[7]== iiii:
                                                                                if [sportid, iiidx, iiiidx, countryid,1,medalid] not in allcountrymedals:
                                                                                        allcountrymedals.append([sportid, iiidx, iiiidx, countryid,1,medalid])

editsport =[]
editsport.append(['Aquatics',[['Swimming','wSwimming'],['Diving','wDiving'],['10 KM Swim','wMarathonSwim'],['Water Polo','wPolo']]])
editsport.append(['Athletics',[['Sprints','wSprints'],['Distance','wDistance'],['Field','wField'],['Weight Lifting','wLifting'],['Jumps','wJumps'],['Walking','wWalking']]])
editsport.append(['Team',[['Basketball','wBasket'],['Football','wFoot'],['Handball','wHand'],['Hockey','wHockey'],['Volleyball','wVolley'],['Beach Volleyball','wBeach']]])
editsport.append(['Combat',[['Judo','wJudo'],['Taekwondo','wTaekwondo'],['Fencing','wFencing'],['Wrestling','wWrestling'],['Boxing','wBoxing']]])
editsport.append(['Weapons',[['Archery','wArchery'],['Pistol','wPistol'],['Rifle','wRifle'],['Skeet','wSkeet'],['Trap','wTrap']]])
editsport.append(['Raquet',[['Tennis','wTennis'],['Badminton','wBad'],['Table Tennis','wTT']]])
editsport.append(['Riding',[['Cycling','wCycling'],['Equestrian','wEquestrian']]])
editsport.append(['Gym',[['Events','wEvents'],['Team','wTeamGym'],['All-Around','wAround'],['Trampoline','wTramp']]])
editsport.append(['Multiple',[['Modern Pentathlon','wPentathlon'],['Triathlon','wTriathlon']]])
editsport.append(['Water',[['Canoe Slalom','wCanoeSlalom'],['Canoe Sprint','wCanoeSprint'],['Rowing','wRowing'],['Sailing','wSailing']]])

editsport.append(['Swimming',[['Backstroke','wBack'],['Breaststroke','wBreast'],['Butterfly','wButter'],['Freestyle','wFree'],['Medley','wMedley']]])
editsport.append(['Sprints',[['Sprints','wRuns'],['Hurdles','wHurdles'],['Relays','wRelays']]])
editsport.append(['Field',[['Decathlon','wDecathlon'],['Shot Put','wShot'],['Hammer Throw','wHammer'],['Discus Throw','wDiscus'],['Javelin','wJavelin'],['Pole Vault','wPole']]])
editsport.append(['Cycling',[['Track','wTrack'],['Road','wRoad'],['BMX','wBmx'],['Mountain Bike','wMountain']]])

istr = ''
for sportg in editsport[0:10]:
        for i in sportg[1]:
                
                istr += i[1]+' = document.getElementById("'+i[1]+'").value;\n'
f = open('helloworld.txt','w')
f.write(istr)
f.close()


istr =''
for sportg in editsport:
        istr += '<div class="row hiddenSport" id="edit'+sportg[0]+'">\n'
        for i in sportg[1]:
                istr += '<div class="two columns">\n'
                istr += '<label for="exampleEmailInput">'+i[0]+'</label>\n'
                istr += '<input class="u-full-width" id="'+i[1]+'" value="20"></input>\n'
                istr += '</div>\n'
        istr += '</div>\n'

f = open('helloworld.txt','w')
f.write(istr)
f.close()

eventtrans = []
for idx,i in enumerate(allsports[1]):
        for iidx, ii in enumerate(alldisp[1][idx]):
                for iiidx,iii in enumerate(allevents[1][idx][iidx]):
                        firstid = sportlist[idx]
                        secondid = -1
                        thirdid = iiidx
                        if ii in ['Swimming','Judo','Archery','Basketball','Tennis','Mountain Bike','Modern Pentathlon','Canoe Slalom']:
                                secondid = 0
                                if ii=='Mountain Bike':
                                        thirdid = 8
                        elif ii in ['Diving','Taekwondo','Football','Badminton','Dressage','Eventing','Jumping','Triathlon','Canoe Sprint']:
                                secondid = 1
                                if ii=='Eventing':
                                        thirdid +=1
                                elif ii=='Jumping':
                                        thirdid+=3
                        elif ii in ['Marathon swimming','Fencing','Handball','Table Tennis','Rowing']:
                                secondid = 2
                        elif ii in ['Water Polo','Weightlifting','Wrestling Freestyle','Hockey','Trampoline','Sailing']:
                                secondid = 3
                        elif ii in ['Boxing','Volleyball']:
                                secondid = 4
                        elif ii in ['Beach Volleyball']:
                                secondid = 5
                        elif ii=='Athletics' and iiidx in [1,2,4,7,8,9,10,13]:
                                secondid  =0
                                for iiiidx,iiii in enumerate([1,2,4,7,8,9,10,13]):
                                        if iiidx==iiii:
                                                thirdid = iiiidx
                        elif ii=='Athletics' and iiidx in [0,3,6,11,20]:
                                secondid  =1
                                for iiiidx,iiii in enumerate([0,3,6,11,20]):
                                        if iiidx==iiii:
                                                thirdid = iiiidx
                        elif ii=='Athletics' and iiidx in [14,15,16,18,21,22]:
                                secondid  =2
                                for iiiidx,iiii in enumerate([14,15,16,18,21,22]):
                                        if iiidx==iiii:
                                                thirdid = iiiidx
                        elif ii=='Athletics' and iiidx in [17,19,23]:
                                secondid  =4
                                for iiiidx,iiii in enumerate([17,19,23]):
                                        if iiidx==iiii:
                                                thirdid = iiiidx
                        elif ii=='Athletics' and iiidx in [5,12]:
                                secondid  =5
                                for iiiidx,iiii in enumerate([5,12]):
                                        if iiidx==iiii:
                                                thirdid = iiiidx
                        elif ii.find('Cycling')>-1:
                                secondid = 0
                        elif iii.find('Pistol')>-1:
                                secondid = 1
                        elif iii.find('Rifle')>-1:
                                secondid = 2
                        elif iii.find('Skeet')>-1:
                                secondid = 3
                        elif iii.find('Trap')>-1:
                                secondid = 4
                        elif ii=='Gymnastics Artistic':
                                if iiidx in [0,1,3,4,5,7]:
                                        secondid = 0
                                        for iiiidx,iiii in enumerate([0,1,3,4,5,7]):
                                                if iiidx==iiii:
                                                        thirdid = iiiidx
                                elif iiidx==2:
                                        secondid = 2
                                elif iiidx==6:
                                        secondid = 1
                        

                        eventtrans.append([[idx,iidx,iiidx], [firstid, secondid,thirdid]])


for idx,i in enumerate(allcountrymedals):
        for iiiii in eventtrans:
                if iiiii[0]==[i[0],i[1],i[2]]:
                        allcountrymedals[idx] = [iiiii[1][0], iiiii[1][1], iiiii[1][2],i[3],i[4],i[5]]


for idx,i in enumerate(allcountrymedals):
        maxv = 0
        for ii in allcountrymedals:
                if ii[0]==i[0] and ii[1]==i[1] and ii[2]>maxv:
                        maxv = ii[2]
        secondid = 0
        for ii in editsport[0:i[0]]:
                for iii in ii[1]:
                        secondid += 1

        allcountrymedals[idx] = [i[0], secondid+i[1], maxv,i[3],i[4],i[5]]


istr = 'int allmedals[] = {'
for i in allcountrymedals[:-1]:
        istr+= str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+','
i = allcountrymedals[-1]
istr += str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+'};'

countstr = 'int allcount[] = {'
for idx,i in enumerate(allabbrev[:-1]):
        countstr+=str(0)+','
countstr+=str(0)+'};'

gstr = 'int goldcount[] = {'
for idx,i in enumerate(allabbrev[:-1]):
        gstr+=str(0)+','
gstr+=str(0)+'};'


f = open('helloworld.txt','w')
f.write(istr+'\n'+'int nmedals = '+str(len(allcountrymedals))+';\n'+countstr+'\n'+gstr+'\n'+'int maxvalue = 0;'+'\n'+'int ncountries = '+str(len(allabbrev))+';\n')
f.close()

print len(allcountrymedals)
#for idx,i in enumerate(alldisp[1]):
#        print i, allsports[1][idx], nevents[1][idx]