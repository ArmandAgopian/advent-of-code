import pytest
from y23d08 import part1, part2

INPUT_PART1 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

EXPECTED_PART1 = 6

INPUT_PART2="""\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

EXPECTED_PART2 = 6

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2