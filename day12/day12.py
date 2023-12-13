import re

with open('day12/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
def findPos(groups, location):
    position = 0
    for i in range(location[0]):
        position += len(groups[i])
    return position + location[1]
    
# keep a dictionary of everything we've already calculated, so we don't have to recalculate it
precalcs = {}
    
def count(groups, lengths, maxpositions, me, position):  
    global precalcs  
    runs = 0
    hashloc = -1
    while True:
        #If we've gone past a hashtag without fulfilling it, STOP
        #Plan: record the first hashtag we passed over. we CANNOT PASS IT COMPLETELY
        if hashloc != -1:
            if findPos(groups, position) > hashloc:
                break
        elif '#' in groups[position[0]][position[1]:]:
            hashloc = findPos(groups, [position[0], groups[position[0]][position[1]:].index('#') + position[1]])
        
        if position[0] == maxpositions[me][0] and position[1] > maxpositions[me][1]:
            break
        elif lengths[me] > len(groups[position[0]][position[1]:]):
            position[0] += 1
            position[1] = 0
        elif position[1] != 0 and groups[position[0]][position[1] - 1] == '#':
            position[1] += 1
        elif position[1] + lengths[me] < len(groups[position[0]]) and groups[position[0]][position[1] + lengths[me]] == '#':
            position[1] += 1
        else:
            #base case
            if me == len(lengths) - 1:
                good = True
                checkPos = [position[0], position[1] + lengths[me] + 1]
                #check for outstanding hashtags
                while checkPos[0] < len(groups):
                    if checkPos[1] >= len(groups[checkPos[0]]):
                        checkPos[1] = 0
                        checkPos[0] += 1
                    elif groups[checkPos[0]][checkPos[1]] == '#':
                        good = False
                        break
                    else:
                        checkPos[1] += 1
                if good:
                    runs += 1
            else:
                startingPos = []
                if lengths[me] + 1 >= len(groups[position[0]][position[1]:]):
                    startingPos = [position[0] + 1, 0]
                else:
                    startingPos = position.copy()
                    startingPos[1] += lengths[me] + 1
                newKey = str(me + 1) + str(startingPos)
                if newKey in precalcs.keys():
                    runs += precalcs[newKey]
                else:
                    newCalc = count(groups, lengths, maxpositions, me + 1, startingPos)
                    runs += newCalc
                    precalcs[newKey] = newCalc
            position[1] += 1
    
    return runs
    
out = 0
for lineNum, line in enumerate(lines):
    groups = []
    lengths = []
    precalcs = {}
    filterLine = re.findall(r'[^ ]+', line)
    groupLine = ''
    lengthLine = ''
    for i in range(5):
        groupLine += filterLine[0]
        if i < 4:
            groupLine += '?'
        lengthLine += filterLine[1] + ','
    groups = re.findall(r'[^. \d,]+', groupLine)
    lengths = [int(i) for i in re.findall(r'\d+', lengthLine)]
    
    if len(groups) == 0:
        continue
    
    #STRATEGY PLAN: trim down all possibilities until we are left with just the number of places each element can go
    #then, permute those elements (shouldn't take too long, there aren't too many and we have a list of everything we can test)
    #if it doesn't work, NEW STRATEGY PLAN: start crying
    
    #strategies:
    #trim ends (if the first/last element doesn't have space for
    # the first/last number, trim it)
    while(True):
        if len(groups[0]) < lengths[0]:
            del groups[0]
        else:
            break
    
    while(True):
        if len(groups[-1]) < lengths[-1]:
            del groups[-1]
        else:
            break
            
    tempGroups = groups.copy()
    maxpositions = []
    #find max position first, to limit the things
    for length in reversed(lengths):
        position = 0
        while True:
            if length > len(tempGroups[-1][:len(tempGroups[-1]) - position]):
                del tempGroups[-1]
                position = 0
            elif position != 0 and tempGroups[-1][-position] == '#':
                position += 1
            elif length != len(tempGroups[-1][:len(tempGroups[-1]) - position]) and tempGroups[-1][-1 -position - length] == '#':
                position += 1
            else:
                strPos = len(tempGroups[-1]) - position - length
                maxpositions.insert(0, [len(tempGroups) - 1, strPos])
                tempGroups[-1] = tempGroups[-1][:strPos]
                if len(tempGroups[-1]) > 0:
                    tempGroups[-1] = tempGroups[-1][:-1]
                else:
                    del tempGroups[-1]
                break
             
    #from there, permute
    # recursive:
    # for every position the element can be in 
    # recursively place the next element
    # if you are the last element, count how many places you can go and return that number
    thisCount = count(groups, lengths, maxpositions, 0, [0,0])
    out += thisCount
    #print(str(lineNum) + " done out of 1000. Result: " + str(thisCount) + ". Output: " + str(out))
    
print(out)