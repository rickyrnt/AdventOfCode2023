import re

with open('day24/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]

#part 1: turn all equations into y = mx + b, then ax + b == cx + d at x = (d - b)/(a - c)

eqns = []
minVal = 200000000000000
maxVal = 400000000000000

for line in lines:
    nums = [int(i) for i in re.findall(r'-?\d+',line)]
    slope = nums[4] / nums[3]
    intercept = nums[1] - (nums[0] * slope)
    eqns.append([slope,intercept,nums[0], nums[3] > 0])
    
out = 0
for i, eqn1 in enumerate(eqns):
    for eqn2 in eqns[i + 1:]:
        if eqn1[0] != eqn2[0]:
            intersectX = (eqn2[1] - eqn1[1])/(eqn1[0] - eqn2[0])
            if (eqn1[3] and intersectX < eqn1[2]) or (not eqn1[3] and intersectX > eqn1[2]):
                continue
            elif (eqn2[3] and intersectX < eqn2[2]) or (not eqn2[3] and intersectX > eqn2[2]):
                continue
            intersectY = (eqn1[0] * intersectX) + eqn1[1]
            if intersectX >= minVal and intersectX <= maxVal and intersectY >= minVal and intersectY <= maxVal:
                out += 1
            
print(out)