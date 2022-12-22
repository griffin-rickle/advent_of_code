import json
import re
import util


move_re = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')

def parse_stacks(stacks: list[str]) -> dict[int, list[str]]:
    stack_nums = [int(stack_num) for stack_num in stacks[-1].split('   ')]
    crate_stacks = stacks[:len(stacks) - 1]

    stacks_dict = {}

    for stack_index, stack_num in enumerate(stack_nums):
        stack = ""
        stacks_dict[stack_num] = [crate_stack[stack_index * 3 + stack_num] for crate_stack in crate_stacks if (stack_index * 3 + stack_num) < len(crate_stack) if crate_stack[stack_index * 3 + stack_num] != ' ']

    return stacks_dict


def process_move(stacks_dict: dict[int, list[str]], move: str):
    # Top of the stacks are the front of the arrays
    match = move_re.match(move)
    num_to_move = int(match.group(1))
    from_stack = int(match.group(2))
    to_stack = int(match.group(3))

	# Take the needed subset of the array and reverse it
    top_stack = stacks_dict[from_stack][:num_to_move][::-1]
    # Remove them from the original stack
    stacks_dict[from_stack] = stacks_dict[from_stack][num_to_move:]
    # Put them on the front of the current stack
    top_stack.extend(stacks_dict[to_stack])
    stacks_dict[to_stack] = top_stack


lines = util.get_day_input_unstripped(5)
sep_index: int = 0

for index, val in enumerate(lines):
    if val == '':
        sep_index = index
        break

stacks: list[str] = lines[0:sep_index]
moves: list[str] = lines[sep_index + 1:]

stacks_dict = parse_stacks(stacks)
[process_move(stacks_dict, move) for move in moves]

answer_str = ""
for key, val in stacks_dict.items():
    answer_str += val[0]
print(answer_str)
