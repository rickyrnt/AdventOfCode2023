import re 
import math

with open('day6/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
times = re.findall("\d+", lines[0])
finaltime = ""
for tim in times:
    finaltime += tim
    
dists = re.findall("\d+", lines[1])
finaldist = ""
for dis in dists:
    finaldist += dis
    
out = 0
time = int(finaltime)
dist = int(finaldist)
min = 0
max = 0
#editor's note: this is how i solved part 2 in real time. had i had time to think i would have implemented the much simpler quadratic formula solution
#and since this took me only a few minutes to solve, i will now implement this optimal solution for fun
"""for i in range(time):
    if i * (time - i) > dist:
        min = i
        break
for i in reversed(range(time)):
    if i * (time - i) > dist:
        max = i
        break
if out == 0: out = max - min + 1
else: out *= max - min + 1"""

min = math.ceil((time - math.sqrt(time*time - 4 * dist))/2)
max = math.ceil((time + math.sqrt(time*time - 4 * dist))/2)
out = max - min
print(out)