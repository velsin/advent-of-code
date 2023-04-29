filepath = "./data/day08.txt"


with open(filepath) as f:
    grid = [
        [int(char) for char in row] for row in [row.strip() for row in f.readlines()]
    ]


# there will always be 4N-4 trees on the perimeter.

N = len(grid[0])
is_visible = [[False for j in range(N)] for i in range(N)]


# Naive approach: travel like a ray from both sides of each column and row.
forward_range = range(N)
reverse_range = [-1 * (x + 1) for x in forward_range]

# go along each row from left, then right
for i in range(N):
    prev_tree = -1
    for j in range(N):
        if i == 0 or i == N - 1:
            is_visible[i][j] = True
        else:
            if grid[i][j] > prev_tree:
                is_visible[i][j] = True
                prev_tree = grid[i][j]
            else:
                continue

    prev_tree = -1
    for j in reverse_range:
        if grid[i][j] > prev_tree:
            is_visible[i][j] = True
            prev_tree = grid[i][j]
        else:
            continue

# go along each column, first up then down
for j in range(N):
    prev_tree = -1
    for i in range(N):
        if j == 0 or j == N - 1:
            is_visible[i][j] = True
        else:
            if grid[i][j] > prev_tree:
                is_visible[i][j] = True
                prev_tree = grid[i][j]
            else:
                continue

    prev_tree = -1
    for i in reverse_range:
        if grid[i][j] > prev_tree:
            is_visible[i][j] = True
            prev_tree = grid[i][j]
        else:
            continue


print(N)
print(grid)
print(is_visible)

print(sum([sum(x) for x in is_visible]))
