import csv

with open('input', mode='r', encoding='utf-8') as file:
    a, b = map(list, zip(*[
        (int(a), int(b))
        for a, b in csv.reader(
            file,
            delimiter=' ',
            skipinitialspace=True,
        )
    ]))

cnts = {
    i: sum(map(lambda x: x == i, b))
    for i in set(a)
}

print(sum([j * cnts[j] for j in a]))
