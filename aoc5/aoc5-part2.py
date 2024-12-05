rls, ups = [], []
with open('input', mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        if '|' in line:
            rls.append(tuple(
                int(x) for x in line \
                    .rstrip('\r\n').split('|')
            ))
        elif ',' in line:
            ups.append([
                int(x) for x in line \
                    .rstrip('\r\n').split(',')
            ])

def order(u):
    while True:
        for a, b in rls:
            if (
                a in u and b in u and
                u.index(a) > u.index(b)
            ):
                x, y = u.index(a), u.index(b)
                u[x], u[y] = u[y], u[x]
                break
        else:
            break
    return u

print(sum(
    order(u)[len(u) // 2]
    for u in ups
    if any(
        u.index(a) > u.index(b)
        for a, b in rls
        if a in u and b in u
    )
))
