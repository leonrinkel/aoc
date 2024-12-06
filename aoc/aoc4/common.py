from aoc.common import parse_map

def apply(data, fil, dx, dy):
    for x, m in enumerate(fil):
        for y, n in enumerate(m):
            if n not in (' ', data[dx + x][dy + y]):
                return 0
    return 1

def aoc4(filters):
    data, w, h = parse_map(__file__)
    return sum(
        apply(data, fil, dx, dy)
        for fil in filters
        for dx in range(0, w - len(fil) + 1)
        for dy in range(0, h - len(fil[0]) + 1)
    )
