from itertools import product
from multiprocessing import Pool, cpu_count

from tqdm import tqdm

from aoc.common import Input

def parse_line(l):
    r, os = l.split(': ')
    return (int(r), [int(o) for o in os.split(' ')])

def parse_input():
    with Input(__file__) as file:
        return [
            parse_line(l)
            for l in file.readlines()
        ]

def add(a, b):
    return a + b
def mul(a, b):
    return a * b
def cat(a, b):
    return int(str(a)+str(b))

def evl(vals, ops):
    for i, (a, b) in enumerate(zip(vals, vals[1:])):
        vals[i+1] = ops[i](a, b)
    return vals[-1]

def solve(stuff):
    ops, (r, vals) = stuff
    return r if any(
        evl(vals[:], perm) == r
        for perm in product(ops, repeat=len(vals)-1)
    ) else 0

def aoc7(ops):
    eqs = parse_input()
    with Pool(cpu_count()) as p:
        return sum(tqdm(
            p.imap(solve, [(ops, eq) for eq in eqs]),
            total=len(eqs),
        ))
