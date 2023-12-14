import re

with open('day13/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
def compareStrings(string1, string2):
    if string1 == string2:
        return 0
    else:
        singleMatch = False
        for index, char in enumerate(string1):
            if char != string2[index]:
                if singleMatch:
                    return -1
                else:
                    singleMatch = True
        return 1
    
def findMirror(map):
    #found = False
    mirror = -1
    for index, mapLine in enumerate(map[:-1]):
        stringComp = compareStrings(mapLine, map[index + 1])
        if stringComp != -1:
            matches = stringComp
            i = 1
            #found = True
            while index + 1 + i < len(map) and index - i >= 0:
                stringComp = compareStrings(map[index + 1 + i], map[index - i])
                if stringComp == -1:
                    matches = -1
                    break
                else:
                    matches += stringComp
                    if matches > 1:
                        break
                i += 1
            if matches == 1:
                mirror = index + 1
    return mirror
    
map = []
out = 0

for line in lines:
    if line == '':
        mirror = findMirror(map)
        if mirror == -1:
            newMap = [''] * len(map[0])
            for mapLine in reversed(map):
                for index, character in enumerate(mapLine):
                    newMap[index] += character
            mirror = findMirror(newMap)
            if mirror == -1:
                print("CODE BROKE LMAO")
            else:
                out += mirror
        else:
            out += mirror * 100
        map = []
    else:
        map.append(line)
        
print(out)