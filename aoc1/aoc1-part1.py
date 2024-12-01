import csv
from functools import reduce

with open('input', mode='r', encoding='utf-8') as file:
    a, b = map(list, zip(*[
        (int(a), int(b))
        for a, b in csv.reader(
            file,
            delimiter=' ',
            skipinitialspace=True,
        )
    ]))

a.sort()
b.sort()

print(reduce(
    lambda acc, pair: acc + abs(pair[0] - pair[1]),
    zip(a, b), 0
))
