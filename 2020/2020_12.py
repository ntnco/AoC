from aoc_get import get_input
from math import prod

inp = get_input().splitlines()

def turn(d, n):
    n /= 90
    new_d = (d + n) % 4
    return new_d

def fwd(d, n, x, y):
    if d == 0:
        return x + n, y
    elif d == 1:
        return x, y + n
    elif d == 2:
        return x - n, y
    elif d == 3:
        return x, y - n
    else:
        print('error bro')
        print(d, n, x, y)

x = y = d = 0

for line in inp:
    ins, num = line[0], int(line[1:])
    if ins == 'R':
        d = turn(d, num)
    elif ins == 'L':
        d = turn(d, 360 - num)
    elif ins == 'F':
        x, y = fwd(d, num, x, y)
    elif ins == 'N':
        y -= num
    elif ins == 'S':
        y += num
    elif ins == 'E':
        x += num
    elif ins == 'W':
        x -= num
    else:
        print('we erring')
        print(x, y, d)

p1 = x + y
print(x, y, p1)


#p2
#IMPORTANT: The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

def rot(wx, wy, n):
    n /= 90
    if n == 0:
        return wx, wy
    elif n == 1:
        return wy, -wx
    elif n == 2:
        return -wx, -wy
    elif n == 3:
        return -wy, wx
    else:
        print('error bro')
        print(wx, wy, n)


x = y = d = 0
wpx, wpy = 10, 1

for line in inp:
    ins, num = line[0], int(line[1:])
    if ins == 'N':
        wpy += num
    elif ins == 'S':
        wpy -= num
    elif ins == 'E':
        wpx += num
    elif ins == 'W':
        wpx -= num
    elif ins == 'R':
        wpx, wpy = rot(wpx, wpy, num)
    elif ins == 'L':
        wpx, wpy = rot(wpx, wpy, 360 - num)
    elif ins == 'F':
        x += num * wpx
        y += num * wpy

p2 = abs(x) + abs(y)
print(x, y, p2)
