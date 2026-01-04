from pathlib import Path


def part1(puzzle):
    value = 50
    zero_counter = 0

    for line in puzzle.splitlines():
        distance = int(line[1:])

        if line[0] == "L":
            value = (value - distance) % 100
        elif line[0] == "R":
            value = (value + distance) % 100

        if value == 0:
            zero_counter += 1

    return zero_counter


def part2(puzzle):
    value = 50
    zero_counter = 0

    # 0 when:
    # - number larger than 100
    # - ending number is 0
    # - number crosses positive to negative
    # - number crosses negative to positive

    for line in puzzle.splitlines():
        distance = int(line[1:])

        for _ in range(distance):
            if line[0] == "L":
                value = (value - 1) % 100
            elif line[0] == "R":
                value = (value + 1) % 100

            if value == 0:
                zero_counter += 1

    return zero_counter


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        puzzle = f.read()

    print(f"Part 1: {part1(puzzle)}")
    print(f"Part 2: {part2(puzzle)}")
