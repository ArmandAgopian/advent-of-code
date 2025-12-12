import regex as re
from pathlib import Path

def part1(input):
    grid = [list(row) for row in input.splitlines()]
    start = (0, 0)
    seen = set()

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 'S':
                start = (i, j)

    curr1 = start
    curr2 = start
    while (curr1 not in seen) and (curr2 not in seen):
        seen.add(curr1)
        seen.add(curr2)

    return NotImplementedError

def part2(input):
    return NotImplementedError

if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
