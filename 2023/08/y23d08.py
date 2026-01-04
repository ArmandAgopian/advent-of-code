import itertools
from math import lcm
import regex as re
from pathlib import Path


def part1(lines):
    tree = {}
    for line in lines[2:]:
        key = line[:3]
        val1 = line[7:10]
        val2 = line[12:15]
        tree[key] = (val1, val2)

    curr = 'AAA'
    for i, n in zip(itertools.count(), itertools.cycle(lines[0])):
        if curr == 'ZZZ':
            return i
        curr = tree[curr][0 if n == 'L' else 1]


def part2(lines):
    tree = {}
    for line in lines[2:]:
        key = line[:3]
        val1 = line[7:10]
        val2 = line[12:15]
        tree[key] = (val1, val2)

    pattern = re.compile(r'..A')  # 3 chars, last must be A
    curr = [k for k in tree.keys() if pattern.match(k)]
    completed = []

    for node in curr:
        for i, n in zip(itertools.count(), itertools.cycle(lines[0])):
            if node[2] == 'Z':
                completed.append(i)
                break
            node = tree[node][0 if n == 'L' else 1]

    return lcm(*completed)


if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.read().splitlines()

    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
