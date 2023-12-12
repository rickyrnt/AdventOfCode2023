import re 
from functools import cmp_to_key
import itertools

with open('day7/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
vals = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    
def compare(item1, item2):
    for i in range(5):
        char1 = item1[0][i]
        char2 = item2[0][i]
        if vals.index(char1) < vals.index(char2):
            return 1
        elif vals.index(char1) > vals.index(char2):
            return -1
    
    
hands = []
sortedHand = [[],[],[],[],[],[],[]]

for line in lines:
    hands.append(re.findall("\w+", line))
    
for hand in hands:
    done = False
    threePoss = False
    twoPoss = False
    #twoChar = ''
    charCount = {}
    for char in hand[0]:
        charCount[char] = hand[0].count(char)
    
    if 'J' in charCount.keys() and len(charCount) > 1:
        jval = charCount['J']
        del charCount['J']
        charCount[max(charCount, key=charCount.get)] += jval
    
    for num in charCount.values():
        #num = hand[0].count(hand[0][i])
        if num == 5:
            sortedHand[6].append(hand)
            done = True
            break
        elif num == 4:
            sortedHand[5].append(hand)
            done = True
            break
        elif num == 3:
            #if twoChar != '':
            if twoPoss:
                sortedHand[4].append(hand)
                done = True
                break
            else:
                threePoss = True
        elif num == 2:
            if threePoss:
                sortedHand[4].append(hand)
                done = True
                break
            elif twoPoss:
                sortedHand[2].append(hand)
                done = True
                break
            else: twoPoss = True
            '''elif twoChar != hand[0][i]:
                if twoChar != '':
                    sortedHand[2].append(hand)
                    done = True
                    break
                else: twoChar = hand[0][i]'''
        
    if not done:
        if threePoss == True:
            sortedHand[3].append(hand)
        #elif twoChar != '':
        elif twoPoss:
            sortedHand[1].append(hand)
        else: sortedHand[0].append(hand)

for i in range(len(sortedHand)):
    if len(sortedHand[i]) > 1:
        sortedHand[i] = sorted(sortedHand[i], key=cmp_to_key(compare))

hands = list(itertools.chain.from_iterable(sortedHand))

out = 0

for i in range(len(hands)):
    
    out += (i + 1) * int(hands[i][1])

#print(sortedHand)
print(out)