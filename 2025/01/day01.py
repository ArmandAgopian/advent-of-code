from pathlib import Path
import regex as re

LETTER_DICT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def part1(lines):
    value = 0
    for line in lines:
        value += int(
            re.search(r"\d", line).group() + re.search(r"\d", line[::-1]).group()
        )

    return value


def part2(lines):
    value = 0
    for line in lines:
        matches = re.findall(
            r"\d|zero|one|two|three|four|five|six|seven|eight|nine",
            line,
            overlapped=True,
        )
        value += (LETTER_DICT[matches[0]] * 10) + LETTER_DICT[matches[-1]]

    return value


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
