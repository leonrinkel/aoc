from aoc.common import Input

def parse_input():
    with Input(__file__) as file:
        return zip(*(
            (int(i) for i in line.split('   '))
            for line in file.readlines()
        ))
