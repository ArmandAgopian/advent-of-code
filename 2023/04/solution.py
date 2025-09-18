import regex as re


def part1(lines):
    value = 0

    for line in lines:
        winning_nums = set(line.split(":")[1].split("|")[0].split())
        nums = set(line.split(":")[1].split("|")[1].split())
        actual_wins = winning_nums & nums
        if actual_wins:
            value += 2 ** (len(actual_wins) - 1)

    return value


def part2(lines):
    cards = [1] * len(lines)

    for i, line in enumerate(lines):
        winning_nums = set(line.split(":")[1].split("|")[0].split())
        nums = set(line.split(":")[1].split("|")[1].split())
        actual_wins = winning_nums & nums

        for j in range(len(actual_wins)):
            cards[i + j + 1] += cards[i]

    return sum(cards)


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
