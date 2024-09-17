DIGITMAP = {
    "zero": 0,
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
from math import log
import sys

def convert_numbers(items):
    numbers = ''
    x=-1
    try:
        for digit in items:
            numbers += DIGITMAP[digit]
        
        x =int(numbers)
    except (KeyError, TypeError) as e:
        print(f"Couldn't convert {e!r}")
        file = sys.stderr
        raise
    

    return x


def string_log(s):
    v = convert_numbers(s)
    log_of_s = log(v)
    return log_of_s

