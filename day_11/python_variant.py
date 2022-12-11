from __future__ import annotations
from typing import List, Tuple
import re
import math


def parse_input(str_array):
    monkeys = []
    curr_monkey = None
    for i, line in enumerate(str_array):
        line = line.strip().split()
        if len(line) < 1:
            continue
        if line[0] == "Monkey":
            if curr_monkey is not None:
                monkeys.append(curr_monkey)
            curr_monkey = Monkey()
        elif line[0] == "Starting":
            curr_monkey.items = list(
                map(lambda x: int(re.sub("[^0-9]", "", x)), line[2:]))
        elif line[0] == "Operation:":
            curr_monkey.oper_func = line[4:]
        elif line[0] == "Test:":
            curr_monkey.divide_val = int(line[-1])
        elif line[1] == "true:":
            curr_monkey.targets[1] = int(line[-1])
        elif line[1] == "false:":
            curr_monkey.targets[0] = int(line[-1])
    if curr_monkey is not None:
        monkeys.append(curr_monkey)
    return monkeys


class Monkey:
    def __init__(self, starting_items=None, operation_func=None, divide_val=None, true_monkey=None, false_monkey=None):
        self.items: List[int] = starting_items
        self.oper_func: List[str] = operation_func
        self.divide_val: int = divide_val
        self.targets: Tuple[int] = [false_monkey, true_monkey]
        self.times_inspected: int = 0

    def stringify(self, num):
        return f'Monkey {num}:\n  Items: {self.items}\n  Operation: new = old {self.oper_func[0]} {self.oper_func[1]}\n  Test: divisible by {self.divide_val}\n    If true: throw to monkey {self.true_monkey}\n    If false: throw to monkey {self.false_monkey}\n  Times Inspected: {self.times_inspected}'


'''
nums = [3, 2, 4, 56]

lcm = math.prod(nums)

print("LCM: ", lcm)
val = 165165165191
for num in nums:
    print(f"{val} % {num} = {val%num}")


new_val = val % lcm
for num in nums:
    print(f"{new_val} % {num} = {new_val%num}")

'''


def get_monkey_business(monkeys: List[Monkey], rounds: int, is_relieved: bool):
    lcm = math.prod(m.divide_val for m in monkeys)
    for i in range(rounds):
        # print(f"round {i}", end="\r")
        for j, monkey in enumerate(monkeys):
            for item in monkey.items:
                print(f"round {i}, monkey {j}, item: {item}", end="\r")
                monkey.times_inspected += 1
                oper_val = item
                if monkey.oper_func[1] != "old":
                    oper_val = int(monkey.oper_func[1])
                if monkey.oper_func[0] == "*":
                    item = item * oper_val
                else:
                    item = item + oper_val

                if is_relieved:
                    item = item // 3
                else:
                    # Remainder of mod with lcm is enough to find if divisible by any of the divide_vals
                    item = item % lcm

                monkeys[monkey.targets[item %
                                       monkey.divide_val == 0]].items.append(item)
            monkey.items.clear()
    print("")
    monkeys.sort(key=lambda x: x.times_inspected)

    print(monkeys[-1].times_inspected * monkeys[-2].times_inspected)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = input_file.readlines()
        monkeys: List[Monkey] = parse_input(lines)

    get_monkey_business(monkeys, 10000, False)
