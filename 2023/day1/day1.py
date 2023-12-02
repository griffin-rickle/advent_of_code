import functools
import re
import sys

digit_regex = re.compile('[0-9]')

def get_digits(string: str) -> str:
    digit_string = ''
    for char in string:
        if digit_regex.match(char):
            digit_string += char
    return digit_string

def get_calibration_number(digit_string: str) -> int:
    return int(digit_string[0] + digit_string[-1])

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.read().splitlines()

calibration_numbers = [get_calibration_number(get_digits(line))
                       for line in lines]
summed_calibrations = functools.reduce(lambda a, b: a + b, calibration_numbers)

print('Summed calibration numbers:', summed_calibrations)
