import regex as re

CARD_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def part01(lines):
    value = 0
    ranks = {}

    return value


def part02(lines):
    value = 0

    return value


from collections import Counter

def char_count(s: str) -> dict:
    return dict(Counter(s))

# Example usage
s = "aabbc"
result = char_count(s)
print(result)
    with open("./input.txt") as f:
        lines = f.readlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")
