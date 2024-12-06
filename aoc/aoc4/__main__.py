from aoc.common import benchmark
from aoc.aoc4.aoc4_part1 import aoc4_part1
from aoc.aoc4.aoc4_part2 import aoc4_part2

def main() -> None:
    benchmark(aoc4_part1, 100)
    benchmark(aoc4_part2, 100)

if __name__ == '__main__':
    main()
