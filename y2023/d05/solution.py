import regex as re


def part01(lines):
    value = float("inf")
    groups = lines.split("\n\n")
    for seed in groups[0].split(":")[1].split():
        val = int(seed)

        for group in map(lambda x: x.split(":")[1], groups[1:]):
            for line in map(lambda x: x.split(), group.strip().splitlines()):
                new, old, offset = map(lambda x: int(x), line)
                if old <= val < old + offset:
                    val = new + (val - old)
                    break

        value = min(val, value)
    return value


def part02(lines):
    value = 0

    return value


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.read()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")
