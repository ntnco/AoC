from aoc_get import get_input
import re

inp = get_input()

# fill the dictionary
bags = {}
for line in inp.split('\n'):
    line = re.sub('bags?', 'bag', line)
    words = line.split()
    container = ' '.join(words[:3])
    contained = []
    to_contain = words[4:]
    for i in range(0, len(to_contain), 4):
        contained.append(' '.join(to_contain[i: i + 4])[:-1])
    bags[container] = contained

colors = set()

def container_inc(col, cols):
    if col not in cols:
        colors.add(col)
        return 1
    else:
        return 0

def remove_num(s):
    color = s.split()[-3:]
    return ' '.join(color)

def fill(target, d) -> int:
    res = 0
    for key in d.keys():
        if target in [remove_num(dk) for dk in d[key]]:
            res += container_inc(key, colors) + fill(key, d)
    return res

p1 = fill('shiny gold bag', bags)
print(p1)


def wrap(bag, mul, d, p2):
    if d[bag][0].startswith('no'):
        p2 += mul
    else:
        for b in d[bag]:
            to_mul = mul * int(b[0])
            p2 = wrap(remove_num(b), to_mul, bags, p2)
        p2 += mul
    return p2

res = wrap('shiny gold bag', 1, bags, 0) - 1
print(res)
