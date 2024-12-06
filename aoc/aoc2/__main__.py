from aoc.common import benchmark
from aoc.aoc2.aoc2_part1 import aoc2_part1
from aoc.aoc2.aoc2_part2 import aoc2_part2

def main() -> None:
    benchmark(aoc2_part1, 1_000)
    benchmark(aoc2_part2, 1_000)

if __name__ == '__main__':
    main()
