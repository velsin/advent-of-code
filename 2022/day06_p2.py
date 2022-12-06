from collections import deque

filepath = "./data/day06.txt"

with open(filepath) as f:
    input = f.readlines()  # single long string

input_string = input[0].rstrip()
print(input_string)
max_length = 14
Q = deque()

for idx, char in enumerate(input_string):

    if len(Q) < max_length:
        Q.append(char)

    else:
        Q.append(char)
        Q.popleft()

    # print(Q)

    n_unique = len(set(Q))
    if n_unique == max_length:
        print(idx + 1)
        break
