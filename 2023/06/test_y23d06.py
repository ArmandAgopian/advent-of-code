import pytest
from y23d06 import part1, part2

INPUT_PART1 = """\
Time:      7  15   30
Distance:  9  40  200
"""

EXPECTED_PART1 = 288

INPUT_PART2="""\
Time:      71530
Distance:  940200
"""

EXPECTED_PART2 = 71503

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2