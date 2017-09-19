import csv
allgamesa = []

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
					try:
						allgamesa.append(row)
					except:
						print row
		return allgamesa

allgamesa = readcsv('week3wip.csv')
voterdb = []
allvotes = []
for row in allgamesa:
	index = row[0].find('>')
	index2 = row[0].find('poll-voter')
	if index2 > -1:
		voterdb.append(allvotes)
		allvotes = [row[0][index+1:]]
	else:
		allvotes.append(row[0][index+1:])
voterdb.append(allvotes)
writecsv(voterdb[1:],'week3final.csv')