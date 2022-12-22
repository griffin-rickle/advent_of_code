import json
import util


def get_priority(char: str) -> int:
    subtract: int = None
    if char.isupper():
        subtract = 38
    else:
        subtract = 96
    return ord(char) - subtract


def get_compartments(line: str) -> list[str]:
    size = int(len(line) / 2)
    return [line[0:size], line[size:len(line)]]


def get_common_item_types(compartments: list[str]) -> int:
    to_return: list = []
    c0 = set([*compartments[0]])
    c1 = set([*compartments[1]])

    for char in c0:
        if char in c1:
            to_return.append(char)

    return to_return

sacks = util.get_day_input(3)
compartments = [get_compartments(sack) for sack in sacks]
common_item_types = [get_common_item_types(compartment) for compartment in compartments]
print(sum([sum([get_priority(item_type) for item_type in common_item_type]) for common_item_type in common_item_types]))

