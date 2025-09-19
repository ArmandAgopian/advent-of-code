from pathlib import Path
import regex as re
from collections import Counter

CARD_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def part1(lines):
    value = 0
    ranks = {}

    #def char_count(s: str) -> dict:
    #    return dict(Counter(s))

    return value


def part2(lines):
    value = 0

    return value

if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
