import re

with open('input', mode='r', encoding='utf-8') as file:
    print(sum(
        int(a) * int(b)
        for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', file.read())
    ))
