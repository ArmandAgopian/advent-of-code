from pathlib import Path
import regex as re


def part1(input: str) -> int:
    value = 0

    ranges, foods = input.split('\n\n')
    ranges = [tuple(map(int, line.split('-'))) for line in ranges.splitlines()]
    foods = [int(line) for line in foods.splitlines()]

    for food in foods:
        for r in ranges:
            if food in range(r[0], r[1] + 1):
                value += 1
                break
    
    return value

def part2(input: str) -> int:
    
    ranges, _ = input.split('\n\n')
    ranges = [tuple(map(int, line.split('-'))) for line in ranges.splitlines()]
    ranges.sort()

    # https://www.youtube.com/watch?v=IKzTKqVIEig

    last = ranges[0]
    count = 0

    for lo, hi in ranges:
        if last[1] < lo:
            count += last[1] - last[0] + 1
            last = (lo, hi)
        else:
            last = (last[0], max(last[1], hi))

    count += last[1] - last[0] + 1

    return count

if __name__ == "__main__":
    input = (Path(__file__).parent / "input.txt").read_text()

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")