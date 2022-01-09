

RAW = """16,1,2,0,4,2,7,1,2,14"""

with open('./data/day07.txt') as f:
    raw_inp = f.read()

# Use test data
# raw_inp = RAW

# parse input
crabpos = [x for x in map(int,raw_inp.split(','))]

# calculate median
crabpos.sort()
mid = len(crabpos)//2
if mid%2 == 0:
    median = crabpos[mid]
else:
    median = (crabpos[mid] + crabpos[mid-1])//2

# get distances from median and sum together
dist = 0
for x in crabpos:
    dist += abs(x-median)

print(dist)