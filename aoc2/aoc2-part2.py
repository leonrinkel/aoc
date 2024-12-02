import csv

def safe(row):
    ascending = row[0] < row[-1]
    return all(
        (
            (ascending and 1 <= b - a <= 3) or
            (not ascending and 1 <= a - b <= 3)
        )
        for a, b in zip(row, row[1:])
    )

def dampened(row):
    return any(
        safe(row[:i] + row[i+1:])
        for i in range(len(row))
    )

with open('input', mode='r', encoding='utf-8') as file:
    print(sum([
        dampened([int(num) for num in row])
        for row in csv.reader(
            file,
            delimiter=' ',
            skipinitialspace=True,
        )
    ]))
