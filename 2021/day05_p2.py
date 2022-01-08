from collections import defaultdict

# TEST data

RAW = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


with open('./data/day05.txt') as f:
    raw_inp = f.read()

grid = defaultdict(int)

# test with RAW
# raw_inp = RAW

for x in raw_inp.rstrip().splitlines():
    # parse each line of input into individual coords
    p1, p2 = x.split(' -> ')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    
    # increment grid value depending on the case
    if x1 == x2:
        # print('horizontal line')
        for y in range(min(y1,y2), max(y1,y2)+1):
            grid[x1, y] += 1

    elif y1 == y2:
        # print('vertical line')
        for x in range(min(x1,x2), max(x1,x2)+1):
            grid[x,y1] += 1

    else:
        # print('not straight')
        pass

# count the number of points in the grid with a score greater than 1
count = sum([1 for x in grid.values() if x > 1])
print(count)