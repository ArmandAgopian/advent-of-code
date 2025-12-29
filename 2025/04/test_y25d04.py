from y25d04 import part1, part2

INPUT_PART1 = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

EXPECTED_PART1 = 13

INPUT_PART2= """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

EXPECTED_PART2 = 43

def test_part1():
    assert part1(INPUT_PART1) == EXPECTED_PART1

def test_part2():
    assert part2(INPUT_PART2) == EXPECTED_PART2