# Cleaned up solution
from typing import List


def read_input(path: str) -> List[str]:
    with open(path) as f:
        input_lines = f.readlines()
    return input_lines


def calculate_score(input_lines: List[str], scoring_dict_choice: int) -> int:

    scoring_dicts = [
        {
            ("A", "X"): 4,
            ("A", "Y"): 8,
            ("A", "Z"): 3,
            ("B", "X"): 1,
            ("B", "Y"): 5,
            ("B", "Z"): 9,
            ("C", "X"): 7,
            ("C", "Y"): 2,
            ("C", "Z"): 6,
        },
        {
            ("A", "X"): 3,
            ("A", "Y"): 4,
            ("A", "Z"): 8,
            ("B", "X"): 1,
            ("B", "Y"): 5,
            ("B", "Z"): 9,
            ("C", "X"): 2,
            ("C", "Y"): 6,
            ("C", "Z"): 7,
        },
    ]

    score = 0

    for line in input_lines:
        opp, you = line.split()
        score += scoring_dicts[scoring_dict_choice][(opp, you)]

    return score


assert calculate_score(read_input("./data/day02_test.txt"), 0) == 15
assert calculate_score(read_input("./data/day02_test.txt"), 1) == 12

print(calculate_score(read_input("./data/day02.txt"), 0))
print(calculate_score(read_input("./data/day02.txt"), 1))
