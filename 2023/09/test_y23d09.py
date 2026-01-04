from y23d09 import part1, part2

INPUT_PART1 = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

EXPECTED_PART1 = 114

INPUT_PART2="""\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

EXPECTED_PART2 = 2

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2