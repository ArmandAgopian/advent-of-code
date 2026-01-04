from pathlib import Path
from collections import Counter

CARD_ORDER = {"2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "T": 10,
              "J": 11,
              "Q": 12,
              "K": 13,
              "A": 14}

CARD_ORDER2 = {"J": 1,
               "2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "T": 10,
               "Q": 12,
               "K": 13,
               "A": 14}


def part1(lines):
    hands = []

    for line in lines:
        hand = 0
        left, right = line.split()
        counts = dict(Counter(left))

        # 5 of a kind has 1 value
        # 4 of a kind has 2 values
        # full house has 2 values
        # 3 of a kind has 3 values
        # Two pair has 3 values
        # One pair has 4 values
        # High card has 5 values
        match len(counts):
            # 5 of a kind
            case 1:
                hand = 6
            case 2:
                # 4 of a kind
                if 4 in counts.values():
                    hand = 5
                # Full house
                else:
                    hand = 4
            case 3:
                # 3 of a kind
                if 3 in counts.values():
                    hand = 3
                # Two pair
                else:
                    hand = 2
            # One pair
            case 4:
                hand = 1
            # High card
            case 5:
                hand = 0

        hands.append((hand, left, right))

    sorted_hands = sorted(
        hands,
        key=lambda item: (item[0], [CARD_ORDER[c] for c in item[1]])
    )

    value = sum((i + 1) * int(hand[2]) for i, hand in enumerate(sorted_hands))
    return value


def part2(lines):
    hands = []

    for line in lines:
        hand = 0
        left, right = line.split()
        counts = dict(Counter(left))

        jokers = counts.get("J", 0)
        non_jokers = [v for k, v in counts.items() if k != "J"]

        if not non_jokers:
            non_jokers = [0]

        non_jokers.sort(reverse=True)
        top_count = non_jokers[0] + jokers

        match top_count:
            case 5:
                hand = 6  # five of a kind
            case 4:
                hand = 5  # four of a kind
            case 3:
                if non_jokers[1] == 2:
                    hand = 4  # full house
                else:
                    hand = 3  # three pair
            case 2:
                if non_jokers[1] == 2:
                    hand = 2 # two pair
                else:
                    hand = 1  # one pair
            case 1:
                hand = 0  # high card

        hands.append((hand, left, right))

    sorted_hands = sorted(
        hands,
        key=lambda item: (item[0], [CARD_ORDER2[c] for c in item[1]])
    )

    value = sum((i + 1) * int(hand[2]) for i, hand in enumerate(sorted_hands))
    return value


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
