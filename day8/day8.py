import re
from math import gcd

with open('day8/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    

def findDist(directions, beginnings):
    lengths = beginnings.copy()
    finished = False
    pos = 0
    length = 0
    while not finished:
        finished = True
        if pos >= len(directions): pos = 0
        dir = directions[pos]
        pos += 1
        #out += 1
        length += 1
        for index, curr in enumerate(beginnings):
            if beginnings[index][2] != 'Z' and length != 0: 
                if dir == 'L':
                    beginnings[index] = dirs[nodes.index(curr)][0]
                else:
                    beginnings[index] = dirs[nodes.index(curr)][1]
                if beginnings[index][2] != 'Z': 
                    finished = False
                else:
                    lengths[index] = length
    return lengths
                
    
instructions = re.findall("\w+", lines[0])[0]


nodes = []
dirs = []
starts = []
startDists = []

#out = 0
for line in lines[2:]:
    input = re.findall("\w+", line)
    nodes.append(input[0])
    dirs.append(input[1:])
    if input[0][2] == 'A':
        starts.append(input[0])
startDists = findDist(instructions, starts)
print(startDists)

#find least common multiple, code taken from online
lcm = 1
for i in startDists:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)