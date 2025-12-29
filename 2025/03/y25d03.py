from pathlib import Path


def part1(puzzle: str) -> int:
    value = 0

    for line in puzzle.splitlines():
        bank = [int(i) for i in line]
        highest = max(bank[:-1])
        i = bank.index(highest)
        second_highest = max(bank[i+1:])
        value += (highest * 10) + second_highest

    return value

def part2(puzzle: str) -> int:
    # i is 0
    # list of values
    #for reverse range of 12->1?
    # find max, repeat, update i. subset of [i+1:range limit]
    value = 0

    for line in puzzle.splitlines():
        bank = [int(i) for i in line]
        digits = []
        i = -1

        for num in range(-11, 1):
            if num == 0:
                num = len(bank)

            highest = max(bank[i + 1:num])
            digits.append(highest)
            i = bank.index(highest, i + 1, num)
        value += int("".join(map(str, digits)))

    return value

if __name__ == "__main__":
    input = (Path(__file__).parent / "input.txt").read_text()

    print(f"Part 1: {part1(puzzle)}")
    print(f"Part 2: {part2(puzzle)}")