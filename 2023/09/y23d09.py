from pathlib import Path

def find_history_1(line):
    if len(set(line)) == 1:
        return line[-1]
    
    diffs = [line[i+1] - line[i] for i in range(len(line)-1)]
    next_diff = find_history_1(diffs)

    return line[-1] + next_diff

def find_history_2(line):
    if len(set(line)) == 1:
        return line[0]
    
    diffs = [line[i] - line[i-1] for i in range(1, len(line))]
    next_diff = find_history_2(diffs)

    return line[0] - next_diff

def part1(lines):
    histories = []
    for line in lines:
        histories.append(find_history_1(list(map(int,line.split()))))
    return sum(histories)

def part2(lines):
    histories = []
    for line in lines:
        histories.append(find_history_2(list(map(int,line.split()))))
    return sum(histories)

if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
