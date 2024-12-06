from aoc.common import benchmark
from aoc.aoc3.aoc3_part1 import aoc3_part1
from aoc.aoc3.aoc3_part2 import aoc3_part2

def main() -> None:
    benchmark(aoc3_part1, 5_000)
    benchmark(aoc3_part2, 5_000)

if __name__ == '__main__':
    main()
