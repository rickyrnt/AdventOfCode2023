import re
from copy import deepcopy

with open('day22/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
    
# min z, x, y, height, width, length
floatingBricks = []

# max z, x1, x2, y1, y2, myIndex
settledBricks = []

# those supporting me, those i support
supports = {}

for line in lines:
    coords = [int(i) for i in re.findall(r'\d+', line)]
    floatingBricks.append([min(coords[2], coords[5]), min(coords[0], coords[3]), min(coords[1], coords[4]), 
                           abs(coords[2] - coords[5]), abs(coords[0] - coords[3]), abs(coords[1] - coords[4])])
    
floatingBricks.sort()

#is it inefficient to sort every iteration? sure. but it's faster to code too.
for brickIndex, brickInsert in enumerate(floatingBricks):
    settledBricks.sort(reverse=True)
    supportLevel = -1
    toAppend = -1
    for i, brickBelow in enumerate(settledBricks):
        if not brickBelow[0] < supportLevel:
            if brickBelow[0] < brickInsert[0]:
                if brickBelow[1] <= brickInsert[1] + brickInsert[4] and brickBelow[2] >= brickInsert[1]:
                    if brickBelow[3] <= brickInsert[2] + brickInsert[5] and brickBelow[4] >= brickInsert[2]:
                        if supportLevel == -1:
                            toAppend = [brickBelow[0] + 1 + brickInsert[3], brickInsert[1], brickInsert[1] + brickInsert[4], brickInsert[2], brickInsert[2] + brickInsert[5], brickIndex]
                            supportLevel = brickBelow[0]
                            supports[brickIndex] = [[],[]]
                        supports[brickIndex][0].append(brickBelow[-1])
                        supports[brickBelow[-1]][1].append(brickIndex)
        else:
            break
    if supportLevel == -1:
        #and on today's episode of terrible storage solutions, we have... this monstrosity!!
        settledBricks.append([1 + brickInsert[3], brickInsert[1], brickInsert[1] + brickInsert[4], brickInsert[2], brickInsert[2] + brickInsert[5], brickIndex])
        supports[brickIndex] = [[],[]]
    else:
        settledBricks.append(toAppend)

out = 0

#part 1 code
'''for brick in supports:
    if len(supports[brick][1]) == 0:
        out += 1
    else:
        for supportedBrick in supports[brick][1]:
            if len(supports[supportedBrick][0]) == 1:
                break
        else:
            out += 1'''
            
def propogateDeletion(sups, brickDel, queue):
    retVal = 0
    for supBrick in sups[brickDel][1]:
        sups[supBrick][0].remove(brickDel)
        if len(sups[supBrick][0]) == 0:
            queue.append(supBrick)
            retVal += 1
            
    return retVal
            
            
for brick in supports:
    testSups = deepcopy(supports)
        
    queue = [brick]
    
    while len(queue) > 0:
        out += propogateDeletion(testSups, queue.pop(0), queue)
            
print(out)