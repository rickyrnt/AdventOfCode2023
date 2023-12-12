import re

#I used this code to test whether or not all the starting points were unique cycles. They were. I was so scared that they would be not cycles but they were.
#Knowing this would have saved me a lot of time and panic I think but eh what can you do.
#I suppose, thinking about it 24 hours later, that this problem couldn't possibly make sense unless they were all unique cycles... live and learn.

with open('day8/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]

instructions = re.findall("\w+", lines[0])[0]
    
nodes = []
dirs = []
places = []

for line in lines[2:]:
    input = re.findall("\w+", line)
    nodes.append(input[0])
    dirs.append(input[1:])
    if input[0][2] == 'A':
        places.append(input[0])

curr = 'QXA'
print(dirs[nodes.index(curr)])
out = 0
pos = 0
finished = False

while curr[2] != "Z":
    finished = True
    if pos >= len(instructions): pos = 0
    dir = instructions[pos]
    pos += 1
    out += 1
    if dir == 'L':
        curr = dirs[nodes.index(curr)][0]
    else:
        curr = dirs[nodes.index(curr)][1]

if pos >= len(instructions): pos = 0
dir = instructions[pos]
if dir == 'L':
    print(dirs[nodes.index(curr)][0])
else:
    print(dirs[nodes.index(curr)][1])

print(out)