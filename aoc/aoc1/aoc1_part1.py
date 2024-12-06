from aoc.aoc1.common import parse_input

def aoc1_part1():
    a, b = map(sorted, parse_input())
    return sum(abs(x - y) for x, y in zip(a, b))
