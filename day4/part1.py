#!/usr/bin/env python3


def get_points(line: str) -> int:
    match line.split('|'):
        case [winners, numbers]:
            winners = set([int(win) for win in winners.split(" ") if win != ""])
            numbers = set([int(number) for number in numbers.split(" ") if number != ""])
            match len(winners.intersection(numbers)):
                case 0: return 0
                case x: return 2 ** (x - 1)

        case _:
            assert False, "Unreachable, bad input"


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = sum([get_points(line.split(':')[1]) for line in file.readlines()[:-1]])
        print(result)
