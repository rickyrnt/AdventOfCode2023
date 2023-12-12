import re

with open('day3/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    

    
def addnum(i,j):
    global out
    #print(str(i) + ", "  + str(j))
    while lines[i][j-1].isnumeric():
        j-=1
    num = re.match(r'\d+', lines[i][j:])[0]
    #print("num: " + str(num))
    #out += int(num)
    while j + 1 < len(lines) and lines[i][j+1].isnumeric():
        j+=1
    return int(num)
    
    
out = 0

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if line[j] == "*":
            nums = []
            for offi in range(3):
                cont = False
                for offj in range(3):
                    if cont:
                        if not lines[i - offi + 1][j - offj + 1].isnumeric():
                            cont = False
                        continue
                    if i - offi + 1 >= 0 and i - offi + 1 < len(lines) and j - offj + 1 >= 0 and j - offj + 1 < len(line):
                        testchar = lines[i - offi + 1][j - offj + 1] 
                        if testchar.isnumeric():
                            nums.append(addnum(i - offi + 1, j - offj + 1))
                            cont = True
                            
            if len(nums) == 2:
                print(nums)
                out += nums[0] * nums[1]

"""for i, line in enumerate(lines):
    cont = 0
    for j, ch in enumerate(line):
        if line[j].isnumeric() and j >= cont:
            done = False
            #haha disgusting quick and dirty brute force
            for offi in range(3):
                for offj in range(3):
                    if i - offi + 1 > 0 and i - offi + 1 < len(lines) and j - offj + 1 > 0 and j - offj + 1 < len(line):
                        testchar = lines[i - offi + 1][j - offj + 1] 
                        if not done and testchar != None and testchar != '.' and not testchar.isnumeric():
                            #print(testchar)
                            #print(i - offi - 1)
                            cont = addnum(i,j)
                            done = True"""

print(out)