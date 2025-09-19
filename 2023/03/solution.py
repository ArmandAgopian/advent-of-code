import math
from pathlib import Path
import regex as re


def part1(lines):
    value = 0
    valid_parts = set()

    for i, line in enumerate(lines):
        for part in re.finditer(r"[^\d.]", line):
            valid_parts.add((i, part.start()))

    for i, line in enumerate(lines):
        for num in re.finditer(r"\d+", line):
            for row in range(i - 1, i + 2):
                for col in range(num.start() - 1, num.end() + 1):
                    if (row, col) in valid_parts:
                        value += int(num.group())

    return value


def part2(lines):
    value = 0
    valid_parts = {}

    for i, line in enumerate(lines):
        for gear in re.finditer(r"\*", line):
            valid_parts[(i, gear.start())] = []

    for i, line in enumerate(lines):
        for num in re.finditer(r"\d+", line):
            for row in range(i - 1, i + 2):
                for col in range(num.start() - 1, num.end() + 1):
                    if (row, col) in valid_parts:
                        valid_parts[(row, col)].append(int(num.group()))

    for part in valid_parts.values():
        if len(part) == 2:
            value += math.prod(part)
    return value


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
