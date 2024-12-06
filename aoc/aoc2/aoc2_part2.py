from aoc.aoc2.common import parse_input, safe

def dampened(row):
    return any(
        safe(row[:i] + row[i+1:])
        for i in range(len(row))
    )

def aoc2_part2():
    return sum(map(dampened, parse_input()))
