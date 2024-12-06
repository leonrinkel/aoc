from aoc.common import benchmark
from aoc.aoc5.aoc5_part1 import aoc5_part1
from aoc.aoc5.aoc5_part2 import aoc5_part2

def main() -> None:
    benchmark(aoc5_part1, 200)
    benchmark(aoc5_part2, 50)

if __name__ == '__main__':
    main()
