import string

filepath = "./data/day03.txt"
priorities = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))

with open(filepath) as f:

    score = 0

    for line in f.readlines():
        first_half, second_half = line[: int(len(line) / 2)], line[int(len(line) / 2) :]

        common = set(first_half).intersection(set(second_half)).pop()
        score += priorities[common]

print(score)
