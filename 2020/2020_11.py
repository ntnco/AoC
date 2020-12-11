from aoc_get import get_input
from math import prod

inp = get_input().splitlines()

def surround(grid):
    h = len(grid)
    w = len(grid[0])
    res = ['.' * (w + 2)]
    for i in range(h):
        res.append('.' + grid[i] + '.')
    res.append('.' * (w + 2))
    return res

def count_around(ii, jj, g):
    #up left
    ul = '.'
    i = ii - 1
    j = jj - 1
    while i > 0 and j > 0 and ul == '.':
        if g[i][j] != '.':
            ul = g[i][j]
        i -= 1
        j -= 1

    #up center
    uc = '.'
    i = ii - 1
    j = jj
    while i > 0 and uc == '.':
        if g[i][j] != '.':
            uc = g[i][j]
        i -= 1

    #up right
    ur = '.'
    i = ii - 1
    j = jj + 1
    while i > 0 and j < len(g[0]) and ur == '.':
        if g[i][j] != '.':
            ur = g[i][j]
        i -= 1
        j += 1

    #center left
    cl = '.'
    i = ii
    j = jj - 1
    while j > 0 and cl == '.':
        if g[i][j] != '.':
            cl = g[i][j]
        j -= 1

    #center right
    cr = '.'
    i = ii
    j = jj + 1
    while j < len(g[0]) and cr == '.':
        if g[i][j] != '.':
            cr = g[i][j]
        j += 1

    #down left
    dl = '.'
    i = ii + 1
    j = jj - 1
    while j > 0 and i < len(g) and dl == '.':
        if g[i][j] != '.':
            dl = g[i][j]
        i += 1
        j -= 1

    #down center
    dc = '.'
    i = ii + 1
    j = jj
    while i < len(g) and dc == '.':
        if g[i][j] != '.':
            dc = g[i][j]
        i += 1

    #down right
    dr = '.'
    i = ii + 1
    j = jj + 1
    while j < len(g) and i < len(g[0]) and dr == '.':
        if g[i][j] != '.':
            dr = g[i][j]
        i += 1
        j += 1

    #p2
    around = ul + uc + ur + cl + cr + dl + dc + dr

    #p1
    #around = [g[i-1][j-1], g[i-1][j], g[i-1][j+1], g[i][j-1],
    #        g[i][j+1], g[i+1][j-1], g[i+1][j], g[i+1][j+1]]
    res = around.count('#')
    return res

def next_round(grid):
    width = len(grid[0])
    res = ['.' * width]
    for i in range(1, len(grid) - 1):
        w = '.'
        for j in range(1, len(grid) - 1):
            cur = grid[i][j]
            if cur == '.':
                w += '.'
            else:
                n = count_around(i, j, grid)
                if n == 0:
                    w += '#' 
                elif n >= 5:
                    w += 'L'
                else:
                    w += cur
        res.append(w + '.')
    res.append('.' * width)
    return res

def count_occ(grid) -> int:
    return str(grid).count('#')

def prints(seats):
    for s in seats:
        print(s)
    print('--------')

#inp = '''#.##.##.##
########.##
##.#.#..#..
#####.##.##
##.##.##.##
##.#####.##
#..#.#.....
###########
##.######.#
##.#####.##'''.splitlines()
seats = surround(inp)

inc = -1
num_occ = 0
#prints(seats)

while inc != 0:
    seats = next_round(seats)
    #prints(seats)
    new_num_occ = count_occ(seats)
    inc = new_num_occ - num_occ
    num_occ = new_num_occ
    #print(num_occ)
print(num_occ)
