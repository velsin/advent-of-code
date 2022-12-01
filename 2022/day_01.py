

with open('./data/day01.txt') as f:
    max = 0
    counter = 0

    for line in f.read().splitlines():
        if line:
            counter += int(line)
        else:
            if counter > max:
                max = counter
            counter = 0

print(max)



