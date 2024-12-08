from aoc.common import benchmark
from aoc.aoc8.aoc8_part1 import aoc8_part1
from aoc.aoc8.aoc8_part2 import aoc8_part2

def main() -> None:
    benchmark(aoc8_part1, 200)
    benchmark(aoc8_part2, 200)

if __name__ == '__main__':
    main()
