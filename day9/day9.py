import re

with open('day9/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
out = 0
for line in lines:
    nums = [int(i) for i in re.findall("-?\d+", line)]
    #finals = []
    firsts = [nums[0]]
    while not all([n == 0 for n in nums]):
        for index, number in enumerate(nums[:-1]):
            nums[index] = nums[index + 1] - number
        #finals.append(nums.pop())
        nums.pop()
        firsts.append(nums[0])
        
    prediction = firsts.pop()
    for first in reversed(firsts):
        prediction = first - prediction
    
    out += prediction
    #out += sum(finals)
    
print(out)