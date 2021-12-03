from typing import Tuple, List

INPUT = []
TEST_INPUT = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]

with open('./inputs/day02.txt') as f:
    for line in f:
        l = line.rstrip().split()
        INPUT.append((l[0], int(l[1])))

def count_position_and_depth_with_aim(inputs: List[Tuple[str, int]]) -> int:
    pos = 0
    depth = 0
    aim = 0

    for com in inputs:
        if com[0] == 'forward':
            pos += com[1]
            depth += aim*com[1]
        elif com[0] == 'down':
            aim += com[1]
        else:
            aim -= com[1]

    return pos*depth

assert (count_position_and_depth_with_aim(TEST_INPUT) == 900)

print(count_position_and_depth_with_aim(INPUT))