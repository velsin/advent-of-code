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

    @classmethod
    def inventory_status(cls):
        for id, monkey in cls.monkey_dict.items():
            print(f"Monkey {id}", monkey.items)

    @classmethod
    def play_round(cls):
        for monkey in cls.monkey_dict.values():
            monkey.play_turn()
        cls.inventory_status()

    def __init__(self, monkey_spec):
        parsed_spec = self.parse_specification(monkey_spec)

        self.id = parsed_spec["id"]
        self.items = parsed_spec["items"]
        self.operation = parsed_spec["operation"]
        self.test = parsed_spec["test"]
        self.if_true = parsed_spec["if_true"]
        self.if_false = parsed_spec["if_false"]

        self.inspections = 0

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

            new_worry = self.operation(item_worry) // 3
            # print("new worry", new_worry)

            if self.test(new_worry):
                # print("true, passing item to", self.if_true)
                Monkey.monkey_dict[self.if_true].items.append(new_worry)
            else:
                # print("false, passing item to", self.if_false)
                Monkey.monkey_dict[self.if_false].items.append(new_worry)


# Create Critters
for monkey_spec in parse_input(filepath):
    Monkey(monkey_spec=monkey_spec)

# Simulate Simian Shenanigans
n_rounds = 20
for i in range(n_rounds):
    print("ROUND ", i + 1)
    Monkey.play_round()

# Report Results
for id, monkey in Monkey.monkey_dict.items():
    print(f"Monkey {id} had {monkey.inspections} inspections.")

monkey_business = reduce(
    mul, (sorted([monkey.inspections for monkey in Monkey.monkey_dict.values()]))[-2:]
)
print("Result:", monkey_business)
