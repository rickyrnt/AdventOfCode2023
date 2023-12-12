import re 

with open('day5/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]
    
stage = 0
oldstage = 0
seeds = []
newseeds = []
source = ""
change = ""
remap = []
toclear = []
maps = []
newmaps = []
testseed = 13
    
def insertmap(change):
    chbgn = change[1]
    chend = change[1] + change[2]
    queue = []
    immediatequeue = []
    overlap = False
    for oldmap in maps:
        olbgn = oldmap[1]
        olend = oldmap[1] + oldmap[2]
        olval = oldmap[0]
        olvle = oldmap[0] + oldmap[2]
        #if overlapping with an old mapping
        if chbgn < olvle and chend > olval:
            overlap = True
            #if we extend beyond the end of the old mapping
            if chend > olvle:
                queue.append([change[0] + (olvle - chbgn), olvle, chend - olvle])
                chend = olvle
                #recursively remap from the end of the old mapping to the end of the new one
                #schedule for later so we don't mess the for loop up
            #if we extend before the beginning of the old mapping
            if chbgn < olval:
                queue.append([change[0], chbgn, olval - chbgn])
                chbgn = olval
                #recursively remap from the beginning of the new mapping to the beginning of the old one
            #modify the old mapping
            #if new map fully inside old one
            if chbgn > olval and chend < olvle:
                immediatequeue.append([oldmap[0], oldmap[1], chbgn - olval])
                immediatequeue.append([oldmap[0] + chend - olval, olbgn + (chend - olval), olvle - chend])
                
                newmaps.append([change[0], olbgn + (chbgn - olval), change[2]])
            #if new map exact same size as old one
            elif chbgn == olval and chend == olvle:
                newmaps.append([change[0] + olval - change[1], oldmap[1], oldmap[2]])
            #if new map overlapping left side
            elif chend < olvle:
                immediatequeue.append([oldmap[0] + chend - olval, olbgn + (chend - olval), olvle - chend])
                
                newmaps.append([change[0] + olval - change[1], oldmap[1], chend - olval])
            #if new map overlapping right side
            elif chbgn > olval:
                immediatequeue.append([oldmap[0], oldmap[1], chbgn - olval])
                
                newmaps.append([change[0], olbgn + (chbgn - olval), olvle - chbgn])
            break
            
        
    #new map for change if no overlap
    if not overlap:
        newmaps.append(change)
    #else recursively do everything in queue
    else:
        maps.remove(oldmap)
        for item in immediatequeue:
            maps.append(item)
        for item in queue:
            insertmap(item)
        
                
for line in lines:
    if re.match(".+-to-.+",line):
        source = re.findall("\w+(?=-to)",line)[0]
        change = re.findall("(?<=to-)\w+",line)[0]
        stage += 1
        maps += newmaps
        newmaps = []
        #debug stuff
        #if stage == 8: 
            #break
            #print("something happens here")
        
    elif re.match("seeds:", line):
        seedpairs = [int(i) for i in re.findall("\d+",line)]
        for i in range(int(len(seedpairs) / 2)):
            seeds.append([seedpairs[i*2], seedpairs[i*2 + 1]])
        continue
    elif len(re.findall("\d+",line)) > 0:
        newmap = [int(i) for i in re.findall("\d+",line)]
        insertmap(newmap)

maps += newmaps
newmaps = []
maps.sort()
seeds.sort()
print(maps)

def findseed():
    scanbegin = 0
    scanend = 0
    for map in maps:
        #if there is a gap in our maps scan it manually
        if map[0] > scanend:
            scanbegin = scanend
            scanend = map[0]
            for seed in seeds:
                if seed[0] < scanend and seed[0] + seed[1] > scanbegin:
                    print(max(seed[0], scanbegin))
                    return
        scanbegin = map[0]
        scanend = map[0] + map [2]
        for seed in seeds:
            if seed[0] < map[1] + map[2] and seed[0] + seed[1] > map[1]:
                print(max(map[0] + seed[0] - map[1], map[0]))
                return
        
findseed()

    #old part 1 code
"""if oldstage != stage and len(remap) > 0 and oldstage != 0:
        #print(remap)
        #print(seeds)
        for seed in seeds:
            if seed == 13:
                print("seed is 13")
            for set in remap:
                if seed >= set[1] and seed < set[1] + set[2]:
                    #print(str(seed) + " remaps to " + str(set[0] + (seed - set[1])))
                    newseeds.append(set[0] + (seed - set[1]))
                    #seeds.remove(seed)
                    toclear.append(seed)
                    break
        for num in toclear:
            seeds.remove(num)
        toclear = []
        seeds += newseeds
        newseeds = []
        print(source + " stage complete")
        remap = []
        
    if len(re.findall("\d+",line)) > 0:
        remap.append([int(i) for i in re.findall("\d+",line)])
                
    oldstage = stage
        
for seed in seeds:
    if seed == 13:
        print("seed is 13")
    for set in remap:
        if seed >= set[1] and seed < set[1] + set[2]:
            #print(str(seed) + " remaps to " + str(set[0] + (seed - set[1])))
            newseeds.append(set[0] + (seed - set[1]))
            #seeds.remove(seed)
            toclear.append(seed)
            break
for num in toclear:
    seeds.remove(num)
toclear = []
seeds += newseeds
newseeds = []
print(source + " stage complete")
remap = []
        
                
print(min(seeds))"""