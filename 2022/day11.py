import re
from collections import deque
from functools import reduce
from operator import mul
from typing import Any, Dict, List

filepath = "./data/day11.txt"


def parse_input(filepath: str) -> List[str]:
    with open(filepath) as f:
        data = f.read().split("\n\n")  # each element of data is a monkeyspec

    return data


class Monkey:
    monkey_dict = {}  # keep track of all monkeys created, must have unique ids
    lcm = None

    @classmethod
    def inventory_status(cls):
        for id, monkey in cls.monkey_dict.items():
            print(f"Monkey {id}", monkey.items)

    @classmethod
    def play_round(cls):
        # On the first round, compute lcm
        if not cls.lcm:
            cls.find_lcm()

        for monkey in cls.monkey_dict.values():
            monkey.play_turn()
        cls.inventory_status()

    @classmethod
    def find_lcm(cls):
        # lcm will just be product since the test divisors are prime
        lcm = 1
        for monkey in cls.monkey_dict.values():
            lcm *= monkey.test_divisor
        cls.lcm = lcm

    def __init__(self, monkey_spec, part):
        parsed_spec = self.parse_specification(monkey_spec)

        self.id = parsed_spec["id"]
        self.items = parsed_spec["items"]
        self.operation = parsed_spec["operation"]
        self.test = parsed_spec["test"]
        self.test_divisor = parsed_spec["test_divisor"]
        self.if_true = parsed_spec["if_true"]
        self.if_false = parsed_spec["if_false"]

        self.inspections = 0
        self.part = part

        # Add self to the monkey dict
        Monkey.monkey_dict[self.id] = self

    def parse_specification(self, monkey_spec: List[str]) -> Dict[str, Any]:
        # 1st: id, 2nd: items, 3rd: op, 4th: test, 5th: T, 6th: F
        spec = [line.strip() for line in monkey_spec.split("\n")]

        return {
            "id": re.search(r"\d", spec[0])[0],
            "items": deque([int(x) for x in re.findall(r"\d+", spec[1])]),
            # build a function from the text with eval !
            "operation": lambda x: eval(
                re.match(r".+=\s*(.*)", spec[2])[1], {"old": x}
            ),
            "test": lambda x: (x % int(re.search(r"\d+", spec[3])[0])) == 0,
            "test_divisor": int(re.search(r"\d+", spec[3])[0]),
            "if_true": re.search(r"\d+", spec[4])[0],
            "if_false": re.search(r"\d+", spec[5])[0],
        }

    def play_turn(self):
        # Go through the list of items until empty
        # print(f"Monkey {self.id} turn")
        while self.items:
            item_worry = self.items.popleft()
            self.inspections += 1
            # print("grabbing item with worry", item_worry)

            if self.part == 1:
                new_worry = self.operation(item_worry) // 3
            elif self.part == 2:
                new_worry = self.operation(item_worry) % Monkey.lcm
            # print("new worry", new_worry)

            if self.test(new_worry):
                # print("true, passing item to", self.if_true)
                Monkey.monkey_dict[self.if_true].items.append(new_worry)
            else:
                # print("false, passing item to", self.if_false)
                Monkey.monkey_dict[self.if_false].items.append(new_worry)


def part_1():
    # Create Critters
    for monkey_spec in parse_input(filepath):
        Monkey(monkey_spec=monkey_spec, part=1)

    # Simulate Simian Shenanigans
    n_rounds = 20
    for i in range(n_rounds):
        print("ROUND ", i + 1)
        Monkey.play_round()

    # Report Results
    for id, monkey in Monkey.monkey_dict.items():
        print(f"Monkey {id} had {monkey.inspections} inspections.")

    monkey_business = reduce(
        mul,
        (sorted([monkey.inspections for monkey in Monkey.monkey_dict.values()]))[-2:],
    )

    print("Result:", monkey_business)


def part_2():
    # Create Critters
    for monkey_spec in parse_input(filepath):
        Monkey(monkey_spec=monkey_spec, part=2)

    # Simulate Simian Shenanigans
    n_rounds = 10000
    for i in range(n_rounds):
        print("ROUND ", i + 1)
        Monkey.play_round()

    # Report Results
    for id, monkey in Monkey.monkey_dict.items():
        print(f"Monkey {id} had {monkey.inspections} inspections.")

    monkey_business = reduce(
        mul,
        (sorted([monkey.inspections for monkey in Monkey.monkey_dict.values()]))[-2:],
    )

    print("Result:", monkey_business)


# part_1()
part_2()
