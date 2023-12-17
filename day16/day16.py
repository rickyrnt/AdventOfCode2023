import re

with open('day16/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
queue = [[0,0, 'right']]

energized = [[[] for i in range(len(lines[0]))] for j in range(len(lines))]

def propogate():
    global out
    global queue
    light = queue.pop()
    while True:
        charOn = lines[light[0]][light[1]]
        charDir = energized[light[0]][light[1]]
        
        if charOn == '.' or ((light[2] == 'left' or light[2] == 'right') and charOn == '-') or ((light[2] == 'up' or light[2] == 'down') and charOn == '|'):
            if light[2][0] in charDir:
                break
        elif light[2] == 'right':
            if charOn == '/':
                light[2] = 'up'
            elif charOn == '\\':
                light[2] = 'down'
            elif charOn == '|':
                queue.append([light[0],light[1],'up'])
                light[2] = 'down'
        elif light[2] == 'left':
            if charOn == '\\':
                light[2] = 'up'
            elif charOn == '/':
                light[2] = 'down'
            elif charOn == '|':
                queue.append([light[0],light[1],'up'])
                light[2] = 'down'
        elif light[2] == 'up':
            if charOn == '\\':
                light[2] = 'left'
            elif charOn == '/':
                light[2] = 'right'
            elif charOn == '-':
                queue.append([light[0],light[1],'left'])
                light[2] = 'right'
        elif light[2] == 'down':
            if charOn == '/':
                light[2] = 'left'
            elif charOn == '\\':
                light[2] = 'right'
            elif charOn == '-':
                queue.append([light[0],light[1],'left'])
                light[2] = 'right'
                
        if len(charDir) == 0:
            out += 1
        charDir.append(light[2][0])
                
        if light[2] == 'right':
            light[1] += 1
        elif light[2] == 'left':
            light[1] -= 1
        elif light[2] == 'up':
            light[0] -= 1
        elif light[2] == 'down':
            light[0] += 1
            
        if light[0] < 0 or light[0] >= len(lines) or light[1] < 0 or light[1] >= len(lines[0]):
            break

finalOut = 0

for i in range(len(lines[0])):
    out = 0
    
    queue = [[0, i, 'down']]
    energized = [[[] for i in range(len(lines[0]))] for j in range(len(lines))]

    propogate()

    while len(queue) > 0:
        propogate()
        
    if out > finalOut:
        finalOut = out
    
    out = 0
    
    queue = [[len(lines) - 1, i, 'up']]
    energized = [[[] for i in range(len(lines[0]))] for j in range(len(lines))]

    propogate()

    while len(queue) > 0:
        propogate()
        
    if out > finalOut:
        finalOut = out 
        
for i in range(len(lines)):
    out = 0
    
    queue = [[i, 0, 'right']]
    energized = [[[] for i in range(len(lines[0]))] for j in range(len(lines))]

    propogate()

    while len(queue) > 0:
        propogate()
    
    if out > finalOut:
        finalOut = out
    
    out = 0
    
    queue = [[i, len(lines[0]) - 1, 'left']]
    energized = [[[] for i in range(len(lines[0]))] for j in range(len(lines))]

    propogate()

    while len(queue) > 0:
        propogate()

    if out > finalOut:
        finalOut = out 
    
        
print(finalOut)