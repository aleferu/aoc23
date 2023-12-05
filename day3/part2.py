#!/usr/bin/env python3


class Number:
    def __init__(self, row, start, end, value):
        self.row = row
        self.start = start
        self.end = end
        self.value = value


class Asterisk:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.values = []

    def add_value_from_number(self, number: Number):
        if abs(self.row - number.row) < 2 and number.start - 1 <= self.col <= number.end + 1:
            self.values.append(number.value)

    def get_value_if_valid(self):
        return self.values[0] * self.values[1] if len(self.values) == 2 else -1


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        numbers = []
        asterisks = []
        for row, line in enumerate(lines):
            current_number = 0
            current_start = 0
            for i, c in enumerate(line):
                if c.isnumeric():
                    if current_number == 0:
                        current_start = i
                    current_number = current_number * 10 + int(c)
                else:
                    if current_number != 0:
                        numbers.append(Number(row, current_start, i - 1, current_number))
                        current_number = 0
                    if c == '*':
                        asterisks.append(Asterisk(row, i))

        result = 0
        for asterisk in asterisks:
            for number in numbers:
                asterisk.add_value_from_number(number)
            match asterisk.get_value_if_valid():
                case -1: continue
                case value: result += value

        print(result)
