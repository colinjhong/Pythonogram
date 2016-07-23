##Pythonogram
import random
import datetime

master=[]
scratch=[]
row_tomo=[]
rows=6
columns=6

##generates master list according to 'rows' and 'columns' values
for i in range(rows):
    masterRow=[]
    for j in range(columns):
        x=random.randint(0,2)
        if x==0:
            masterRow.append(0)
        else:
            masterRow.append(1)
##row_tomo starts to create hints for rows
    tomo=''.join(str(k) for k in masterRow)
    tomo=tomo.split('0')
    row_tomo.append(tomo)
    master.append(masterRow)

##number of X's in puzzle (for accuracy %)
answerCount=0
for i in master:
    answerCountindiv=i.count(1)
    answerCount+=answerCountindiv

##creates row hints
tomoPrint=[]

for i in range(rows):
    tomoPrintList=[]
    for j in row_tomo[i]:
        tomoPrintInt=j.count('1', 0, len(j))
        tomoPrintList.append(tomoPrintInt)
    tomoPrint.append(tomoPrintList)
    
##removes 0's from row hints
for i in range(rows):
    tomoPrintCount=tomoPrint[i].count(0)
    for j in range(tomoPrintCount):
        tomoPrint[i].remove(0)
##finished row hints

##creates column hints
tomoPrint2Draft=[]

for i in range(columns):
    column_tomo=[]    
    columnCount=0
##columnCount will be the hint numbers, columnCount +1 if 1,
##append current value and reset columnCount to 0 if 0
    for j in range(rows):
        if master[j][i]==1:
            columnCount+=1
        elif master[j][i]==0:
            column_tomo.append(columnCount)
            columnCount=0
##tells it to append and reset at the last row value
        if j==(rows-1):
            column_tomo.append(columnCount)
            columnCount=0
    tomoPrint2Draft.append(column_tomo)

##removes 0's from column hints
for i in range(columns):
    tomoPrint2Count=tomoPrint2Draft[i].count(0)
    for j in range(tomoPrint2Count):
        tomoPrint2Draft[i].remove(0)

##generates scratch list according to 'rows' and 'columns' values
for i in range(rows):
    scratchRow=[]
    for j in range(columns):
        scratchRow.append(0)
    scratch.append(scratchRow)

##generates scratch board according to 'rows' and 'columns' values
##top row with column numbers
for i in range(columns):
    if i==0:
        print('    ',end='')
    print(i,'  ',end='',)
print('\n','  ','+','---+'*columns, sep='')
##rest of board with row hints
for i in range(rows):
    print(i,'|', end='')
    for j in range(columns):
        if scratch[i][j]==0:
            print('   ','|', sep='', end='')
        if scratch[i][j]!=0:
            print(' ','X',' ','|', sep='', end='')
    for k in tomoPrint[i]:
        print(k,' ', end='')
    print('\n','  ','+','---+'*columns, sep='')

##formatting column hints
##finds the length of the largest column
max_column = 0

for i in tomoPrint2Draft:
    length=(len(i))
    if length>max_column:
        max_column=length

for i in range(max_column):
    if rows>=columns:
        for j in range(rows):
##formatting
            if j==0 and i==0:
                print('    ',end='')
            elif j==0:
                print('\n    ',end='')
                
##print the data
            if rows==columns:
                sublist=tomoPrint2Draft[j]
                if i<len(sublist):
                    value=sublist[i]
                else:
                    value=' '
                print(value,'  ',end='')
##for rectangular puzzles with more rows than columns
            if rows>columns:
                if j<columns:
                    sublist=tomoPrint2Draft[j]
                    if i<len(sublist):
                        value=sublist[i]
                    else:
                        value=' '
                    print(value,'  ',end='')
                else:
                    continue
##for rectangular puzzles with more columns than rows
    if columns>rows:
        for j in range(rows):
##formatting
            if j==0 and i==0:
                print('    ',end='')
            elif j==0:
                print('\n    ',end='')
##printing the data
        for j in range(columns):
            sublist=tomoPrint2Draft[j]
            if len(sublist)<1:
                value=' '
            elif i<len(sublist):
                value=sublist[i]
            else:
                value=' '
            print(value,'  ',end='')
print('\n')

##user input for guesses
x=datetime.datetime.now()
userGuessCount=0
response=['WOW GREAT JOB!!!', "YOU'RE A STAR!", 'Your mother would be proud.',
          'Daaaaaaamn, Daniel!', 'Back at it again with the white Vans!',
          'Daaaaaaamn, Daniel!']
response2=['Are you serious?', 'Please try again.', "That wasn't even close honestly.",
           'Damn, Daniel. (not in a good way)', "It's okay. This is a little challenging. Maybe take a break. Grab a snack. Come back to it later.",
           'PLEASE CAN YOU JUST FINISH THIS PUZZLE ALREADY.']
while True:
    userGuess=input('Enter guess (row,column): ')
    userGuessCount+=1
    userGuess=userGuess.split(',')
    userGuessRow=int(userGuess[0])
    userGuessCol=int(userGuess[1])
    if master[userGuessRow][userGuessCol]==1:
        if scratch[userGuessRow][userGuessCol]==1:
            print("You've already guessed that. Please try harder. It's like you don't even care.")
        if scratch[userGuessRow][userGuessCol]==0:
            scratch[userGuessRow][userGuessCol]=1
            print(response[random.randint(0,5)])
            ##generates scratch board according to 'rows' and 'columns' values
            ##top row with column numbers
            for i in range(columns):
                if i==0:
                    print('    ',end='')
                print(i,'  ',end='',)
            print('\n','  ','+','---+'*columns, sep='')
            ##rest of board with row hints
            for i in range(rows):
                print(i,'|', end='')
                for j in range(columns):
                    if scratch[i][j]==0:
                        print('   ','|', sep='', end='')
                    if scratch[i][j]!=0:
                        print(' ','X',' ','|', sep='', end='')
                for k in tomoPrint[i]:
                    print(k,' ', end='')
                print('\n','  ','+','---+'*columns, sep='')

            ##column hints
            # find the length of the largest column
            max_column = 0

            for i in tomoPrint2Draft:
                length=(len(i))
                if length>max_column:
                    max_column=length

            for i in range(max_column):
                if rows>=columns:
                    for j in range(rows):
                        ##formatting
                        if j==0 and i==0:
                            print('    ',end='')
                        elif j==0:
                            print('\n    ',end='')
                            
                        ##print the data
                        if rows==columns:
                            sublist=tomoPrint2Draft[j]
                            if i<len(sublist):
                                value=sublist[i]
                            else:
                                value=' '
                            print(value,'  ',end='')
                ##for rectangular puzzles
                        if rows>columns:
                            if j<columns:
                                sublist=tomoPrint2Draft[j]
                                if i<len(sublist):
                                    value=sublist[i]
                                else:
                                    value=' '
                                print(value,'  ',end='')
                            else:
                                continue
                if columns>rows:
                    for j in range(rows):
                    ##formatting
                        if j==0 and i==0:
                            print('    ',end='')
                        elif j==0:
                            print('\n    ',end='')
                    ##printing the data
                    for j in range(columns):
                        sublist=tomoPrint2Draft[j]
                        if len(sublist)<1:
                            value=' '
                        elif i<len(sublist):
                            value=sublist[i]
                        else:
                            value=' '
                        print(value,'  ',end='')
            print('\n')
            if master==scratch:
                y=datetime.datetime.now()
                userAccuracy=answerCount/userGuessCount
                userAccuracy=userAccuracy*100
                print('Congrats you finished Pythonogram!!!!\nPlease call +971 56 663 9565 and ask Kiril Bolotnikov to give you his guitar as your prize.\nI am so sick of that guy and his guitar.')
                print('You completed the puzzle in',y-x,'with',userAccuracy,'%','accuracy.')
                break
    else:
        print(response2[random.randint(0,5)])
        continue
