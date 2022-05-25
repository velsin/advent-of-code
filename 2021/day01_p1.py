from typing import List

INPUT = []

TEST_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open('./data/day01.txt') as f:
    for line in f:
        INPUT.append(int(line.rstrip()))

def count_depth_increases(inputs: List[int]) -> int:
    " Count the number of times a measurement increases from the previous measurement. Return the count."
    count = 0
    previous = None
    for i in inputs:
        if previous and i > previous:
            count += 1
        previous = i
    return count

assert count_depth_increases(TEST_INPUT) == 7

print(count_depth_increases(INPUT))