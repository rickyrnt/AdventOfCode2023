import re

with open('day19/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
workflows = {}

def classify(x, m, a, s):
    flow = workflows['in']
    index = 0
    while index < len(flow):
        result = ''
        instructions = re.findall('[^:]+', flow[index])
        if len(instructions) == 1:
            result = instructions[0]
        else:
            test = -1
            if instructions[0][0] == 'x':
                test = x
            elif instructions[0][0] == 'm':
                test = m
            elif instructions[0][0] == 'a':
                test = a
            else:
                test = s
            testResult = False
            if instructions[0][1] == '>':
                testResult = test > int(instructions[0][2:])
            else:
                testResult = test < int(instructions[0][2:])
            if testResult:
                result = instructions[1]
        if result == 'A':
            return x + m + a + s
        elif result == 'R':
            return 0
        elif result == '':
            index += 1
            continue
        else:
            flow = workflows[result]
            index = 0
            
    
out = 0    

for line in lines:
    if len(line) == 0:
        continue
    if line[0] == '{':
        break
        #part 1 code here
        x = int(re.findall("(?<=x=)\d+", line)[0])
        m = int(re.findall("(?<=m=)\d+", line)[0])
        a = int(re.findall("(?<=a=)\d+", line)[0])
        s = int(re.findall("(?<=s=)\d+", line)[0])
        out += classify(x,m,a,s)
    else:
        flowName = re.findall("^\w+", line)[0]
        workflows[flowName] = re.findall("[^,]+", line[line.index('{') + 1:len(line) - 1])
        
#part 2 plan:
#starting with the in workflow,
#go through every element in the workflow, adding to the queue a list of constraints
#when they get to the point of acceptance, multiply the range of each value together and add it to the output

indices = [-1, 'x', 'm', 'a', 's']

#ranges are inclusive
queue = [['in', [1, 4000], [1, 4000], [1, 4000], [1, 4000]]]

def duplicate(oldArr):
    return [oldArr[0], oldArr[1].copy(), oldArr[2].copy(), oldArr[3].copy(), oldArr[4].copy()]

while len(queue) > 0:
    curr = queue.pop()
    if curr[0] == 'R':
        continue
    elif curr[0] == 'A':
        xes = (curr[1][1] - curr[1][0] + 1)
        mes = (curr[2][1] - curr[2][0] + 1)
        aes = (curr[3][1] - curr[3][0] + 1)
        ses = (curr[4][1] - curr[4][0] + 1)
        out += xes * mes * aes * ses
        continue
    for inst in workflows[curr[0]]:
        instructions = re.findall('[^:]+', inst)
        if len(instructions) == 1:
            curr[0] = instructions[0]
            queue.append(curr)
        else:
            constraint = int(instructions[0][2:])
            toChange = indices.index(instructions[0][0])
            if instructions[0][1] == '>':
                if constraint >= curr[toChange][1]:
                    continue
                newGroup = duplicate(curr)
                newGroup[toChange][0] = constraint + 1
                newGroup[0] = instructions[1]
                queue.append(newGroup)
                curr[toChange][1] = constraint
            else:
                if constraint <= curr[toChange][0]:
                    continue
                newGroup = duplicate(curr)
                newGroup[toChange][1] = constraint - 1
                newGroup[0] = instructions[1]
                queue.append(newGroup)
                curr[toChange][0] = constraint
                
print(out)