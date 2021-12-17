import sys
sys.setrecursionlimit(2000)

inp = 'target area: x=88..125, y=-157..-103'
x1, x2, y1, y2 = 88, 125, -157, -103


def simulate(px, py, vx, vy, apex):
    apex = max(apex, py)

    if x1 <= px <= x2 and y1 <= py <= y2:
        return True, apex

    elif px < x2 and py > y1:
        next_vx = vx - 1 if vx > 0 else 0
        return simulate(px + vx, py + vy,
                next_vx, vy - 1, apex)
    else:
        return False, apex


limit = 2 * abs(y1)
p1 = p2 = 0
for i in range(limit):
    for j in range(-limit, limit):
        is_good, apex = simulate(0, 0, i, j, 0)
        if is_good:
            p2 += 1
            p1 = max(p1, apex)

print(p1, p2)
