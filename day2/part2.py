#!/usr/bin/env python3


def get_power(line: str) -> float:
    min_values = {
        'red': float('-inf'),
        'green': float('-inf'),
        'blue': float('-inf'),
    }
    for test in line.split(';'):
        for color in test.split(','):
            color = color.split(' ')
            color_name = color[2].strip()
            color_value = float(color[1])
            min_values[color_name] = max(color_value, min_values[color_name])
    return min_values['red'] * min_values['green'] * min_values['blue']


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = sum([get_power(line.split(':')[1]) for line in file.readlines()])
        print(int(result))
