import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(30000)

inp = 'target area: x=88..125, y=-157..-103'

x1, x2, y1, y2 = 88, 125, -157, -103

# x1, x2, y1, y2 = 20, 30, -10, -5

def simulate(px, py, vx, vy, apex, verbose=False):
    apex = max(apex, py)
    if verbose:
        print(f'{px=} {py=} {vx=} {vy=}')

    if x1 <= px <= x2 and y1 <= py <= y2:
        return True, apex

    if px < x2 and py > y1:
        next_vx = vx - 1 if vx > 0 else 0
        return simulate(px + vx, py + vy,
                next_vx, vy - 1, apex)
    else:
        return False, apex


limit = x2 * abs(y1)
limit = 5 * abs(y1)
valids = []
p1 = 0
for i in range(limit):
    for j in range(-limit, limit):
        is_good, apex = simulate(0, 0, i, j, 0)
        if is_good:
            valids.append((i, j))
            p1 = max(p1, apex)

print(p1)
print(len(valids))
