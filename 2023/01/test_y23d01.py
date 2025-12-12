import pytest
from y23d01 import part1, part2

INPUT_PART1 = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXPECTED_PART1 = 142

INPUT_PART2="""\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

EXPECTED_PART2 = 281

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2