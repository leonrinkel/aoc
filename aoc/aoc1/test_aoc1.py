from aoc.aoc1.common import parse_input
from aoc.aoc1.aoc1_part1 import aoc1_part1
from aoc.aoc1.aoc1_part2 import aoc1_part2

def test_parse_input():
    a, b = parse_input()
    assert a[:3] == (14764, 59598, 63147)
    assert b[:3] == (28773, 86587, 83451)

def test_aoc1_part1():
    assert aoc1_part1() == 2815556

def test_aoc1_part2():
    assert aoc1_part2() == 23927637
