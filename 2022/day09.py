from collections import defaultdict
from typing import List, Tuple

filepath = "./data/day09.txt"


def parse_input(filepath):
    with open(filepath, "r") as f:
        input = [line.strip() for line in f.readlines()]
    return input


# go through each command, move head step by step, and move tail to follow, record tail visits
def move_tail(head_pos: Tuple[int], tail_pos: Tuple[int]) -> Tuple[int]:
    # update the tail position for a given head and tail position
    dx = head_pos[0] - tail_pos[0]
    dy = head_pos[1] - tail_pos[1]

    if (dx**2 + dy**2) ** 0.5 < 2:
        # still touching
        return tail_pos
    elif abs(dx) >= 1 and dy == 0:
        return (int(tail_pos[0] + (dx / abs(dx))), tail_pos[1])
    elif dx == 0 and abs(dy) >= 1:
        return (tail_pos[0], int(tail_pos[1] + (dy / abs(dy))))
    else:
        # diagonal move
        return (int(tail_pos[0] + (dx / abs(dx))), int(tail_pos[1] + (dy / abs(dy))))


def find_tail_path(input_list: List[str]):
    # start at origin, iterate through instructions, and move step by step
    tail_visited = defaultdict(int)
    head_pos, tail_pos = (0, 0), (0, 0)
    tail_visited[tail_pos] += 1

    for row in input_list:
        direction, distance = row.split()
        # print(direction, distance)
        for _ in range(int(distance)):
            match direction:
                case "R":
                    head_pos = (head_pos[0] + 1, head_pos[1])
                    tail_pos = move_tail(head_pos, tail_pos)
                    tail_visited[tail_pos] += 1
                case "L":
                    head_pos = (head_pos[0] - 1, head_pos[1])
                    tail_pos = move_tail(head_pos, tail_pos)
                    tail_visited[tail_pos] += 1
                case "U":
                    head_pos = (head_pos[0], head_pos[1] + 1)
                    tail_pos = move_tail(head_pos, tail_pos)
                    tail_visited[tail_pos] += 1
                case "D":
                    head_pos = (head_pos[0], head_pos[1] - 1)
                    tail_pos = move_tail(head_pos, tail_pos)
                    tail_visited[tail_pos] += 1

            # print("head:", head_pos)
            # print("tail:", tail_pos)

    return len(tail_visited.keys())


print(parse_input(filepath))

print(find_tail_path(parse_input(filepath)))
