import csv

from aoc.common import Input

def parse_input():
    with Input(__file__) as file:
        return list(csv.reader(
            file,
            delimiter=' ',
            skipinitialspace=True,
        ))

def safe(row):
    ascending = row[0] < row[-1]
    return all(
        (
            (ascending and 1 <= b - a <= 3) or
            (not ascending and 1 <= a - b <= 3)
        )
        for a, b in zip(row, row[1:])
    )
