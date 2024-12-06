from aoc.aoc1.common import parse_input

def aoc1_part2():
    a, b = parse_input()
    cnts = {
        i: sum(map(lambda x, j=i: x == j, b))
        for i in set(a)
    }
    return sum(j * cnts[j] for j in a)
