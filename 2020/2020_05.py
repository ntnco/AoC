from aoc_2020 import get_input

#inp = get_input(5).split('\n')

inp = """BFFFBBFRRR
BFBFFFBRLR""".splitlines()

def get_amp(ss, n, c):
    res = 0
    for s in ss:
        if s == c:
            res += n
        n /= 2
    return int(res)

m = 0

ids = []

for line in inp:
    amp_beg = get_amp(line[:7], 64, 'B')
    amp_end = get_amp(line[7:], 4, 'R')
    id = (amp_beg << 3) + amp_end
    m = max(m, id)
    ids.append(id)

print(m)

ids.sort()
for i in range(1, len(ids)):
    if ids[i - 1] == ids[i] - 2:
        print(int(ids[i]) - 1)
