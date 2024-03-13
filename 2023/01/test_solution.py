import solution


def test_part01():
    example = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

    assert solution.part01(example) == 142


def test_part02():
    example = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    assert solution.part02(example) == 281
