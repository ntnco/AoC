from aoc_get import get_input
from collections import deque

inp = get_input().splitlines()


def find_illegal(preamble, lines) -> int:
    q = []   
    for i in range(preamble):
        cur = int(lines[i])
        q.append(cur)
    i = preamble

    while i < len(lines):
        cur = int(lines[i])
        if check_illegal(cur, q):
            return cur
        else:
            q.pop(0)
            q.append(cur)
            i += 1

def check_illegal(n, pre) -> bool:
    if not pre:
        return True
    elif (n - int(pre[0])) in pre[1:]:
        return False
    else:
        return check_illegal(n, pre[1:])

print(find_illegal(25, inp))


def find_range(preamble, lines, stop, goal):
    t = 0
    for j in range(preamble):
        cur2 = int(lines[j])
        t += cur2
    j = preamble - 1
    i = 0
    while j < stop:
        if t == goal:
            return(range(i, j))
        else: 
            j += 1
            t += int(lines[j])
            t -= int(lines[i])
            i += 1
    return None

def sum_extremes(r, lines) -> int:
    mini = float('inf')
    maxi = float('-inf')
    for i in r:
        cur = int(lines[i])
        if cur > maxi:
            maxi = cur
        if cur < mini:
            mini = cur
    return mini + maxi


num = p1
rank = inp.index(str(num))

i = 2
while i < rank:
    fr = find_range(i, inp, rank, num)
    if fr:
        p2 = sum_extremes(fr, inp)
        print(p2)
        exit()
    else:
        i += 1
