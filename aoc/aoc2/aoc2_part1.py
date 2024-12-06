from aoc.aoc2.common import parse_input, safe

def aoc2_part1():
    return sum(map(safe, parse_input()))
