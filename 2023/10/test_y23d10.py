from y23d10 import part1, part2

INPUT_PART1 = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

EXPECTED_PART1 = 8

INPUT_PART2="""\

"""

EXPECTED_PART2 = 2

def test_part1():
    lines = INPUT_PART1.splitlines()
    assert part1(lines) == EXPECTED_PART1

def test_part2():
    lines = INPUT_PART2.splitlines()
    assert part2(lines) == EXPECTED_PART2