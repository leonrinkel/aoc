from aoc.aoc4.common import aoc4

def aoc4_part1():
    return aoc4([
        # horizontal
        [['X', 'M', 'A', 'S']],
        [['S', 'A', 'M', 'X']],
        # vertical
        [['X'], ['M'], ['A'], ['S']],
        [['S'], ['A'], ['M'], ['X']],
        # diagonal
        [
            ['X', ' ', ' ', ' '],
            [' ', 'M', ' ', ' '],
            [' ', ' ', 'A', ' '],
            [' ', ' ', ' ', 'S'],
        ],
        [
            ['S', ' ', ' ', ' '],
            [' ', 'A', ' ', ' '],
            [' ', ' ', 'M', ' '],
            [' ', ' ', ' ', 'X'],
        ],
        [
            [' ', ' ', ' ', 'X'],
            [' ', ' ', 'M', ' '],
            [' ', 'A', ' ', ' '],
            ['S', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', ' ', 'S'],
            [' ', ' ', 'A', ' '],
            [' ', 'M', ' ', ' '],
            ['X', ' ', ' ', ' '],
        ],
    ])
