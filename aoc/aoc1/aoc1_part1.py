from functools import reduce

from aoc.aoc1.common import parse_input

def aoc1_part1():
    a, b = parse_input()
    a.sort()
    b.sort()
    return reduce(
        lambda acc, pair: acc + abs(pair[0] - pair[1]),
        zip(a, b), 0
    )
