from pathlib import Path

import regex as re


def part1(puzzle: str) -> int:
    value = 0
    for pair in puzzle.split(','):
        start, end = map(int, pair.split('-'))

        for num in range(start, end + 1):
            if str(num)[: len(str(num)) // 2] == str(num)[len(str(num)) // 2 :]:
                value += num

    return value


def part2(puzzle: str) -> int:
    value = 0
    for pair in puzzle.split(','):
        start, end = map(int, pair.split('-'))

        for num in range(start, end + 1):
            if re.match(r'^(\d+)\1+$', str(num)):
                value += num

    return value


if __name__ == '__main__':
    puzzle = (Path(__file__).parent / 'input.txt').read_text()

    print(f'Part 1: {part1(puzzle)}')
    print(f'Part 2: {part2(puzzle)}')
