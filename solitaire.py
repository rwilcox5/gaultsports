import random

thedeck = []
for i in range(0,52):
    thecard = []
    thecard.append(i%13+1)
    thecard.append(i%4)
    thedeck.append(thecard)
print thedeck

columns = []
for i in range(0,7):
    tcol = []
    for ii in range(0,i+1):
        randomcard = random.randint(0,len(thedeck)-1)
        tcard = thedeck[randomcard]
        if i==ii:
            thecard = [tcard[0],tcard[1],1]
        else:
            thecard = [tcard[0],tcard[1],0]
        tcol.append(thecard)
        thedeck.remove(tcard)
    
    columns.append(tcol)

tdeck = []
for i in range(0,24):
    randomcard = random.randint(0,len(thedeck)-1)
    tdeck.append(thedeck[randomcard])
    thedeck.remove(thedeck[randomcard])

thedeck = tdeck

toprow = [0,0,0,0]

def movecards(x,y,columns,i=0):
    maxi = 0
    for i in range(0,len(columns[x])):
        if columns[x][i][2]==0:
            maxi = maxi+1
            
    columns[y]=columns[y]+columns[x][maxi:]
    columns[x]=columns[x][:maxi]
    return columns

def flipcard(x,columns):
    if len(columns[x])>0:
        columns[x][len(columns[x])-1][2]=1
    return columns

def uptotop(x,columns,toprow):
    stotop = columns[x][len(columns[x])-1][1]
    toprow[stotop] = toprow[stotop]+1
    columns[x]=columns[x][:len(columns[x])-1]
    
    return columns, toprow

def deal(i,thedeck):
    if len(thedeck)>i+3:
        i=i+3
    else:
        i = len(thedeck)-1
    return i

def downfromdeal(x,columns,thedeck,i):
    columns[x]=columns[x]+[thedeck[i]]
    thedeck.remove(thedeck[i])
    if i>0:
        i=i-1
    return columns, thedeck, i
    
    
def upfromdeal(thedeck,toprow,i):
    stotop = thedeck[i][1]
    toprow[stotop] = toprow[stotop]+1
    thedeck.remove(thedeck[i])
    if i>0:
        i=i-1
    return thedeck,toprow,i
def dispcolumns(columns):
    for ii in range(0,20):
        iscard=True
        for i in range(0,7):
            if len(columns[i])>ii:
                if columns[i][ii][2]==1:
                    iscard=False
                    if columns[i][ii][0]>9:
                        cc0 = ""+str(columns[i][ii][0])
                        cc1 = columns[i][ii][1]
                        print [cc0,cc1],
                    else:
                        cc0 = " "+str(columns[i][ii][0])
                        cc1 = columns[i][ii][1]
                        print [cc0,cc1],
                else:
                    iscard=False
                    print '---------',
            else:
                
                print '         ',
        print ""
        if iscard:
            break
            
dispcolumns(columns)

#columns, toprow = uptotop(4,columns,toprow)

print thedeck
#columns, thedeck, i = downfromdeal(3,columns,thedeck,5)

#thedeck, toprow, i = upfromdeal(thedeck,toprow, 7)
i=-1
for iiii in range(0,10):
    moved = True
    while moved:
        moved = False
        #Flip unknown card
        for ii in range(0,7):
            if len(columns[ii])>0:
                if columns[ii][len(columns[ii])-1][0]==toprow[columns[ii][len(columns[ii])-1][1]]+1:
                    columns, toprow = uptotop(ii,columns,toprow)
                    columns = flipcard(ii,columns)
                    dispcolumns(columns)
                    print toprow
                    moved = True
                    break
                
        for ii in range(0,7):
            maxi = 0
            for iii in range(0,len(columns[ii])):
                if columns[ii][iii][2]==0:
                    maxi = maxi+1
            for iii in range(0,7):
                if len(columns[ii])>0 and len(columns[iii])>0:
                    if columns[ii][maxi][0]==columns[iii][len(columns[iii])-1][0]-1:
                        if columns[ii][maxi][1]%2!=columns[iii][len(columns[iii])-1][1]%2:
                            columns = movecards(ii,iii,columns,i=0)
                            columns = flipcard(ii,columns)
                            dispcolumns(columns)
                            print toprow
                            moved = True
                            break
    if i < len(thedeck)-1:
        i = deal(i,thedeck)
    else:
        i = -1
        i = deal(i,thedeck)
    for ii in range(0,7):
        if len(columns[ii])>0:
            if thedeck[i][0]==columns[ii][len(columns[ii])-1][0]-1:
                if thedeck[i][1]%2!=columns[ii][len(columns[ii])-1][1]%2:
                    columns,thedeck,i = downfromdeal(ii,columns,thedeck,i)
                    columns[ii][len(columns[ii])-1].append(1)
            


dispcolumns(columns)
print toprow
