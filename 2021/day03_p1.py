from typing import List

RAW = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

INPUT = []
TEST_INPUT = [x for x in RAW.rstrip().split()]

with open('./data/day03.txt') as f:
    INPUT = [x.rstrip() for x in f.readlines()]

def read_power_consumption(inputs: List[str]) -> int:
    N = len(inputs)
    counter_list = [0 for x in range(len(inputs[0]))]

    for inp in inputs:
        for j in range(len(counter_list)):
            counter_list[j] += int(inp[j])

    gamma = ''
    epsilon = ''

    for x in counter_list:
        if x/N >= 0.5:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, base=2)*int(epsilon, base=2)

assert read_power_consumption(TEST_INPUT)==198

print(read_power_consumption(INPUT))
