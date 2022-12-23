import json
import re
import util


def get_dir_contents(data: list[str], start_index: int) -> (int, dict):
    curr_index = start_index + 1
    cmd_re = re.compile('\$.*')
    while curr_index < len(data) and cmd_re.match(data[curr_index]) is None:
        curr_index += 1

    to_return = { 'files':{}, 'dirs': []}
    for content in data[start_index + 1:curr_index]:
        split_content = content.split(' ')
        if split_content[0] == 'dir':
            to_return['dirs'].append(split_content[1])
        else:
            to_return['files'][split_content[1]] = int(split_content[0])
    return curr_index, to_return


def parse_file_structure(data: list[str]) -> dict:
    file_structure: dict = {}
    cwd: list[str] = ''
    curr_counter = 0
    entry = data[curr_counter]
    while curr_counter < len(data):
        split_line = entry.split(' ')
        if split_line[0] == '$':
            if split_line[1] == 'ls':
                curr_counter, dir_contents = get_dir_contents(data, curr_counter)
                file_structure[cwd] = dir_contents
            elif split_line[1] == 'cd':
                cwd = split_line[2]
                curr_counter += 1
        if curr_counter < len(data):
            entry = data[curr_counter]
    return file_structure


def get_dir_size(fs, directory):
    total = 0
    if directory not in fs.keys():
        return 0
    for file, size in fs[directory]['files'].items():
        total += size
    for subdir in fs[directory]['dirs']:
        total += get_dir_size(fs, subdir)
    return total

lines = util.get_day_input(7)
fs = parse_file_structure(lines)


sizes = {}
for directory in fs.keys():
    file_size = get_dir_size(fs, directory)
    sizes[directory] = get_dir_size(fs, directory)
    # if file_size <= 100000:
    print(f'{directory} {file_size}')
    print(json.dumps(fs[directory], indent=4))

print(sum([sizes[directory] for directory in sizes.keys() if sizes[directory] <= 100000]))
