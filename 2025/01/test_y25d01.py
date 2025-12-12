import pytest
from y25d01 import part1, part2

INPUT_PART1 = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

EXPECTED_PART1 = 3

INPUT_PART2="""\

"""

EXPECTED_PART2 = 281

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2