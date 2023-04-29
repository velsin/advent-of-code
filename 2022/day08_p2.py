filepath = "./data/day08.txt"


with open(filepath) as f:
    grid = [
        [int(char) for char in row] for row in [row.strip() for row in f.readlines()]
    ]


N = len(grid[0])


# Brute force O(N^2) solution, create rays outward from every grid position??
def rays(i_s, j_s):
    # calculate the 4 ray directions going out from i,j
    source = grid[i_s][j_s]
    # up
    u_score = 0
    for u in range(i_s):
        if grid[i_s - u - 1][j_s] < source:
            u_score += 1
        else:
            u_score += 1
            break
    # down
    d_score = 0
    for d in range(N - i_s - 1):
        if grid[i_s + d + 1][j_s] < source:
            d_score += 1
        else:
            d_score += 1
            break
    # left
    l_score = 0
    for l in range(j_s):
        if grid[i_s][j_s - l - 1] < source:
            l_score += 1
        else:
            l_score += 1
            break

    # right
    r_score = 0
    for r in range(N - j_s - 1):
        if grid[i_s][j_s + r + 1] < source:
            r_score += 1
        else:
            r_score += 1
            break

    return u_score * d_score * l_score * r_score


print(grid)
scenic_scores = []

for i in range(N):
    for j in range(N):
        scenic_scores.append(rays(i, j))

print(max(scenic_scores))
