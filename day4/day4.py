import re 

with open('day4/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
out = 0    
scorevals = {}

def score(linenum):
    global out
    if linenum == len(lines) - 1:
        scorevals[linenum] = 1
        return
    line = lines[linenum]
    numsets = line[line.find(":"):].split("|")
    #editor's note: why would you line[line.find(":"):].split("|") when you could just r'(\d+)(?=\s((\d+\s+)+)?\|)'? so much easier. clearly.
    #this is sarcasm, but regex is my new favorite thing nonetheless
    goodnums = [int(i) for i in re.findall("\d+", numsets[0])]
    ournums = [int(i) for i in re.findall("\d+", numsets[1])]
    val = 0
    for number in ournums:
        if number in goodnums:
            val += 1
    
    scoreval = 0
    
    
    
    for next in range(val):
        if linenum + val - next < len(lines):
            scoreval += scorevals[linenum + val - next]
    
    scorevals[linenum] = scoreval + 1

for line in range(len(lines)):
    score(len(lines) - line - 1)
    
for key in scorevals:
    out += scorevals[key]

print(out)