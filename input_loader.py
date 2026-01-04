import argparse

from aocd import get_data
from dotenv import load_dotenv
from pathlib import Path

def load_input(year: int, day: int):
    data = get_data(year=year, day=day)

    day_str = f"{day:02d}"  # zero-padded
    outdir = Path(str(year)) / day_str
    outdir.mkdir(parents=True, exist_ok=True)

    outfile = outdir / "input.txt"
    outfile.write_text(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load input for Advent of Code by year and day."
    )
    parser.add_argument("YYYY", type=int, help="Year of the challenge (YYYY)")
    parser.add_argument("DD", type=int, help="Day of the challenge (DD)")

    args = parser.parse_args()

    year = args.year
    day = args.day

    load_dotenv()
    load_input(year, day)