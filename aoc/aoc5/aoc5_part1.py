from aoc.aoc5.common import parse_input

def aoc5_part1():
    rls, ups = parse_input()
    return sum(
        u[len(u) // 2]
        for u in ups
        if all(
            u.index(a) < u.index(b)
            for a, b in rls
            if a in u and b in u
        )
    )
