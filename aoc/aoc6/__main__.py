from aoc.common import benchmark
from aoc.aoc6.aoc6_part1 import aoc6_part1
from aoc.aoc6.aoc6_part2 import aoc6_part2

def main() -> None:
    benchmark(aoc6_part1, 1_000)
    benchmark(aoc6_part2, 1, result_only=True)

if __name__ == '__main__':
    main()
