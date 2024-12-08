import os
import typing
import timeit

from pathlib import Path

class Input:

    file: typing.TextIO | None

    def __init__(self, path: str):
        self.path = Path(
            os.path.dirname(os.path.realpath(path)),
            'input'
        )

    def __enter__(self):
        self.file = open(self.path, mode='r', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

def parse_map(path: str):
    with Input(path) as file:
        data = [
            list(line.rstrip('\r\n'))
            for line in file.readlines()
        ]
    return data, len(data), len(data[0])

def benchmark(fn, iters):
    print(fn.__name__)
    print(f' result = {fn()}')

    if iters > 0:
        time = timeit.timeit(
            'fn()', globals={'fn': fn}, number=iters)
        print(f' speed = {iters/time:g} it/s')

    print()

def print_map(data):
    print('\n'.join([''.join(l) for l in data]))
