from collections import defaultdict

# Test input
RAW = """3,4,3,1,2"""

with open('./data/day06.txt') as f:
    raw_inp = f.read()

# use test data
# raw_inp = RAW

fishdict = defaultdict(int)

for x in raw_inp.rstrip().split(','):
    fishdict[int(x)] += 1

print('init:', fishdict)

n_days = 256
for d in range(n_days):
    # do updates 
    new_fishdict = defaultdict(int)
    for i in range(8,0,-1):
        new_fishdict[i-1] = fishdict[i]
    # spawn new fish
    new_fishdict[6] += fishdict[0]
    new_fishdict[8] += fishdict[0]

    fishdict = new_fishdict
    # print status
    # print(f'end of day {d+1}: ', fishlist)

print(sum(fishdict.values()))


