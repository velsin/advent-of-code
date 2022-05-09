from collections import deque


TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

with open('./data/day11.txt') as f:
    raw_input = f.read()

# raw_input = TEST_INPUT

# read into a grid
grid = []
for line in raw_input.splitlines():
    grid.append([int(x) for x in line])

nRow = len(grid)
nCol = len(grid[0])

# based on Jonathan Paulson's day 9 approach, keep track of row, col change for the eight neighbor cells
# combine with conditions to make sure incremented points are withing the grid boundaries.
# go clockwise from top
dRow = [-1, -1, 0, 1, 1, 1, 0, -1]
dCol = [0, 1, 1, 1, 0, -1, -1, -1]

nCycles = 0
sync_flash = False
flash_count = 0

# make the outer loop a while loop, keep going until the sync flash

while not sync_flash:
    nCycles += 1
    # do the whole process within here

    # increase energy of each octopus
    for i in range(nRow):
        for j in range(nCol):
            grid[i][j] += 1

    flashed = [[False for _ in range(nCol)] for _ in range(nRow)] # only one flash allowed

    # go through cells and check for flash condition
    Q = deque() 

    for i in range(nRow):
        for j in range(nCol):
            if grid[i][j] > 9 and flashed[i][j] == False:
                Q.append((i,j))

    # start the flash cascade, go through the deque, and add on all cells affected by flash

    while Q:
        i, j = Q.popleft()

        if flashed[i][j]: # node could have been added to deque before flashing due to a neighbor, must skip
            continue

        flashed[i][j] = True
        flash_count += 1

        # go through all the neighbors and increment, if cell hasn't flashed add it to deque
        for d in range(8):
            dr = i + dRow[d]
            dc = j + dCol[d]

            if 0 <= dr < nRow and 0 <= dc < nCol:
                grid[dr][dc] += 1

                if grid[dr][dc] > 9 and flashed[dr][dc] == False:
                    Q.append((dr,dc))

        # print(Q)
        # print(input())

    sync_flash = all([x for sublist in flashed for x in sublist])

    # after going through the flash cascade, all nodes that flash are set to 0
    for i in range(nRow):
        for j in range(nCol):
            if flashed[i][j]:
                grid[i][j] = 0

print(nCycles)
