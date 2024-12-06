import re

from aoc.common import Input

def aoc3_part2():
    active, summ = 1, 0
    with Input(__file__) as file:
        for op, a, b in re.findall(
            r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))',
            file.read()
        ):
            if a and b:
                summ += int(a) * int(b) * active
            else:
                active = op == 'do()'
    return summ
