from pathlib import Path
import regex as re


def part1(lines):
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


# Solution provided by https://aoc-puzzle-solver.streamlit.app
def part2(lines):
    segments = lines.split("\n\n")
    intervals = []

    for seed in re.findall(r"(\d+) (\d+)", segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float("inf")
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r"(\d+) (\d+) (\d+)", segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:  # no overlap
                continue
            if x1 < y1:  # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:  # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append(
                (x1 + diff, x2 + diff, level + 1)
            )  # perfect overlap -> make conversion and let pass to next nevel
            break

        else:
            intervals.append((x1, x2, level + 1))

    return min_location


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
