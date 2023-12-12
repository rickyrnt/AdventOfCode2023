import re 

with open('day2/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]

#editors note: learn regex. this problem can be solved instantly by something to the effect of max(re.findall(r'\d(?<= blue), line.))
#in fact i'm gonna try it now. real solution in quotes at bottom

out = 0

for line in lines:
    red = max([int(i) for i in re.findall(r'\d+(?= red)', line)])
    green = max([int(i) for i in re.findall(r'\d+(?= green)', line)])
    blue = max([int(i) for i in re.findall(r'\d+(?= blue)', line)])
    
    out += red * green * blue
    
#yeah ok it takes the solution down to O(n) with FOUR LINES. regex is busted i love it.

"""for line in lines:
    red = 0
    green = 0
    blue = 0
    possible = True
    split = line.split(":")
    sets = split[1].split(";")
    for set in sets:
        if possible:
            pairs = set.split(",")
            for pair in pairs:
                count = pair.split(" ")
                #print(count[2])
                if (count[2] == 'red' and int(count[1]) > red):
                    red = int(count[1])
                elif (count[2] == 'green' and int(count[1]) > green):
                    green = int(count[1])
                elif (count[2] == 'blue' and int(count[1]) > blue):
                    blue = int(count[1])
    out += red * green * blue"""
            
        
print(out)

#part 1 code
"""if (count[2] == 'red' and int(count[1]) > 12) or (count[2] == 'green' and int(count[1]) > 13) or (count[2] == 'blue' and int(count[1]) > 14):
                    #print(pair)
                    possible = False
                    break
    if possible:
        #print(int(split[0][5:]))
        out += int(split[0][5:])"""