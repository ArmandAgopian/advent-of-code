import pytest
from y25d05 import part1, part2

INPUT_PART1 = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

EXPECTED_PART1 = 3

INPUT_PART2= """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

EXPECTED_PART2 = 14

def test_part1():
    assert part1(INPUT_PART1) == EXPECTED_PART1

def test_part2():
    assert part2(INPUT_PART2) == EXPECTED_PART2