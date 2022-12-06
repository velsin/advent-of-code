filepath = "./data/day04.txt"

with open(filepath) as f:

    inclusions = 0

    for line in f.readlines():

        elf1, elf2 = line.strip().split(",")
        elf1_interval = list(map(int, elf1.split("-")))
        elf2_interval = list(map(int, elf2.split("-")))

        elf1_set = set(range(elf1_interval[0], elf1_interval[1] + 1))
        elf2_set = set(range(elf2_interval[0], elf2_interval[1] + 1))

        if elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set):
            inclusions += 1


print(inclusions)
