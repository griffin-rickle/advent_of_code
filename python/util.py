import os

def get_day_input(day: int) -> list[str] :
    filename = os.path.sep.join(['inputs', 'day' + str(day) + '.txt'])
    return get_lines(filename)


def get_lines(filename: str) -> list[str] :
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

