from aoc.aoc1.common import parse_input

def aoc1_part2():
    a, b = parse_input()
    return sum(j * b.count(j) for j in a)
