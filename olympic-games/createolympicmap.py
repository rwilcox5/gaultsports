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
                the_country = ''
                for ii in matched_abbrev:
                        if i[5]==ii[0]:
                                the_country = ii[1]
                countryid = -1
                for iidx,ii in enumerate(allabbrev):
                        if ii==the_country:
                                countryid = iidx
                if countryid > -1:
                        alldata[countryid]+=1


for idx,i in enumerate(allabbrev):
        print 'g_map_stateMap["'+i+'"].myBaseRGB = [255,'+str(255-int(15.*math.sqrt(alldata[idx]+0.)))+','+str(255-int(15.*math.sqrt(alldata[idx]+0.)))+'];'

