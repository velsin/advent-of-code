# Cleaned up solution
from typing import List


def read_input(path: str) -> List[str]:
    with open(path) as f:
        input_lines = f.read().split("\n")
    return input_lines


def sum_of_top_n(input: List[str], n: int) -> int:
    top_n_values = [0]
    total = 0

    for line in input:

        if line:
            total += int(line)

        else:
            if any(total > value for value in top_n_values):
                top_n_values.append(total)
                top_n_values.sort()
            if len(top_n_values) > n:
                top_n_values.pop(0)
            total = 0

    return sum(top_n_values)


assert sum_of_top_n(read_input("./data/day01_test.txt"), n=1) == 24000
assert sum_of_top_n(read_input("./data/day01_test.txt"), n=3) == 45000

print(sum_of_top_n(read_input("./data/day01.txt"), n=1))
print(sum_of_top_n(read_input("./data/day01.txt"), n=3))
