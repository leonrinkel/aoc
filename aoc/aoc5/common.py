from aoc.common import Input

def parse_input():
    rls, ups = [], []
    with Input(__file__) as file:
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
    return rls, ups
