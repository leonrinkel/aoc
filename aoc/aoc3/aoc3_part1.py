import re

from aoc.common import Input

def aoc3_part1():
    with Input(__file__) as file:
        return sum(
            int(a) * int(b)
            for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', file.read())
        )
