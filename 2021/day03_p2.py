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

def read_life_support_rating(inputs: List[str]) -> int:
    seq_length = len(inputs[0])

    o2_list = inputs.copy()
    for i in range(seq_length):
        N = len(o2_list)
        count = 0
        for inp in o2_list:
            count += int(inp[i])
        most_common = '1' if count/N >= 0.5 else '0'
        if len(o2_list) > 1:
            o2_list = [x for x in o2_list if x[i]==most_common]

    co2_list = inputs.copy()
    for i in range(seq_length):
        N = len(co2_list)
        count = 0
        for inp in co2_list:
            count += int(inp[i])
        least_common = '0' if count/N >= 0.5 else '1'
        if len(co2_list) > 1:
            co2_list = [x for x in co2_list if x[i]==least_common]

    return int(o2_list[0], base=2)*int(co2_list[0], base=2)

assert read_life_support_rating(TEST_INPUT)==230

print(read_life_support_rating(INPUT))
