from typing import List

INPUT = []

TEST_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open('./data/day01.txt') as f:
    for line in f:
        INPUT.append(int(line.rstrip()))

def count_depth_increases(inputs: List[int]) -> int:
    " Count the number of times the 3-index window increases from the previous window. Return the count."
    count = 0
    prev_window = None
    for i in range(len(inputs)-2):
        # could maybe make a negligable speed improvement by adding next point and removing oldest, instead of reslicing?
        # bigger improvement is only comparing entering and exiting element!
        window = sum(inputs[i:i+3])
        if prev_window and window > prev_window:
            count += 1
        prev_window = window
    return count

assert count_depth_increases(TEST_INPUT) == 5

print(count_depth_increases(INPUT))