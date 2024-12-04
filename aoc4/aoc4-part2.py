with open('input', mode='r', encoding='utf-8') as file:
    data = [
        list(line.rstrip('\r\n'))
        for line in file.readlines()
    ]
w, h = len(data), len(data[0])

filters = [
    [
        ['M', ' ', 'S'],
        [' ', 'A', ' '],
        ['M', ' ', 'S'],
    ],
    [
        ['M', ' ', 'M'],
        [' ', 'A', ' '],
        ['S', ' ', 'S'],
    ],
    [
        ['S', ' ', 'S'],
        [' ', 'A', ' '],
        ['M', ' ', 'M'],
    ],
    [
        ['S', ' ', 'M'],
        [' ', 'A', ' '],
        ['S', ' ', 'M'],
    ],
]

def apply(fil, dx, dy):
    for x in range(0, len(fil)):
        for y in range(0, len(fil[0])):
            if (
                fil[x][y] != ' ' and
                data[dx + x][dy + y] != fil[x][y]
            ):
                return 0
    return 1

print(sum(
    apply(fil, dx, dy)
    for fil in filters
    for dx in range(0, w - len(fil) + 1)
    for dy in range(0, h - len(fil[0]) + 1)
))
