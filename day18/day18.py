import re

with open('day18/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]

out = 0

directions = ['R', 'D', 'L', 'U']

#plan: parse all of our vertices, and keep their row nums in a list
#then sort both those lists
#then for each row num, find the area of the lines in it, and multiply it by the distance to the next line

#test this on the original part 1 before moving on to parsing hexadecimal

instructions = []

for line in lines:
    code = re.findall('(?<=#)\w+', line)[0]
    direction = directions[int(code[-1])]
    #direction = re.findall('\w', line)[0]
    length = int(code[:-1], 16)
    #length = int(re.findall('\d+', line)[0])
    instructions.append([direction, length])
    
rowchanges = []
# [x, y]
pos = [0,0]
#store in [col, start, end] format
verticalLines = []
    
for i, inst in enumerate(instructions):
    if inst[0] == 'R':
        pos[0] += inst[1]
    elif inst[0] == 'L':
        pos[0] -= inst[1]
    elif inst[0] == 'U':
        start = pos[1]
        end = pos[1] - inst[1]
        if i > 0:
            if instructions[i - 1][0] == 'R':
                start -= 1
        elif instructions[0][0] == 'R':
            start -= 1
        if i < len(instructions) - 1:
            if instructions[i + 1][0] == 'L':
                end += 1
        elif instructions[0][0] == 'L':
            end += 1
        
        verticalLines.append([pos[0], end, start])
        
        pos[1] -= inst[1]
        if not pos[1] in rowchanges:
            rowchanges.append(pos[1])    
        if not pos[1] + 1 in rowchanges:
            rowchanges.append(pos[1] + 1)
        if not pos[1] - 1 in rowchanges:
            rowchanges.append(pos[1] - 1)
    elif inst[0] == 'D':
        start = pos[1]
        end = pos[1] + inst[1]
        if i > 0:
            if instructions[i - 1][0] == 'L':
                start += 1
        elif instructions[0][0] == 'L':
            start += 1
        if i < len(instructions) - 1:
            if instructions[i + 1][0] == 'R':
                end -= 1
        elif instructions[0][0] == 'R':
            end -= 1
        
        verticalLines.append([pos[0], start, end])
        
        pos[1] += inst[1]
        if not pos[1] in rowchanges:
            rowchanges.append(pos[1])
        if not pos[1] + 1 in rowchanges:
            rowchanges.append(pos[1] + 1)
        if not pos[1] - 1 in rowchanges:
            rowchanges.append(pos[1] - 1)
        
rowsInOrder = sorted(rowchanges)
linesInOrder = sorted(verticalLines)

for i, row in enumerate(rowsInOrder[:-1]):
    area = 0
    inside = False
    openCol = None
    for col in linesInOrder:
        if col[1] <= row and col[2] >= row:
            if not inside:
                inside = True
                openCol = col[0]
            else:
                inside = False
                area += col[0] - openCol + 1
    
    out += area * (rowsInOrder[i + 1] - row)

#part 1 solution
'''
#i'm sure there's a more efficient way of storing this, but my computer can handle it and it's easier to debug this way :)
#surely this won't have any consequeAAAAAAAAAAAA PART 2
trench = [['#']]

pos = [0,0]
firstIndex = [1, 1]

for line in lines:
    dir = re.findall('\w', line)[0]
    length = int(re.findall('\d+', line)[0])
    color = re.findall('(?<=#)\w+', line)[0]
    
    for i in range(length):
        if dir == 'R':
            pos[0] += 1
        elif dir == 'L':
            pos[0] -= 1
        elif dir == 'U':
            pos[1] -= 1
        elif dir == 'D':
            pos[1] += 1
            
        if pos[1] >= len(trench):
            trench.append(['.'])
        elif pos[1] < 0:
            trench.insert(0, ['.'])
            pos[1] += 1
            firstIndex[1] += 1
        
        while pos[0] >= len(trench[pos[1]]):
            trench[pos[1]] += '.'
        while pos[0] < 0:
            for trenchLine in trench:
                trenchLine.insert(0, '.')
            pos[0] += 1
            firstIndex[0] += 1
            
        trench[pos[1]][pos[0]] = '#'
        out += 1
        

#oh boy i sure do love floodfill
queue = [firstIndex]

while len(queue) > 0:
    thisNum = queue.pop()
    if trench[thisNum[1]][thisNum[0]] != '#':
        trench[thisNum[1]][thisNum[0]] = '#'
        out += 1
        if thisNum[0] + 1 < len(trench[thisNum[1]]):
            queue.append([thisNum[0] + 1, thisNum[1]])
        if thisNum[0] - 1 > 0:
            queue.append([thisNum[0] - 1, thisNum[1]])
        if thisNum[1] + 1 < len(trench):
            queue.append([thisNum[0], thisNum[1] + 1])
        if thisNum[1] - 1 > 0:
            queue.append([thisNum[0], thisNum[1] - 1])'''
    
    
print(out)