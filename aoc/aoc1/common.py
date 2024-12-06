import csv

from aoc.common import Input

def parse_input():
    with Input(__file__) as file:
        return map(list, zip(*[
            (int(a), int(b))
            for a, b in csv.reader(
                file,
                delimiter=' ',
                skipinitialspace=True,
            )
        ]))
