import regex as re

CARD_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def part01(lines):
    value = 0
    ranks = {}
    for line in lines:
        card = (line.split()[0], line.split()[1])
        count = {x: card[0].count(x) for x in set(card[0])}
        rank = int("".join([str(CARD_ORDER.index(x)) for x in card[0]]))
        print(card[0], rank)
        match len(count):
            case 1:
                ranks[card] = 50000000000 + rank
            case 2:
                ranks[card] = 40000000000 + rank
            case 3:
                ranks[card] = 30000000000 + rank
            case 4:
                ranks[card] = 20000000000 + rank
            case 5:
                ranks[card] = 10000000000 + rank

    print(ranks)
    return value


def part02(lines):
    value = 0

    return value


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.readlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")
