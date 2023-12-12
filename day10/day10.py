import re

with open('day10/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
out = 0
    
def floodfill(start):
    global out
    global personalMap
    personalMap[start[0]][start[1]] = '@'
    out += 1
    #written recursively for (code writing) speed. i am well aware that this would overflow most cases :)
    if start[0] - 1 >= 0 and personalMap[start[0] - 1][start[1]] == ' ':
        floodfill([start[0] - 1, start[1]])
    if start[0] + 1 < len(personalMap) and personalMap[start[0] + 1][start[1]] == ' ':
        floodfill([start[0] + 1, start[1]])
    if start[1] - 1 >= 0 and personalMap[start[0]][start[1] - 1] == ' ':
        floodfill([start[0], start[1] - 1])
    if start[1] + 1 < len(personalMap[0]) and personalMap[start[0]][start[1] + 1] == ' ':
        floodfill([start[0], start[1] + 1])
        
    
partOneOutput = 1
personalMap = zeros = [ [' ']*len(lines[0]) for _ in range(len(lines)) ]
    
for index, line in enumerate(lines):
    if 'S' in line:
        turncount = 0
        startPos = line.find('S')
        personalMap[index][startPos] = 'S'
        position = []
        dir = ""
        if startPos < len(line) - 1:
            test = line[startPos + 1]
            if test == 'J' or test == '7' or test == '-':
                position = [index, startPos + 1]
                dir = "right"
                turncount += 1
        if startPos > 0:
            test = line[startPos - 1]
            if test == 'L' or test == 'F' or test == '-':
                position = [index, startPos - 1]
                dir = "left"
                turncount -= 1
        if index > 0:
            test = lines[index - 1][startPos]
            if test == 'F' or test == '7' or test == '|':
                position = [index - 1,startPos]
                dir = "up"
        
        while lines[position[0]][position[1]] != 'S':
            currChar = lines[position[0]][position[1]]
            personalMap[position[0]][position[1]] = currChar
            if dir == "right":
                if currChar == 'J':
                    dir = "up"
                    turncount -= 1
                elif currChar == '7':
                    dir = "down"
                    turncount += 1
            elif dir == "left":
                if currChar == 'F':
                    dir = "down"
                    turncount -= 1
                elif currChar == 'L':
                    dir = "up"
                    turncount += 1
            elif dir == "up":
                if currChar == 'F':
                    dir = "right"
                    turncount += 1
                elif currChar == '7':
                    dir = "left"
                    turncount -= 1
            elif dir == "down":
                if currChar == 'J':
                    dir = "left"
                    turncount += 1
                elif currChar == 'L':
                    dir = "right"
                    turncount -= 1
                
            if dir == "up":
                position[0] -= 1
            elif dir == "down":
                position[0] += 1
            elif dir == "left":
                position[1] -= 1
            else:
                position[1] += 1
            partOneOutput += 1
        
        #print(turncount)
        #if turncount is negative, we went counterclockwise
        #if positive, we went clockwise
        #all of my data is counterclockwise and i don't have time to do general case rn
        
        #copy paste this cuz lazy
        #plan: traverse our cleaned up pipe, now performing floodfill on it, dir based on turncount
        if startPos < len(line) - 1:
            test = line[startPos + 1]
            if test == 'J' or test == '7' or test == '-':
                position = [index, startPos + 1]
                dir = "right"
        if startPos > 0:
            test = line[startPos - 1]
            if test == 'L' or test == 'F' or test == '-':
                position = [index, startPos - 1]
                dir = "left"
        if index > 0:
            test = lines[index - 1][startPos]
            if test == 'F' or test == '7' or test == '|':
                position = [index - 1,startPos]
                dir = "up"
                
        turncount //= 4
                
        while personalMap[position[0]][position[1]] != 'S':
            currChar = lines[position[0]][position[1]]
            
            if dir == "right":
                if currChar == 'J':
                    dir = "up"
                elif currChar == '7':
                    dir = "down"
            elif dir == "left":
                if currChar == 'F':
                    dir = "down"
                elif currChar == 'L':
                    dir = "up"
            elif dir == "up":
                if currChar == 'F':
                    dir = "right"
                elif currChar == '7':
                    dir = "left"
            elif dir == "down":
                if currChar == 'J':
                    dir = "left"
                elif currChar == 'L':
                    dir = "right"
                
            if dir == "up":
                if position[1] + turncount >= 0 and position[1] + turncount < len(personalMap[0]) and personalMap[position[0]][position[1] + turncount] == ' ':
                    floodfill([position[0],position[1] + turncount])
                position[0] -= 1
                if position[1] + turncount >= 0 and position[1] + turncount < len(personalMap[0]) and personalMap[position[0]][position[1] + turncount] == ' ':
                    floodfill([position[0],position[1] + turncount])
            elif dir == "down":
                if position[1] - turncount >= 0 and position[1] - turncount < len(personalMap[0]) and personalMap[position[0]][position[1] - turncount] == ' ':
                    floodfill([position[0],position[1] - turncount])
                position[0] += 1
                if position[1] - turncount >= 0 and position[1] - turncount < len(personalMap[0]) and personalMap[position[0]][position[1] - turncount] == ' ':
                    floodfill([position[0],position[1] - turncount])
            elif dir == "left":
                if position[0] - turncount >= 0 and position[0] - turncount < len(personalMap) and personalMap[position[0] - turncount][position[1]] == ' ':
                    floodfill([position[0] - turncount,position[1]])
                position[1] -= 1
                if position[0] - turncount >= 0 and position[0] - turncount < len(personalMap) and personalMap[position[0] - turncount][position[1]] == ' ':
                    floodfill([position[0] - turncount,position[1]])
            else:
                if position[0] + turncount >= 0 and position[0] + turncount < len(personalMap) and personalMap[position[0] + turncount][position[1]] == ' ':
                    floodfill([position[0] + turncount,position[1]])
                position[1] += 1
                if position[0] + turncount >= 0 and position[0] + turncount < len(personalMap) and personalMap[position[0] + turncount][position[1]] == ' ':
                    floodfill([position[0] + turncount,position[1]])
            partOneOutput += 1
        
        break
    
partOneOutput /= 2
for mapline in personalMap:
    print(''.join(mapline))
    
'''with open('output.txt', 'a') as f:
    for mapline in personalMap:
        f.write(''.join(mapline))
        f.write('\n')'''

print(out)