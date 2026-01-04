import math
from pathlib import Path


def part1(puzzle: str) -> int:
    coords = puzzle.splitlines()

    for coord in coords:
        for coord2 in coords:
            point = coord.split(',')
            point2 = coord2.split(',')
            distance = math.dist(point, point2)


def part2(puzzle: str) -> int:
    pass


if __name__ == '__main__':
    puzzle = (Path(__file__).parent / 'input.txt').read_text()

    print(f'Part 1: {part1(puzzle)}')
    print(f'Part 2: {part2(puzzle)}')
