#!/usr/bin/env python3


def get_number_from_line(line: str) -> int:
    digits = [int(c) for c in line if c.isnumeric()]
    match len(digits):
        case 0: return 0
        case _: return digits[0] * 10 + digits[-1]


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = sum([get_number_from_line(line) for line in file.readlines()])
        print(result)
