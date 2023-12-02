import functools
import re
import sys

digit_regex = re.compile('[0-9]')

spelled_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def get_spelled_digit(digit_string: str) -> tuple[str, int]:
    for spelled_digit in spelled_digits.keys():
        if digit_string[:len(spelled_digit)] == spelled_digit:
            return spelled_digits[spelled_digit], len(spelled_digit)
    return None, 0

def get_digits(string: str) -> str:
    digit_string = ''
    num_skip = 0

    for index, char in enumerate(string):
        if digit_regex.match(char):
            digit_string += char
        spelled_digit, num_skip = get_spelled_digit(string[index:])
        if spelled_digit is not None:
            digit_string += spelled_digit
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
