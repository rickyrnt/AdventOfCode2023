import re

with open('day15/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
def hash(stringIn):
    currVal = 0
    
    for char in stringIn:
        currVal += ord(char)
        currVal *= 17
        currVal %= 256
        
    return currVal

instructions = lines[0].split(',')

out = 0

boxes = [[] for i in range(256)]
boxlenses = [[] for i in range(256)]

for inst in instructions:
    name = re.findall(r'\w+', inst)[0]
    boxnum = hash(name)
    if bool(re.search(r'\-', inst)):
        if name in boxes[boxnum]:
            delIndex = boxes[boxnum].index(name)
            del boxes[boxnum][delIndex]
            del boxlenses[boxnum][delIndex]
    else:
        focLength = re.findall(r'\d', inst)[0]
        if name in boxes[boxnum]:
            repIndex = boxes[boxnum].index(name)
            boxlenses[boxnum][repIndex] = focLength
        else:
            boxes[boxnum].append(name)
            boxlenses[boxnum].append(focLength)
    
for i, box in enumerate(boxlenses):
    for j, lens in enumerate(box):
        out += (i + 1) * (j + 1) * int(lens)
    
print(out)