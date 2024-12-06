from aoc.aoc2.common import parse_input, safe

def aoc2_part1():
    return sum(
        safe([int(num) for num in row])
        for row in parse_input()
    )
