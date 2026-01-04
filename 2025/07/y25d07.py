import operator
from functools import reduce
from pathlib import Path


def part1(puzzle: str) -> int:
    split_count = 0
    grid = [list(line) for line in puzzle.splitlines()]

    index = grid[0].index('S')
    grid[1][index] = '|'

    for g_row in range(2, len(grid)):
        for g_col in range(len(grid[g_row])):
            if grid[g_row - 1][g_col] == '|':
                if grid[g_row][g_col] == '^':
                    split_count += 1
                    grid[g_row][g_col - 1] = '|'
                    grid[g_row][g_col + 1] = '|'
                elif grid[g_row][g_col] == '.':
                    grid[g_row][g_col] = '|'

    return split_count

def part2(puzzle: str) -> int:
    grid = [list(line) for line in puzzle.splitlines()]

    index = grid[0].index('S')
    grid[1][index] = '1'

    for g_row in range(2, len(grid)):
        for g_col in range(len(grid[g_row])):
            g_above = grid[g_row - 1][g_col]

            if g_above.isdigit():
                if grid[g_row][g_col] == '^':
                    g_left = grid[g_row][g_col - 1]
                    g_right = grid[g_row][g_col + 1]

                    grid[g_row][g_col - 1] = str(int(g_above) + int(g_left)) if g_left.isdigit() else g_above
                    grid[g_row][g_col + 1] = str(int(g_above) + int(g_right)) if g_right.isdigit() else g_above
                elif grid[g_row][g_col] == '.':
                    grid[g_row][g_col] = g_above
                elif grid[g_row][g_col].isdigit():
                    grid[g_row][g_col] = str(int(g_above) + int(grid[g_row][g_col]))


    return sum(int(cell) for cell in grid[-1] if cell.isdigit())

if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input.txt").read_text()

    print(f"Part 1: {part1(puzzle)}")
    print(f"Part 2: {part2(puzzle)}")