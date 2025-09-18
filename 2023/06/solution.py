import regex as re


def part1(lines):
    value = 1
    times = map(int, re.findall(r"\d+", lines[0]))
    distances = map(int, re.findall(r"\d+", lines[1]))

    for time, distance in zip(times, distances):
        runs = 0

        for millisecond in range(0, time + 1):
            actual = (time - millisecond) * millisecond
            if actual > distance:
                runs += 1

        value *= runs
    return value


def part2(lines):
    value = 0
    time = int("".join(re.findall(r"\d+", lines[0])))
    distance = int("".join(re.findall(r"\d+", lines[1])))

    for millisecond in range(0, time + 1):
        actual = (time - millisecond) * millisecond
        if actual > distance:
            value += 1

    return value


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
