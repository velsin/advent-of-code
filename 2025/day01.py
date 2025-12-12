from dataclasses import dataclass
from os import read
from typing import Literal
from pathlib import Path

DATA_PATH = Path("./data/day01.txt")

TEST_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


@dataclass
class Rotation:
    direction: int
    size: int

    def __post_init__(self):
        if self.direction not in (1, -1):
            raise ValueError("Invalid direction, must be either 1 or -1")


class Dial:
    def __init__(self):
        self.position: int = 50
        self.counter: int = 0

    def turn(self, rot: Rotation):
        self.position = (self.position + (rot.direction * rot.size)) % 100
        if self.position == 0:
            self.counter += 1

    def turn_2(self, rot: Rotation):
        # Alternate turning method for part 2
        # print(rot)
        delta = rot.direction * rot.size
        new_pos = delta + self.position
        old_pos = self.position
        self.position = new_pos % 100
        if rot.direction == 1:
            self.counter += new_pos // 100
        else:
            # Create a compensator for starting on 0
            self.counter += ((old_pos - 1) // 100) - ((new_pos - 1) // 100)
        # print("new:", new_pos)
        # print("pos", self.position)
        # print("c:", self.counter)

    def turn_2_naive(self, rot: Rotation):
        for _ in range(rot.size):
            self.position = (self.position + rot.direction) % 100
            if self.position == 0:
                self.counter += 1


def parse_input(t: str) -> list[Rotation]:
    map = {"R": 1, "L": -1}
    commands = []
    for line in t.splitlines():
        commands.append(Rotation(map[line[0]], int(line[1:])))

    return commands


def part1(inp: list[Rotation]) -> int:
    d = Dial()
    for c in inp:
        d.turn(c)

    return d.counter


def part2(inp: list[Rotation]) -> int:
    d = Dial()
    for c in inp:
        d.turn_2(c)

    return d.counter


if __name__ == "__main__":
    assert part1(parse_input(TEST_INPUT)) == 3

    print("x", part2(parse_input(TEST_INPUT)))
    assert part2(parse_input(TEST_INPUT)) == 6

    with open(DATA_PATH, "r") as f:
        input = f.read().strip()

    inp = parse_input(input)
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
