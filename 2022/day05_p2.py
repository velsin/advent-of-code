from collections import deque

filepath = "./data/day05.txt"

box_config = True

with open(filepath) as f:

    box_config, instruction = f.read().split("\n\n")

    box_config_lines = box_config.split("\n")
    instruction_lines = instruction.rstrip().split("\n")

    n_boxes = (len(box_config_lines[0]) + 1) // 4
    box_stacks = {i + 1: deque() for i in range(n_boxes)}

    for line in box_config_lines:
        for i in range(n_boxes):
            box = line[(4 * i) + 1]
            if box != " " and box not in list(map(str, range(10))):
                box_stacks[i + 1].append(line[(4 * i) + 1])

    for line in instruction_lines:
        line_split = line.split(" ")

        n, from_stack, to_stack = [int(line_split[i]) for i in (1, 3, 5)]

        crate_stack = []
        for i in range(n):
            crate_stack.append(box_stacks[from_stack].popleft())
        for i in range(n):
            box_stacks[to_stack].appendleft(crate_stack.pop())

print(box_stacks)

print([x[0] for x in box_stacks.values()])
