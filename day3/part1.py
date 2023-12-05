#!/usr/bin/env python3


def is_symbol(c: str) -> bool:
    return not c.isnumeric() and c != '.'


class Number:
    def __init__(self, row, start, end, value):
        self.row = row
        self.start = start
        self.end = end
        self.value = value

    def is_valid(self, lines: list[str]):
        if self.row > 0:
            for i in range(self.start, self.end + 1):
                if is_symbol(lines[self.row - 1][i]):
                    return True
            if self.start > 0 and is_symbol(lines[self.row - 1][self.start - 1]):
                return True
            if self.end != len(lines[self.row - 1]) - 2 and is_symbol(lines[self.row - 1][self.end + 1]):
                return True

        if self.row < len(lines) - 2:
            for i in range(self.start, self.end + 1):
                if is_symbol(lines[self.row + 1][i]):
                    return True
            if self.start > 0 and is_symbol(lines[self.row + 1][self.start - 1]):
                return True
            if self.end != len(lines[self.row - 1]) - 2 and is_symbol(lines[self.row + 1][self.end + 1]):
                return True

        if self.start > 0 and is_symbol(lines[self.row][self.start - 1]):
            return True

        if self.end < len(lines[self.row]) - 2 and is_symbol(lines[self.row][self.end + 1]):
            return True

        return False


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        result = 0

        for row, line in enumerate(lines):
            current_number = 0
            current_start = 0
            for i, c in enumerate(line):
                if c.isnumeric():
                    if current_number == 0:
                        current_start = i
                    current_number = current_number * 10 + int(c)
                elif current_number != 0:
                    number = Number(row, current_start, i - 1, current_number)
                    if number.is_valid(lines):
                        result += number.value
                    current_number = 0

        print(result)
