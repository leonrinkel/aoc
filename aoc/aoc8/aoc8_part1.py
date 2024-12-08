from aoc.common import parse_map
from aoc.aoc8.common import aoc8

def aoc8_part1():
    data, w, h = parse_map(__file__)
    return len({
        (x1 + dx, y1 + dy)
        for (x1, y1), (dx, dy) in aoc8(data, w, h)
        if 0 <= x1 + dx < w and 0 <= y1 + dy < h
    })
