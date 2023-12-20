import re

with open('day20/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
#broadcaster is simple list of nodesto
broadcaster = []
#flipFlops is dict of [list of nodesto, state]
flipFlops = {}
#conjunctions is dict of [list of nodesto, list of nodes it reads from]
conjunctions = {}
#conjunctionMem is dict of last known inputs from the nodes it reads from
conjunctionMem = {}

pulseQueue = []

#first pass: populate dicts
for line in lines:
    name = re.findall("^[^ ]+", line)[0]
    modulesTo = re.findall("[^ ,]+", line)[2:]
    if name == 'broadcaster':
        broadcaster = modulesTo.copy()
    elif name[0] == '%':
        flipFlops[name[1:]] = [modulesTo.copy(), False]
    elif name[0] == '&':
        conjunctions[name[1:]] = [modulesTo.copy(),[]]
        conjunctionMem[name[1:]] = []

#second pass: catalog inputs to conjunctions
for line in lines:
    name = re.findall("^[^ ]+", line)[0]
    modulesTo = re.findall("[^ ,]+", line)[2:]
    
    if name != 'broadcaster':
        name = name[1:]
    
    for module in modulesTo:
        if module in conjunctions.keys() and not (name in conjunctions[module][1]):
            conjunctions[module][1].append(name)
            conjunctionMem[module].append(False)
            
    
totalHighPulses = 0
totalLowPulses = 0

onTimes = []

i = 0 

keyNode = 'xd'
startNode = 'mf'
#for i in range(1000):
while True:
    i += 1
    #False is low, True is high
    #for module in broadcaster:
    #    pulseQueue.append([module, False, 'broadcaster'])
    
    #key nodes: zt, gt, ms, xd. All must be simultaneuosly activated to activate rx
    #starter nodes for each: jf, bv, fr, mf
    
    #LOOP TIMES:
        # zt: 3823
        # bv: 3797
        # ms: 3907
        # mf: 3733
    # LCM: 211712400442661
        
    pulseQueue.append([startNode, False, 'broadcaster'])
        
    highpulses = 0
    lowpulses = 1
    while len(pulseQueue) > 0:
        currModule = pulseQueue.pop(0)
        if currModule[1]:
            highpulses += 1
        else:
            lowpulses += 1
            
        if currModule[0] in flipFlops.keys():
            if currModule[1] == False:
                flipFlops[currModule[0]][1] = not flipFlops[currModule[0]][1]
                for moduleTo in flipFlops[currModule[0]][0]:
                    pulseQueue.append([moduleTo, flipFlops[currModule[0]][1], currModule[0]])
        elif currModule[0] in conjunctions.keys():
            conjunctionMem[currModule[0]][conjunctions[currModule[0]][1].index(currModule[2])] = currModule[1]
            outPulse = True
            if not False in conjunctionMem[currModule[0]]:
                outPulse = False
                if currModule[0] == keyNode:
                    print(i)
                    exit()
            
            for moduleTo in conjunctions[currModule[0]][0]:
                pulseQueue.append([moduleTo, outPulse, currModule[0]])
    totalHighPulses += highpulses
    totalLowPulses += lowpulses
    
#print(totalLowPulses * totalHighPulses)
