import re

with open('day14/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
def score(map):
    finalScore = 0
    for index, line in enumerate(map):
        finalScore += line.count('O') * (index + 1)
    return finalScore
    
def scorePart1(pair):
    finalScore = 0
    for i in range(pair[1]):
        finalScore += pair[0] - i
    return finalScore
    
map = [''] * len(lines[0])
    
for line in lines:
    for index, character in enumerate(reversed(line)):
        map[index] += character
        
out = 0
states = {}
stateVals = {}

#pray we never complete this loop
k = 0
for k in range(1000000000):
    for j in range(4):
        eastState = ''
        stateScore = 0
        
        for mapIndex, mapLine in enumerate(map):
            #find pairs
            length = len(mapLine)
            pairs = [[length,0]]
            hashIndexes = []
            for index, character in enumerate(mapLine):
                if character == '#':
                    pairs.append([length - index - 1, 0])
                    hashIndexes.append(index)
                elif character == 'O':
                    pairs[-1][1] += 1
                    
            if j == 3:
                for pair in pairs:
                    eastState += str(pair)
                    
            #slam left
            modifiedLine = ''
            i = 0
            pairIndex = 0
            while i < length:
                if i in hashIndexes:
                    modifiedLine += '#'
                    i += 1
                    pairIndex += 1
                elif pairIndex < len(pairs) and length - i == pairs[pairIndex][0] and pairs[pairIndex][1] > 0:
                    modifiedLine += 'O' * pairs[pairIndex][1]
                    i += pairs[pairIndex][1]
                else:
                    modifiedLine += '.'
                    i += 1
            map[mapIndex] = modifiedLine
        
        if j == 3:
            if eastState in states:
                #HOO BOY do we do some magic here ok this needs explanation
                #we've found our loop. the length of that loop is:
                # our current iter (k) - the last time we were in this state (states[eastState])
                #we need to find how far past that state our final solution goes, which is:
                # how many runs we have left (1000000000 - k) mod loop length
                #offset it by the start of our loop (states[eastState] - 1), and find its value in stateVals
                #we have our answer!
                print(stateVals[((1000000000 - k) % (k - states[eastState])) + states[eastState] - 1])
                exit()
            else:
                states[eastState] = k
                stateVals[k] = score(map)
        
        #rotate
        newMap = [''] * len(lines[0])
        for line in reversed(map):
            for index, character in enumerate(line):
                newMap[index] += character

        map = newMap.copy()
        
        
'''for pair in pairs:
    out += score(pair)'''
        
print(out)