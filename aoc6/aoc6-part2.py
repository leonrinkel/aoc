from multiprocessing import Pool, cpu_count
from tqdm import tqdm

with open('input', mode='r', encoding='utf-8') as file:
    data = [
        list(line.rstrip('\r\n'))
        for line in file.readlines()
    ]
w, h = len(data), len(data[0])
sx, sy = next(
    (x, y)
    for x in range(w) for y in range(h)
    if data[x][y] in ('^', '<', '>', 'v')
)

def cycle(ob):
    lab = [
        [
            '#' if (x, y) == ob else data[x][y]
            for y in range(h)
        ]
        for x in range(w)
    ]

    visited = set()
    x, y = sx, sy
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

def main():
    obs = [
        (x, y)
        for x in range(w) for y in range(h)
        if data[x][y] not in ('#', '^', '<', '>', 'v')
    ]

    with Pool(cpu_count()) as p:
        assert sum(tqdm(p.imap(cycle, obs), total=len(obs))) == 2262

if __name__ == '__main__':
    main()
