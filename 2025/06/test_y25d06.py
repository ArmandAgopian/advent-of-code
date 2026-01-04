from y25d06 import part1, part2

INPUT_PART1 = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

EXPECTED_PART1 = 4277556

INPUT_PART2= """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

EXPECTED_PART2 = 3263827

def test_part1():
    assert part1(INPUT_PART1) == EXPECTED_PART1

def test_part2():
    assert part2(INPUT_PART2) == EXPECTED_PART2