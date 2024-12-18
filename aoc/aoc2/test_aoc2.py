from aoc.aoc2.common import parse_input
from aoc.aoc2.aoc2_part1 import aoc2_part1
from aoc.aoc2.aoc2_part2 import aoc2_part2

def test_parse_input():
    x = parse_input()
    assert x[0] == [74, 76, 78, 79, 76]
    assert x[1] == [38, 40, 43, 44, 44]

def test_aoc2_part1():
    assert aoc2_part1() == 257

def test_aoc2_part2():
    assert aoc2_part2() == 328
