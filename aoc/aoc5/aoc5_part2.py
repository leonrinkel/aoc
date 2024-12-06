from aoc.aoc5.common import parse_input

def order(u, rls):
    while True:
        for a, b in rls:
            if (
                a in u and b in u and
                u.index(a) > u.index(b)
            ):
                x, y = u.index(a), u.index(b)
                u[x], u[y] = u[y], u[x]
                break
        else:
            break
    return u

def aoc5_part2():
    rls, ups = parse_input()
    return sum(
        order(u, rls)[len(u) // 2]
        for u in ups
        if any(
            u.index(a) > u.index(b)
            for a, b in rls
            if a in u and b in u
        )
    )
