import pytest
from y23d03 import part1, part2

INPUT_PART1 = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

EXPECTED_PART1 = 4361

INPUT_PART2="""\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

EXPECTED_PART2 = 467835

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2