

with open('./data/day01.txt') as f:
    max = [0]
    counter = 0

    for line in f.read().splitlines():
        if line:
            counter += int(line)
        else:
            if any(counter > x for x in max):
                max.append(counter)
                max.sort()
            if len(max) > 3:
                max.pop(0)
            counter = 0

print(sum(max))



