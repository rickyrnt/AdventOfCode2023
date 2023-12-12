import re

with open('day11/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
finalmap = lines.copy()

insertedlines = 0
    
for index, line in enumerate(lines):
    if not '#' in line:
        finalmap.insert(index + insertedlines, '+'*len(line))
        insertedlines += 1
        
insertedlines = 0

for i in range(len(lines[0])):
    hasGalaxy = False
    for j in range(len(lines)):
        if lines[j][i] == '#':
            hasGalaxy = True
            break
    if not hasGalaxy:
        for index, line in enumerate(finalmap):
            finalmap[index] = line[:i + insertedlines] + '+' + line[i + insertedlines:]
        insertedlines += 1
        
galaxies = []
        
for row, line in enumerate(finalmap):
    for col, galaxy in enumerate(line):
        if galaxy == '#':
            galaxies.append([row, col])
            
out = 0
expansion = 1000000 - 1

for sIndex, start in enumerate(galaxies):
    for eIndex, end in enumerate(galaxies[sIndex + 1:]):
        if start[0] != end[0]:
            pos = start[0]
            step = int((end[0] - start[0])/abs(end[0] - start[0]))
            
            while pos != end[0]:
                if finalmap[pos][start[1]] == '+':
                    out += expansion
                else: out += 1
                pos += step
            
        if start[1] != end[1]:
            pos = start[1]
            step = int((end[1] - start[1])/abs(end[1] - start[1]))
            
            while pos != end[1]:
                if finalmap[end[0]][pos] == '+':
                    out += expansion
                else: out += 1
                pos += step
        
        #part 1 code
        #out += abs(start[0] - end[0]) + abs(start[1] - end[1])
        
print(out)

#editor's note: IDEA FOR LESS HACKY SOLUION:
#store inserted columns in a list, inserted rows in another. instead of traversing map manually, just see how many inserted
#rows or columns are between you and the destination, and add that to the distance calculations
#removes the need for a second map, drastically reduces complexity. but also i didn't think about it at the time and i 
#already made a solution so i'm not gonna start on another one :)