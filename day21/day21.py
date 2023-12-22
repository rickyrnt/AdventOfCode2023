import re

with open('day21/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
#talkdijkstrato.me again    
    
nodes = {}
edges = []
startpos = -1
    
index = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        edgeList = []
        if j > 0 and line[j - 1] != '#':
            edgeList.append(index - 1)
        if j + 1 < len(line) and line[j + 1] != '#':
            edgeList.append(index + 1)
        if i > 0 and lines[i - 1][j] != '#':
            edgeList.append(index - len(line))
        if i + 1 < len(lines) and lines[i + 1][j] != '#':
            edgeList.append(index + len(line))
        edges.append(edgeList)
        
        if char == 'S':
            startpos = index
        nodes[index] = float('inf')
        index += 1
        
    
def dijkstra(nodes, edges, distanceMax):
    solutions = {}
    while len(nodes.values()) > 0:
        minNode = min(nodes, key=nodes.get)
        minVal = nodes[minNode]
        if minVal > distanceMax:
            break
        solutions[minNode] = minVal
        for edge in edges[minNode]:
            if edge in nodes and minVal + 1 < nodes[edge]:
                nodes[edge] = minVal + 1
                
        del nodes[minNode]
        
    return solutions
    
'''startNodes = nodes.copy()
startNodes[startpos] = 0
solutions = dijkstra(startNodes, edges, 64)
    
out = 0
for pathLen in solutions.values():
    if pathLen <= 64 and pathLen % 2 == 0:
        out += 1
    
index = 0
for i, line in enumerate(lines):
    outLine = ''
    for j, char in enumerate(line):
        if char == 'S':
            outLine += "@"
        elif index in solutions.keys():
            if solutions[index] == float('inf'):
                outLine += '#'
            elif solutions[index] == 0:
                outLine += 'S'
            elif solutions[index] <= 64 and solutions[index] % 2 == 0:
                outLine += 'O'
            else:
                outLine += '.'
        else:
            outLine += char
        index += 1
    print(outLine)
    

print(out)'''
    
#dynamic programming time
#first, run the center map. find the shortest path to each edge, and queue up adjacent maps starting from the node adjacent to that one
#keep track of which map repetitions we've been to, so we don't overscore
#score maps in the queue starting from the edge. store their data in a dictionary if we completely fill them so we don't hafta redo 'em all
#this'd be a nightmare if the maps were too complex but i can't help but notice that the input data has straight-line clear paths to the edges from the start... convenient!

# some observations for the final case to make it go faster (won't necessarily work in the test case)
# going in a straight line to the edges will offset the graph by 1, so it's worth calculating both values for a full map
# full map values are ALWAYS THE SAME
# input full map vales: centered- 7757, offset- 7748
# quickest path for input (NOT TEST CASE) is always in a straight line

# conclusion: i am not going to write a general case solution, but rather one that runs SPECIFICALLY for inputs with these conditions. Which is just this input.
# in fact, i am going to piecemeal calculate every section of the final map and add them together manually

# edge indices

# 0     65      130
#
# 8515  8580   8645
#
# 17030 17095 17160 

#below code used to collect the data found in maps.txt

stepsLeft = (26501365 - 65)
length = int((26501365 - 65) / 131)

out = 0
out += 158635871652300 * 4
out += 978 * length
out += 977 * length
out += 996 * length
out += 990 * length
out += 6804 * (length - 1)
out += 6790 * (length - 1)
out += 6781 * (length - 1)
out += 6813 * (length - 1)
out += 7748 + 5846 + 5823 + 5846 + 5869


print(out)

'''

halfLength = int(length / 2)

barsize = (halfLength - 1) * 7748 + (halfLength) * 7757

cornersize = 0 

offset = False
while barsize > 0:
    cornersize += barsize
    if offset:
        barsize -= 7748
    else:
        barsize -= 7757
    offset = not offset
    
print(cornersize)
print(barsize)'''

'''offset = True
while length > 1:
    offset = not offset
    if offset:
        barsize += 7748
    else:
        barsize += 7757
    stepsLeft -= 131
    length -= 1'''

'''print(barsize)
print(stepsLeft)

stepsLeft -= 66
#offset = not offset

startNodes = nodes.copy()
startNodes[17160] = 0
solutions = dijkstra(startNodes, edges, stepsLeft)
    
out = 0

compareVal = 0
if offset:
    compareVal = 1

for pathLen in solutions.values():
    if pathLen <= stepsLeft and pathLen % 2 == compareVal:
        out += 1
        
index = 0
for i, line in enumerate(lines):
    outLine = ''
    for j, char in enumerate(line):
        if char == 'S':
            outLine += "@"
        elif index in solutions.keys():
            if solutions[index] == float('inf'):
                outLine += '#'
            elif solutions[index] == 0:
                outLine += 'S'
            elif solutions[index] <= stepsLeft and solutions[index] % 2 == compareVal:
                outLine += 'O'
                #outLine += str(solutions[index])
            else:
                outLine += '.'
        else:
            outLine += char
        index += 1
    print(outLine)
    

print(out)'''