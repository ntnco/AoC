from aoc_get import get_input
from math import prod

inp = get_input().splitlines()
jolts = [0]
inp = [int(n) for n in inp]
inp.sort()
jolts.extend(inp)
jolts.append(int(jolts[-1]) + 3)

d1 = 0
d3 = 1
groups = []
cur_gr = [0]

for i in range(1, len(jolts)):
    cur = int(jolts[i])
    cur_gr.append(cur)
    diff = cur - int(jolts[i - 1])
    if diff == 1:
        d1 += 1
    elif diff == 3:
        groups.append(cur_gr)
        cur_gr = [cur]
        d3 += 1

p1 = d1 * d3
print(p1)

def powerset(r):
    res = []
    poss = 2 ** len(r)
    for n in range(poss):
        cur_group = []
        for i in range(len(r)):
            if n & 1:
                cur_group.append(r[i])
            n >>= 1
        res.append(cur_group)
    return res

def is_valid_chain(chain):
    ch = sorted(chain)
    for i in range(1, len(ch)):
        if ch[i] - ch[i - 1] > 3:
            return False
    return True


clean_groups = []
num_valids = []

for group in groups:
    if len(group) > 2:
        clean_groups.append(group)

for cg in clean_groups:
    c = cg[1:-1]
    cur_valid = 0
    centers = powerset(c)
    for center in centers:
        ch = [cg[0]] + center + [cg[-1]]
        if is_valid_chain(ch):
            cur_valid += 1
    num_valids.append(cur_valid)

p2 = prod(num_valids)
print(p2)
