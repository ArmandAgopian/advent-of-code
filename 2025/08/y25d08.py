import operator
from functools import reduce
from pathlib import Path


def part1(puzzle: str) -> int:
    coords = puzzle.splitlines()

    for coord in coords:
        pass


def part2(puzzle: str) -> int:
    pass


if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input.txt").read_text()

    print(f"Part 1: {part1(puzzle)}")
    print(f"Part 2: {part2(puzzle)}")
