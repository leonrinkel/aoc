import re

active = 1

def do():
    global active
    active = 1
    return 0

def dont():
    global active
    active = 0
    return 0

with open('input', mode='r', encoding='utf-8') as file:
    print(sum(
        do() if op == 'do()' else
        dont() if op == "don't()" else
        int(a) * int(b) * active
        for op, a, b in re.findall(
            r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))', file.read())
    ))
