#!/usr/bin/env python3


def is_valid(line: str, max_red=12.0, max_green=13.0, max_blue=14.0) -> bool:
    max_values = {
        'red': max_red,
        'green': max_green,
        'blue': max_blue,
    }
    for test in line.split(';'):
        for color in test.split(','):
            color = color.split(' ')
            color_name = color[2].strip()
            color_value = float(color[1])
            if color_value > max_values[color_name]:
                return False
    return True


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = 0
        for i, line in enumerate(file.readlines()):
            if line == "":
                continue
            if is_valid(line.split(':')[1]):
                result += i + 1
        print(result)
