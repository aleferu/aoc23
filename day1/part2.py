#!/usr/bin/env python3


def modify_line(line: str) -> str:
    return (line.replace("one", "one1one")
                .replace("two", "two2two")
                .replace("three", "three3three")
                .replace("four", "four4four")
                .replace("five", "five5five")
                .replace("six", "six6six")
                .replace("seven", "seven7seven")
                .replace("eight", "eight8eight")
                .replace("nine", "nine9nine"))


def get_number_from_line(line: str) -> int:
    digits = [int(c) for c in modify_line(line) if c.isnumeric()]
    match len(digits):
        case 0: return 0
        case _: return digits[0] * 10 + digits[-1]


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = sum([get_number_from_line(line) for line in file.readlines()])
        print(result)
