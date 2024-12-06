from aoc.common import benchmark
from aoc.aoc1.aoc1_part1 import aoc1_part1
from aoc.aoc1.aoc1_part2 import aoc1_part2

def main() -> None:
    benchmark(aoc1_part1, 1_000)
    benchmark(aoc1_part2, 100)

if __name__ == '__main__':
    main()
