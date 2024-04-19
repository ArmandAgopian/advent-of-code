import regex as re

MAX_VAL = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main():
    with open("./input.txt") as f:
        lines = f.read().splitlines()

    print(f"Part 01: {part01(lines)}")
    print(f"Part 02: {part02(lines)}")


def part01(lines):
    value = 0
    for count, line in enumerate(lines, start=1):
        limit = False

        # Each game set
        for set in line.split(':')[1].split(';'):

            # Each color number pair
            for pair in set.split(','):
                number, color = pair.split()
                if int(number) > MAX_VAL.get(color):
                    limit = True

        if not limit:
            value += count

    return value


def part02(lines):
    value = 0
    for count, line in enumerate(lines, start=1):
        maxes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        # Each game set
        for set in line.split(':')[1].split(';'):

            # Each color number pair
            for pair in set.split(','):
                number, color = pair.split()
                maxes.update({color: max(maxes.get(color), int(number))})

        value += (maxes.get('red') * maxes.get('blue') * maxes.get('green'))

    return value


if __name__ == '__main__':
    main()
