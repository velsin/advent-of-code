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
    N = len(inputs)

    oxy_counter = [0 for x in range(seq_length)]
    c02_counter = [0 for x in range(seq_length)]

    oxy = ''
    c02 = ''

    for i in range(seq_length):
        for inp in inputs:
            


    


    for x in counter_list:
        if x/N >= 0.5:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, base=2)*int(epsilon, base=2)

assert read_life_support_rating(TEST_INPUT)==230

print(read_power_consumption(INPUT))
