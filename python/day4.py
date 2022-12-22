import util

lines: list[str] = util.get_day_input(4)
elf_sections: list[list[str]] = [entry.split(',') for entry in lines]

count: int = 0
for pairing in elf_sections:
    l_low = int(pairing[0].split('-')[0])
    l_high = int(pairing[0].split('-')[1])

    r_low = int(pairing[1].split('-')[0])
    r_high = int(pairing[1].split('-')[1])

    if (l_low <= r_low and l_high >= r_high) or (r_low <= l_low and r_high >= l_high):
        count += 1

print(count)
