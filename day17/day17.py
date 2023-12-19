with open('day17/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
directions = ['^', '<', 'v', '>']
    
#talkdijkstrato.me
    
nodes = {}
edges = []
heap = []

#residue from trying a* (ended up being unnecessary)
def calcCost(nodeNum: int):
    y = int(nodeNum / len(lines))
    x = nodeNum % len(lines)
    return len(lines) - y + len(lines[0]) - x - 2

#insert into queue
def insert(nodeTo, newData):
    existingPaths = []
    for path in nodes[nodeTo]:
        if path[1] == newData[1]:
            existingPaths.append(path)
            
    if len(existingPaths) > 0:
        placed = False
        skipped = False
        for oldPath in existingPaths:
            #if our path is less straight and less heat loss, replace it
            #part 2 addition: only replace if the length is >= 4 (can turn)
            if newData[0] <= oldPath[0] and newData[2] <= oldPath[2]:
                if newData[2] >= 3 or newData[2] == oldPath[2]:
                    if not placed:
                        nodes[nodeTo][nodes[nodeTo].index(oldPath)] = newData
                        placed = True
                        #break
                    else:
                        del nodes[nodeTo][nodes[nodeTo].index(oldPath)]
                        del heap[heap.index([oldPath, nodeTo, len(nodes[nodeTo])])]
            #otherwise, if it is MORE straight and MORE heat loss, forgeddaboudit
            elif newData[0] >= oldPath[0] and newData[2] >= oldPath[2]:
                if newData[2] > 4 or newData[2] == oldPath[2]:
                    skipped = True
                    break
            #otherwise, tack it on as an alternate option
        if not (placed or skipped):
            #heap.append([calcCost(nodeTo) + newData[0], newData, nodeTo, len(nodes[nodeTo])])
            heap.append([newData, nodeTo, len(nodes[nodeTo])])
            nodes[nodeTo].append(newData)
    else:
        #heap.append([calcCost(nodeTo) + newData[0], newData, nodeTo, len(nodes[nodeTo])])
        heap.append([newData, nodeTo, len(nodes[nodeTo])])
        nodes[nodeTo].append(newData)

#build our lovely graph
index = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        edgeList = []
        if j > 0:
            edgeList.append([int(line[j - 1]), index - 1, '<'])
        if j + 1 < len(line):
            edgeList.append([int(line[j + 1]), index + 1, '>'])
        if i > 0:
            edgeList.append([int(lines[i - 1][j]), index - len(line), '^'])
        if i + 1 < len(lines):
            edgeList.append([int(lines[i + 1][j]), index + len(line), 'v'])
        edges.append(edgeList)
        nodes[index]= []
        index += 1

#cost to get here from direction, direction we took to get here, how long we've been going that way, finished, parent index, parent
nodes[0] = [[0, '.', 0, False, -1, -1]]
#heap.append([calcCost(0), nodes[0][0], 0, 0])
heap.append([nodes[0][0], 0, 0])
    
def debugMap(path):
    global index
    pathlist = [index - 1]
    dirList = [path[1]]
    parent = path[4]
    parentNode = path[5]
    while parent != -1:
        pathlist.append(parent)
        dirList.append(parentNode[1])
        parent = parentNode[4]
        parentNode = parentNode[5]
        
    index = 0
    for line in lines:
        printLine = ''
        for char in line:
            if index in pathlist:
                printLine += dirList[pathlist.index(index)]
            else:
                printLine += char
            index += 1
        print(printLine)
    
#DIJKSTRA THAT SUCKER
nodesProcessed = 0
while True:
    #find minimum node approach
    if len(heap) == 0:
        break
        
    newMin = min(heap)
    minNode = newMin[1]
    minApp = newMin[2]
                
    thisPath = nodes[minNode][minApp]
    
    myPath = []
                
    parent = thisPath[4]
    parentNode = thisPath[5]
    while parent != -1:
        myPath.append(parent)
        parent = parentNode[4]
        parentNode = parentNode[5]
                
    for edge in edges[minNode]:
        #make sure we aren't backtracking
        if edge[1] in myPath:
            continue
        
        #if going in the same direction
        if edge[2] == thisPath[1]:
            #if thisPath[2] > 2:
            if thisPath[2] >= 10:
                #going straight for too long, break out
                continue
            else:
                #GOOD LORD WHAT IS HAPPENING IN THERE
                insert(edge[1], [thisPath[0] + edge[0], edge[2], thisPath[2] + 1, False, minNode, thisPath])
        #if we've gone straight long enough to turn (or we're just starting out)
        elif thisPath[2] >= 4 or thisPath[1] == '.':
            insert(edge[1], [thisPath[0] + edge[0], edge[2], 1, False, minNode, thisPath])
        else:
            continue
            
    thisPath[3] = True
    del heap[heap.index(newMin)]
    
    for path in nodes[index - 1]:
        debugMap(path)
        print(path[0:3])
        exit()



'''for path in nodes[index - 1]:
    if path[2] >= 4:
        print(path[0:3])
        debugMap(path)
        break'''
    