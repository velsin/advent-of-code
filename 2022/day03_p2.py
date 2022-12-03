import string
from functools import reduce

filepath = "./data/day03.txt"
priorities = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))
group_size = 3
group_lines = []

with open(filepath) as f:

    score = 0
    group_score = 0

    for idx, line in enumerate(f.readlines()):

        if not idx % group_size:
            group_lines = []

        group_lines.append(set(line.strip()))

        first_half, second_half = line[: int(len(line) / 2)], line[int(len(line) / 2) :]

        common = set(first_half).intersection(set(second_half)).pop()
        score += priorities[common]

        if idx % group_size == group_size - 1:
            group_common = reduce(set.intersection, group_lines).pop()
            group_score += priorities[group_common]

print(score)
print(group_score)
