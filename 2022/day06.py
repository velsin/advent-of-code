from collections import deque

filepath = "./data/day06.txt"

with open(filepath) as f:
    input = f.readlines()  # single long string

input_string = input[0].rstrip()
print(input_string)
max_length = 4
Q = deque()

for idx, char in enumerate(input_string):

    if len(Q) < 4:
        Q.append(char)

    else:
        Q.append(char)
        Q.popleft()

    # print(Q)

    n_unique = len(set(Q))
    if n_unique == 4:
        print(idx + 1)
        break
