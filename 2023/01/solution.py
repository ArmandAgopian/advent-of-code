import re

LETTER_DICT = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")


def part01(lines):
    value = 0
    for line in lines:
        value += int(
            re.search(r"\d", line).group() + re.search(r"\d", line[::-1]).group()
        )

    return value


def part02(lines):
    lines[:] = [re.sub(r"zero|one|two|three|four|five|six|seven|eight|nine", lambda x: LETTER_DICT.get(x.group()), line) for line in lines]
    print(lines)
    return part01(lines)


if __name__ == "__main__":
    main()
