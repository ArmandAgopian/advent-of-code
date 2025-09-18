import os

from aocd import get_data
from dotenv import load_dotenv
import sys
from pathlib import Path

def load_input(year: int, day: int):
    data = get_data(year=year, day=day)

    day_str = f"{day:02d}"  # zero-padded
    outdir = Path(str(year)) / day_str
    outdir.mkdir(parents=True, exist_ok=True)

    outfile = outdir / "input.txt"
    outfile.write_text(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python input_loader.py <YYYY> <DD>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    load_dotenv()
    load_input(year, day)