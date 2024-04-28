import regex as re


def part01(lines):
    value = 0

    for line in lines:
        winning_nums = set(line.split(":")[1].split("|")[0].split())
        nums = set(line.split(":")[1].split("|")[1].split())
        actual_wins = winning_nums & nums
        if actual_wins:
            value += 2 ** (len(actual_wins) - 1)

    return value


def part02(lines):
    value = 0

    return value


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.read().splitlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")
