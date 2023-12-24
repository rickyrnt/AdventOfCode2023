import re

with open('day23/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
#dijkstra part 3 but worse this time

#plan: build full graph then turn it into a simpler graph. Then run dfs with longest instead of shortest

nodes = {}
edges = {}
solutions = {}
startpos = -1

index = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != '#':
            edgeList = []
            '''if char == '.':
                if j > 0 and line[j - 1] != '#' and line[j - 1] != '>':
                    edgeList.append(index - 1)
                if j + 1 < len(line) and line[j + 1] != '#' and line[j + 1] != '<':
                    edgeList.append(index + 1)
                if i > 0 and lines[i - 1][j] != '#' and lines[i - 1][j] != 'v':
                    edgeList.append(index - len(line))
                if i + 1 < len(lines) and lines[i + 1][j] != '#' and lines[i + 1][j] != '^':
                    edgeList.append(index + len(line))
            elif char == '>':
                edgeList.append(index + 1)
            elif char == '<':
                edgeList.append(index - 1)
            elif char == '^':
                edgeList.append(index - len(line))
            elif char == 'v':
                edgeList.append(index + len(line))'''
                
            if j > 0 and line[j - 1] != '#':
                edgeList.append(index - 1)
            if j + 1 < len(line) and line[j + 1] != '#':
                edgeList.append(index + 1)
            if i > 0 and lines[i - 1][j] != '#':
                edgeList.append(index - len(line))
            if i + 1 < len(lines) and lines[i + 1][j] != '#':
                edgeList.append(index + len(line))
                
            edges[index] = edgeList.copy()
            
            if index == 1:
                nodes[index] = 0
            else:
                nodes[index] = -1
        index += 1

'''queue = [[1]]
qlens = [0]
finalLens = []

while len(queue) > 0:
    currPath = queue.pop()
    currNode = currPath[-1]
    currLen = qlens.pop()
    
    while True:
        numDirs = 0
        nextNode = -1
        for edge in edges[currNode]:
            if edge not in currPath:
                numDirs += 1
                if numDirs > 1:
                    newPath = currPath.copy()
                    newPath.append(edge)
                    queue.append(newPath)
                    qlens.append(currLen + 1)
                else:
                    nextNode = edge
        if nextNode == -1:
            finalLens.append(currLen)
            break
        else:
            currPath.append(nextNode)
            currNode = nextNode
            currLen += 1
            
print(sorted(finalLens, reverse=True))'''

keyNodes = [1, index - 2]
cleanEdges = {1:[], index - 2:[]}
allEdges = []
finalPath = []
finishedNodes = {}

finalEdges = {}

for potentialKey in edges:
    if len(edges[potentialKey]) > 2:
        keyNodes.append(potentialKey)
        cleanEdges[potentialKey] = []
        finalEdges[potentialKey] = []
        finishedNodes[potentialKey] = 0
        
def removeEdge(nodeTo, nodeFrom):
    found = False
    for edge in cleanEdges[nodeTo]:
        if edge[0] == nodeFrom:
            cleanEdges[nodeTo].remove(edge)
            found = True
            break
    for edge in cleanEdges[nodeFrom]:
        if edge[0] == nodeTo:
            cleanEdges[nodeFrom].remove(edge)
            found = True
            break
    return found
        
for startNode in keyNodes:
    for startEdge in edges[startNode]:
        currLen = 1
        lastNode = startNode
        currNode = startEdge
        while currNode not in keyNodes:
            currLen += 1
            for edge in edges[currNode]:
                if edge != lastNode:
                    lastNode = currNode
                    currNode = edge
                    break
        cleanEdges[startNode].append([currNode, currLen])
        newEdge = [currLen, min(startNode, currNode), max(startNode, currNode)]
        if (newEdge[1] == 1 or newEdge[2] == index - 2):
            if newEdge not in finalPath:
                finalPath.append(newEdge)
                finishedNodes[newEdge[1]] = 1
                finishedNodes[newEdge[2]] = 1
            removeEdge(newEdge[1], newEdge[2])
        elif newEdge not in allEdges:
            allEdges.append(newEdge)
            

finishedNodes[1] = 2
finishedNodes[index - 2] = 2

#new test case to test theory i had about longest path (succeeded! hopefully it was a good test)
'''keyNodes = [1,2,3,4,5,6,7,8,index - 2]
        
cleanEdges = {1: [[2,1]],
            2:[[1,0],[3,17],[7,49],[6,9],[5,8]],
            3:[[2,17],[5,6],[4,14]],
            4:[[3,14],[5,5],[8,1]],
            5:[[2,8],[3,6],[4,5],[6,7]],
            6:[[2,9],[5,7],[7,6]],
            7:[[2,49],[6,6],[8,50]],
            8:[[index - 2, 1],[7,50],[4,1]],
            index - 2:[[8,1]]}'''
        
#for visualization purposes
def writeToDot(edgeList, finalList):
    f = open('day23/graphvisualization.dot', 'w')
    f.write('digraph G {\n')
    for edge in edgeList:
        lineadd = 'edge[dir=both,label='
        lineadd += str(edge[0])
        if edge in finalList:
            lineadd += ',color=red'
        else:
            lineadd += ',color=black'
        lineadd += '] '
        lineadd += str(edge[1])
        lineadd += ' -> '
        lineadd += str(edge[2])
        lineadd += '\n'
        f.write(lineadd)
    f.write('}')
    f.close()
    
#writeToDot(allEdges)

'''queue = [[1]]
qlens = [0]
finalLens = []

targetNode = cleanEdges[index - 2][0][0]
finalLen = cleanEdges[index - 2][0][1]

#bfs??? see if this works or if it needs more optimisation (yes it does)
#idea- only one node goes to the end node. exit on that node instead of the end, cuz if we're there we HAVE to go to the end.
    # prevents unnecessary searching, cuts the bfs down by half
while len(queue) > 0:
    currPath = queue.pop(0)
    currLen = qlens.pop(0)
    
    if currPath[-1] == targetNode:
        finalLens.append(currLen + finalLen)
        if currLen + finalLen == 154:
            print(currPath)
        continue
    
    for edge in cleanEdges[currPath[-1]]:
        if edge[0] not in currPath:
            newPath = currPath.copy()
            newPath.append(edge[0])
            queue.append(newPath)
            qlens.append(currLen + edge[1])
            
print(max(finalLens))'''
            
#new idea: the longest path goes through EVERY NODE (it's always possible, I checked.)
#plan: pick the longest legal edge to each node until we have the best possible path
#legal edges:
    # there will be exactly TWO coming out of a node
    # adding them does not strand a node with less than two possible edges
    # adding them does not create a node with more than two edges
    # adding them does not create cycles
    
allEdges = sorted(allEdges, reverse=True)
savedEdges = allEdges.copy()

#TODO: if old node is left with exactly the edges it needs left, automatically add those edges
def removeAllEdges(node):
    removeQueue = []
    for edge in cleanEdges[node]:
        removeQueue.append(edge[0])
    for edgeTo in removeQueue:
        removeEdge(node, edgeTo)
        if len(cleanEdges[edgeTo]) + finishedNodes[edgeTo] == 2:
            for toAdd in cleanEdges[edgeTo]:
                allEdges.insert(0, [toAdd[1], min(toAdd[0], edgeTo), max(toAdd[0], edgeTo)])
    
while len(allEdges) > 0:
    maxEdge = allEdges.pop(0)
    if not removeEdge(maxEdge[1], maxEdge[2]):
        #oopsie! we're not in the list. we must have been removed, move on
        continue
    
    #check for stranding
    #TODO: make this recursive- make a copy of the map, actually insert the node, and see if we have any stranded edges then
    stranded = False
    if finishedNodes[maxEdge[1]] == 1:
        for edge in cleanEdges[maxEdge[1]]:
            #for each node that we would have cut off
            #if the number of possible edges it has + the number of finished edges is less than 2, then we've stranded it
            if len(cleanEdges[edge[0]]) + finishedNodes[edge[0]] - 1 < 2:
                stranded = True
                break
    if finishedNodes[maxEdge[2]] == 1:
        for edge in cleanEdges[maxEdge[2]]:
            if len(cleanEdges[edge[0]]) + finishedNodes[edge[0]] - 1 < 2:
                stranded = True
                break
    if stranded:
        continue
    #check for cycles
    if len(finalEdges[maxEdge[1]]) > 0:
        lastNode = maxEdge[1]
        thisNode = finalEdges[maxEdge[1]][0]
        while len(finalEdges[thisNode]) > 1:
            for edge in finalEdges[thisNode]:
                if edge != lastNode:
                    lastNode = thisNode
                    thisNode = edge
                    break
        if thisNode == maxEdge[2]:
            continue
    
    
    #we are legal, if we've maxed out the node remove all the node's other edges
    finalPath.append(maxEdge)
    finalEdges[maxEdge[1]].append(maxEdge[2])
    finalEdges[maxEdge[2]].append(maxEdge[1])
    
    finishedNodes[maxEdge[1]] += 1
    if finishedNodes[maxEdge[1]] == 2:
        removeAllEdges(maxEdge[1])
    finishedNodes[maxEdge[2]] += 1
    if finishedNodes[maxEdge[2]] == 2:
        removeAllEdges(maxEdge[2])
            
writeToDot(savedEdges, finalPath)

out = 0
for finalEdge in finalPath:
    out += finalEdge[0]
    
print(out)