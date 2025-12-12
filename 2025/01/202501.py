from pathlib import Path
import regex as re

def part1(input):
    value = 50
    for line in input.splitlines():
        if line[0] == 'L':
            value = (value - int(line[1:])) % 100
        elif line[0] == 'R':
            value = (value + int(line[1:])) % 100
        
    return value


def part2(input):
    return NotImplementedError


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        input = f.read()

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
