from aoc.common import parse_map

def aoc6_part1():
    data, w, h = parse_map(__file__)
    x, y = next(
        (x, y)
        for x in range(w)
        for y in range(h)
        if data[x][y] in ('^', '<', '>', 'v')
    )

    visited = set()
    while True:
        visited.add((x, y))
        dx, dy = (
            (-1,  0) if data[x][y] == '^' else
            ( 0, -1) if data[x][y] == '<' else
            ( 0,  1) if data[x][y] == '>' else
            ( 1,  0)
        )
        if not (
            0 <= x + dx < w and
            0 <= y + dy < h
        ):
            break
        if data[x + dx][y + dy] == '#':
            data[x][y] = {
                '^': '>',
                '<': '^',
                '>': 'v',
                'v': '<',
            }[data[x][y]]
        else:
            data[x + dx][y + dy] = data[x][y]
            data[x][y] = '.'
            x, y = dx + x, y + dy

    return len(visited)
