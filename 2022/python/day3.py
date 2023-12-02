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


def get_common_sack_items(sacks: list[str]) -> list[str]:
    common_items = []
    sack_sets: list[set] = []
    for sack in sacks:
        sack_sets.append(set([*sack]))

    for sack_item in sack_sets[0]:
        if sack_item in sack_sets[1] and sack_item in sack_sets[2]:
            common_items.append(sack_item)

    return common_items


sacks = util.get_day_input(3)
compartments = [get_compartments(sack) for sack in sacks]
common_item_types = [get_common_item_types(compartment) for compartment in compartments]

print("Part 1:")
print(sum([sum([get_priority(item_type) for item_type in common_item_type]) for common_item_type in common_item_types]))

print("Part 2:")
common_items = [get_common_sack_items(sacks[start_idx:start_idx + 3]) for start_idx in range(0, len(sacks), 3)]
print(sum([get_priority(common_item[0]) for common_item in common_items]))
