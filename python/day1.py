from model import Elf
import util


def get_elves(input: list[str], blank_indeces: list[int]) -> list[Elf]:
    elves: list[Elf] = []
    idx: int = 0
    for end_idx in blank_indeces:
        elves.append(Elf([int(line) for line in lines[idx:end_idx]]))
        idx = end_idx + 1
    return elves


def get_most_calories(elves: list[Elf]) -> Elf:
    ret_elf: Elf = None
    for curr_elf in elves:
        if ret_elf is None or ret_elf.total_calories < curr_elf.total_calories:
            ret_elf = curr_elf
    return ret_elf

lines: list[str] = util.get_day_input(1)
blank_indeces: list[int] = [index for index, val in enumerate(lines) if val == '']
elves: list[Elf] = get_elves(lines, blank_indeces)
most_cal_elf: Elf = get_most_calories(elves)
print(most_cal_elf.total_calories)
