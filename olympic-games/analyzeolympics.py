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
        istr += "':{'points':255-sendValue("
        istr += str(idx)
        istr += "),'gold':sendGold("
        istr += str(idx)
        istr += "),'silver':"
        istr += str(2)
        istr += ",'bronze':"
        istr += str(1)
        istr += "},'"
        

istr += allabbrev[-1]
istr += "':{'points':255-sendValue("
istr += str(len(allabbrev)-1)
istr += "),'gold':"
istr += str(4)
istr += ",'silver':"
istr += str(2)
istr += ",'bronze':"
istr += str(1)
istr += "}});"
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
                                if ii==i[2]:
                                        for iiidx, iii in enumerate(alldisp[1][iidx]):
                                                if iii==i[3]:
                                                        if i[7] not in allevents[1][iidx][iiidx]:
                                                                allevents[1][iidx][iiidx].append(i[7])
                                                                nevents[1][iidx][iiidx]+=1
                                                                if [iidx, iiidx, len(allevents[1][iidx][iiidx])-1, countryid,1,medalid] not in allcountrymedals:
                                                                        allcountrymedals.append([iidx, iiidx, len(allevents[1][iidx][iiidx])-1, countryid,1,medalid])
                                                        else:
                                                                for iiiidx, iiii in enumerate(allevents[1][iidx][iiidx]):
                                                                        if i[7]== iiii:
                                                                                if [iidx, iiidx, iiiidx, countryid,1,medalid] not in allcountrymedals:
                                                                                        allcountrymedals.append([iidx, iiidx, iiiidx, countryid,1,medalid])

istr = 'int allmedals[] = {'
for i in allcountrymedals[:-1]:
        istr+= str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+','
i = allcountrymedals[-1]
istr += str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+'};'

cstr = 'int allcountries[] = {'
countstr = 'int allcount[] = {'
for idx,i in enumerate(allabbrev[:-1]):
        cstr+=str(idx)+','
        countstr+=str(0)+','

cstr+=str(len(allabbrev)-1)+'};'
countstr+=str(0)+'};'



f = open('helloworld.txt','w')
f.write(istr+'\n'+'int nmedals = '+str(len(allcountrymedals))+';\n'+cstr+'\n'+countstr)
f.close()

print len(allcountrymedals)
#for idx,i in enumerate(alldisp[1]):
#        print i, allsports[1][idx], nevents[1][idx]