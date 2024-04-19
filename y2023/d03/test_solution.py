from .solution import *


def test_part01():
    example = ["467..114..",
               "...*......",
               "..35..633.",
               "......#...",
               "617*......",
               ".....+.58.",
               "..592.....",
               "......755.",
               "...$.*....",
               ".664.598.."]

    assert part01(example) == 4361


def test_part02():
    example = []

    assert part02(example) == 2286
