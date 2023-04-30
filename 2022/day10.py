from typing import List

filepath = "./data/day10.txt"


def parse_input(filepath: str) -> List[str]:
    with open(filepath) as f:
        data = [line.split() for line in f.readlines()]
    return data


def calculate_signal_strength(instructions: List[str]) -> int:
    # create a queue of some kind to parse the inputs.
    Q = []
    register = 1
    signal_strength = []
    cycle = 1

    for line in instructions:
        # parse instruction
        match line[0]:
            case "noop":
                Q.append(None)
            case "addx":
                Q.append(None)
                Q.append(int(line[1]))

    # parse Q and execute the cycles
    for command in Q:
        if command:
            register += command
        cycle += 1

        if (cycle - 20) % 40 == 0:
            signal_strength.append(cycle * register)

    return sum(signal_strength)


print(calculate_signal_strength(parse_input(filepath)))
