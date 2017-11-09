import random
import csv

def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

alldata = readcsv('Game_Logs_Quarterback.csv')

allgames = []
qbids = []
qbnames = []
for i in alldata[1:]:
    if i[14]!= '--':
        try:
            if i[0].find('/')>-1:
                qbid = int(i[0][i[0].find('/')+1:])
            else:
                qbid = int(i[0])
        except:
            qbid = 0
        if qbid not in qbids:
            qbids.append(qbid)
            qbnames.append(i[1])

for i in range(0,len(qbids)):
    print str(qbids[i])+',"'+qbnames[i]+'",',


