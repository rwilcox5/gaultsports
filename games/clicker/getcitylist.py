import time
import random
import csv
import math
import threading
from threading import Thread

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

rawcities = readcsv('citypopulations.csv')

raw_str = ''
for i in rawcities:
        raw_str += i[2]+','
        raw_str += i[3]
        raw_str += '\n'

f = open('citystatepop.csv','w')
f.write(raw_str)
f.close()

csp = readcsv('citystatepop.csv')
allcities = []
state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
city_types = [' city', ' town', ' municipality', ' borough', ' village', ' government', ' county', ' corporation']

for i in csp:
        try:
                for ii in city_types:
                        i[0] = i[0].replace(ii,'')
                if int(i[2])>999:
                        allcities.append([i[0],i[1][1:],int(i[2])])
        except:
                pass
def getKey(item):
        return -1*item[2]

for iii in range(39,60):
        sd = readcsv('finalstatepops.csv')
        state_done = []
        for i in sd:
                state_done.append(i[0])

        csv_str = []
        for i in state_list:
                if i not in state_done:
                        topcities = []
                        for ii in allcities:
                                if ii[1]==i:
                                        topcities.append(ii)
                        topcities = sorted(topcities,key=getKey)
                        try:
                                pop50 = topcities[iii][2]
                        except:
                                pop50 = 200
                        statecities = []
                        for ii in topcities:
                                if ii[2]>5*pop50:
                                        statecities.append([ii[0],ii[2]/5])
                                        statecities.append(['E. '+ii[0],ii[2]/5])
                                        statecities.append(['W. '+ii[0],ii[2]/5])
                                        statecities.append(['N. '+ii[0],ii[2]/5])
                                        statecities.append(['S. '+ii[0],ii[2]/5])
                                        statecities.append(['NE '+ii[0],ii[2]/5])
                                        statecities.append(['NW '+ii[0],ii[2]/5])
                                        statecities.append(['SE '+ii[0],ii[2]/5])
                                        statecities.append(['SW '+ii[0],ii[2]/5])
                                elif ii[2]>4*pop50:
                                        statecities.append([ii[0],ii[2]/4])
                                        statecities.append(['E. '+ii[0],ii[2]/4])
                                        statecities.append(['W. '+ii[0],ii[2]/4])
                                        statecities.append(['N. '+ii[0],ii[2]/4])
                                        statecities.append(['S. '+ii[0],ii[2]/4])
                                elif ii[2]>3*pop50:
                                        statecities.append([ii[0],ii[2]/3])
                                        statecities.append(['E. '+ii[0],ii[2]/3])
                                        statecities.append(['W. '+ii[0],ii[2]/3])
                                        statecities.append(['S. '+ii[0],ii[2]/3])
                                elif ii[2]>2*pop50:
                                        statecities.append(['E. '+ii[0],ii[2]/2])
                                        statecities.append(['W. '+ii[0],ii[2]/2])
                                elif ii[2]>pop50:
                                        statecities.append([ii[0],ii[2]])
                                        statecities.append(['N. '+ii[0],ii[2]])

                        if len(statecities)>95 and len(statecities)<120:
                                state_array = [i]
                                for ii in statecities:
                                        state_array.append(ii[0])
                                csv_str.append(state_array)
                                state_done.append(i)
                        else:
                                print iii, i, len(statecities)
        

        writecsv(csv_str,'finalstatepops.csv')
print state_done, len(state_done)