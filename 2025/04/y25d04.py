from pathlib import Path


def part1(puzzle: str) -> int:
    grid = [list(line) for line in puzzle.splitlines()]
    value = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                neighbors = 0

                for drow, dcol in directions:
                    row_new = row + drow
                    col_new = col + dcol
                    if (
                        (0 <= row_new < len(grid))
                        and (0 <= col_new < len(grid[0]))
                        and (grid[row_new][col_new] == '@')
                    ):
                        neighbors += 1

                if neighbors < 4:
                    value += 1
    return value


def part2(puzzle: str) -> int:
    grid = [list(line) for line in puzzle.splitlines()]
    value = 0
    iteration = 1

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while iteration > 0:
        iteration = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '@':
                    neighbors = 0

                    for drow, dcol in directions:
                        row_new = row + drow
                        col_new = col + dcol
                        if (
                            (0 <= row_new < len(grid))
                            and (0 <= col_new < len(grid[0]))
                            and (
                                grid[row_new][col_new] == '@'
                                or grid[row_new][col_new] == 'x'
                            )
                        ):
                            neighbors += 1

                    if neighbors < 4:
                        value += 1
                        grid[row][col] = 'x'
                        iteration += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'x':
                    grid[row][col] = '.'
    return value


if __name__ == '__main__':
    puzzle = (Path(__file__).parent / 'input.txt').read_text()

    print(f'Part 1: {part1(puzzle)}')
    print(f'Part 2: {part2(puzzle)}')
