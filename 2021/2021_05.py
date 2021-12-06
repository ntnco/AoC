from aoc_get import get_input


inp = get_input().splitlines()


def get_inc(v1, v2):
    if v1 == v2:
        inc = 0
    elif v1 < v2:
        inc = 1
    else:
        inc = -1
    return inc


def run_commands(commands, no_diagonals=True):
    
    sky = [[0] * 1000 for i in range(1000)]

    for command in commands:
        beg, arrow, end = command.split()
        beg_x, beg_y = map(int, beg.split(','))
        end_x, end_y = map(int, end.split(','))
    
        i, j = beg_x, beg_y
        inc_x = get_inc(beg_x, end_x)
        inc_y = get_inc(beg_y, end_y)
        
        if no_diagonals and inc_x != 0 and inc_y != 0:
            continue

        last = False
        while True:
            sky[i][j] += 1
            i += inc_x
            j += inc_y
            if last:
                break
            last = i == end_x and j == end_y

    return count_overlaps(sky)


def count_overlaps(sky):
    total = 0
    for row in sky:
        for c in row:
            if c > 1:
                total += 1
    return total


p1 = run_commands(inp)
print(p1)

p2 = run_commands(inp, no_diagonals=False)
print(p2)
