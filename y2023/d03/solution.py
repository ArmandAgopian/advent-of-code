import regex as re


def main():
    lines = []
    with open("./input.txt") as f:
        for line in f.read().splitlines():
            lines.append([*line])

    print(lines)
    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")


def part01(lines):
    value = 0

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            print(f"Part 01: {row}, {col}, {char}")

    return value


def part02(lines):
    value = 0

    return value


if __name__ == '__main__':
    main()
