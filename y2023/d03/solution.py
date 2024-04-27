import regex as re


# FIXME: Messy solution, refactor needed
def part01(lines):
    value = 0
    valid_parts = set()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not re.search(r"\d|\.", char):
                valid_parts.add((row - 1, col + 1))
                valid_parts.add((row - 1, col))
                valid_parts.add((row - 1, col - 1))
                valid_parts.add((row, col + 1))
                valid_parts.add((row, col))
                valid_parts.add((row, col - 1))
                valid_parts.add((row + 1, col + 1))
                valid_parts.add((row + 1, col))
                valid_parts.add((row + 1, col - 1))

    for row, line in enumerate(lines):
        nums = set()
        for col, char in enumerate(line):
            if re.search(r"\d", char) and (row, col) in valid_parts:
                if (row, col) in nums:
                    continue
                num = char
                nums.add((row, col))

                try:
                    counter = 1
                    while re.search(r"\d", line[col - counter]):
                        if col - counter < 0:
                            break
                        num = line[col - counter] + num
                        nums.add((row, col - counter))
                        counter += 1
                except IndexError:
                    continue

                try:
                    counter = 1
                    while re.search(r"\d", line[col + counter]):
                        num = num + line[col + counter]
                        nums.add((row, col + counter))
                        counter += 1
                except IndexError:
                    pass
                value += int(num)

    return value


def part02(lines):
    value = 0

    return value


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.read().splitlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")
