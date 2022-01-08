
# Test input
RAW = """3,4,3,1,2"""

with open('./data/day06.txt') as f:
    raw_inp = f.read()

# use test data
# raw_inp = RAW

fishlist = []

for x in raw_inp.rstrip().split(','):
    fishlist.append(int(x))

print('init:', fishlist)

n_days = 80
for d in range(n_days):
    # do updates
    new_fish = 0
    new_fishlist = []
    for f in fishlist:
        if f==0:
            new_fish += 1
            f = 6
        else:
            f -= 1
        new_fishlist.append(f)

    new_fishlist.extend([8]*new_fish)

    fishlist = new_fishlist
    # print status
    # print(f'end of day {d+1}: ', fishlist)

print(len(fishlist))
