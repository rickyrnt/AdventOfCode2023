#my old code is so close but gives a wrong answer... 
#i decided to try to write it again from scratch, now that i know what i'm doing so i can get it right first try
#editor's note: it worked!

#parse input and build graph
with open('day17/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
edges = []
solutions = {}

#edge data: [cost, nodetonum, direction]
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
        solutions[index]= []
        index += 1
        
#push to heap (and solution dictionary): [0:cost, 1:direction, 2:straightlength, 3:mynodenum, 4:parent pointer]

heap = [[0, '.', 0, 0, -1]]

#insert logic
    #add to heap and
    #add to the node solutions

#push to heap logic
#WE ARE SEEKING: the minimum possible solution for straight lengths 1, 2, 3, and >= 4 in every direction
def pushToHeap(newApproach):
    #traceback- make sure we aren't backtracking. if we are, break out
    parent = newApproach[4]
    while parent != -1:
        if parent[3] == newApproach[3]:
            return False
        parent = parent[4]
        
    oldApproaches = []
    for approach in solutions[newApproach[3]]:
        if approach[1] == newApproach[1]:
            oldApproaches.append(approach)
            
    fastest = False
    #if the node already has approaches from this direction, consider:
    for oldApproach in oldApproaches:
        #if we will have gone 1, 2, or 3 straight, 
        if newApproach[2] <= 3:
            #is there an approach with the same straightlength?
            if newApproach[2] == oldApproach[2]:
                #if so, do we cost less? if so, replace the old one
                if newApproach[0] < oldApproach[0]:
                    solutions[newApproach[3]][solutions[newApproach[3]].index(oldApproach)] = newApproach
                    heap[heap.index(oldApproach)] = newApproach
                    return True
                #if not, break out
                else:
                    return False
            #if not, add in our solution
            else:
                solutions[newApproach[3]].append(newApproach)
        #make sure we aren't comparing a >=4 with a 1, 2, or 3 (they are not the same)
        elif oldApproach[2] <= 3:
            continue
        #otherwise we will have gone at least 4 straight, is our straightlength <= the old solution and our cost less?
        elif newApproach[2] <= oldApproach[2] and newApproach[0] <= oldApproach[0]:
            #if so, the solution is definitely better. replace the old solution and remove other approaches that also satisfy the condition
            if not fastest:
                fastest = True
                solutions[newApproach[3]][solutions[newApproach[3]].index(oldApproach)] = newApproach
                heap[heap.index(oldApproach)] = newApproach
            else:
                del solutions[newApproach[3]][solutions[newApproach[3]].index(oldApproach)]
                del heap[heap.index(oldApproach)]
        #ok, we are not better than the old solution. are we worse? (length >= old and cost >= old)
        elif newApproach[2] >= oldApproach[2] and newApproach[2] >= oldApproach[2]:
            #if so, break out, we'd just clog up the system
            return False
        #otherwise, we have some advantages and some disadvantages. add us into the system
        elif not fastest:
            solutions[newApproach[3]].append(newApproach)
            heap.append(newApproach)
            return True
    #add us into the system
    if not fastest:
        solutions[newApproach[3]].append(newApproach)
        heap.append(newApproach)
        return True

#while we haven't found a solution
while len(heap) > 0:
    #pop min cost off of heap
    minPath = min(heap)
    del heap[heap.index(minPath)]
    #explore each edge
    for edge in edges[minPath[3]]:
        #if we are within constraints (turn after 4, don't go past 10), push to heap
        if edge[2] == minPath[1] or minPath[1] == '.':
            if minPath[2] < 10:
                pushToHeap([minPath[0] + edge[0], edge[2], minPath[2] + 1, edge[1], minPath])
        elif  minPath[2] >= 4:
            pushToHeap([minPath[0] + edge[0], edge[2], 1, edge[1], minPath])

    #we found our solution! provide a traceback for debugging and print out our solution!
    for sol in solutions[index - 1]:
        if sol[2] >= 4:
            path = [index - 1]
            pathDirs = [sol[1]]
            parent = sol[4]
            while parent != -1:
                path.append(parent[3])
                pathDirs.append(parent[1])
                parent = parent[4]
            index = 0
            for line in lines:
                printLine = ''
                for char in line:
                    if index in path:
                        printLine += pathDirs[path.index(index)]
                    else:
                        printLine += char
                    index += 1
                print(printLine)
            print(sol[:4])
            exit()