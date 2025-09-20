import pytest
from day07 import part1, part2

INPUT_PART1 = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

EXPECTED_PART1 = 6440

INPUT_PART2="""\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

EXPECTED_PART2 = 5905

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2