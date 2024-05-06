import regex as re

CARD_ORDER = ["1" "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def part01(lines):
    value = 0

    for line in lines:
        print(line.split()[0])
    return value


def part02(lines):
    value = 0

    return value


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.readlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")
