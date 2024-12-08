from itertools import product

def aoc8(data, w, h):
    return {
        ((x1, y1), (x1 - x2, y1 - y2))
        for (x1, y1) in product(range(w), range(h))
        if data[x1][y1] != '.'
        for (x2, y2) in product(range(w), range(h))
        if (
            data[x1][y1] == data[x2][y2] and
            (x1, y1) != (x2, y2)
        )
    }
