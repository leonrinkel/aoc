from aoc.aoc7.common import parse_line, evl, add, mul
from aoc.aoc7.aoc7_part1 import aoc7_part1
from aoc.aoc7.aoc7_part2 import aoc7_part2

def test_parse_line():
    assert parse_line('123: 1 2 3\n') == (123, [1, 2, 3])
    assert parse_line('1234: 1 2 3 4\n') == (1234, [1, 2, 3, 4])

def test_evl():
    assert evl([4, 4], [mul]) == 16
    assert evl([1, 1, 2], [add, mul]) == 4

def test_aoc7_part1():
    assert aoc7_part1() == 14711933466277

def test_aoc7_part2():
    assert aoc7_part2() == 286580387663654
