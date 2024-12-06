from multiprocessing import Pool, cpu_count

from tqdm import tqdm

from aoc.common import parse_map

def cycle(stuff):
    data, w, h, x, y, ob = stuff
    lab = [
        [
            '#' if (x, y) == ob else data[x][y]
            for y in range(h)
        ]
        for x in range(w)
    ]
    visited = set()
    while True:
        if (x, y, lab[x][y]) in visited:
            return True
        visited.add((x, y, lab[x][y]))

        dx, dy = (
            (-1,  0) if lab[x][y] == '^' else
            ( 0, -1) if lab[x][y] == '<' else
            ( 0,  1) if lab[x][y] == '>' else
            ( 1,  0)
        )

        if not (
            0 <= x + dx < w and
            0 <= y + dy < h
        ):
            return False

        if lab[x + dx][y + dy] == '#':
            lab[x][y] = {
                '^': '>', '<': '^',
                '>': 'v', 'v': '<',
            }[lab[x][y]]
        else:
            lab[x + dx][y + dy] = lab[x][y]
            lab[x][y] = '.'
            x, y = dx + x, y + dy

def aoc6_part2():
    data, w, h = parse_map(__file__)
    sx, sy = next(
        (x, y)
        for x in range(w) for y in range(h)
        if data[x][y] in ('^', '<', '>', 'v')
    )

    obs = [
        (data, w, h, sx, sy, (x, y))
        for x in range(w) for y in range(h)
        if data[x][y] not in ('#', '^', '<', '>', 'v')
    ]

    with Pool(cpu_count()) as p:
        return sum(tqdm(p.imap(cycle, obs), total=len(obs)))
