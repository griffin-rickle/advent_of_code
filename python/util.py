import os

def get_day_input_unstripped(day: int) -> list[str] :
    filename = os.path.sep.join(['inputs', 'day' + str(day) + '.txt'])
    return get_lines(filename, stripped=False)

def get_day_input(day: int) -> list[str] :
    filename = os.path.sep.join(['inputs', 'day' + str(day) + '.txt'])
    return get_lines(filename)


def get_lines(filename: str, stripped: bool=True) -> list[str] :
    with open(filename) as f:
        lines = [line for line in f.readlines()]
        if stripped is True:
            lines = [line.strip() for line in lines]
        else:
            lines = [line.replace('\n', '') for line in lines]

    return lines

