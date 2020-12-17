from aoc_get import get_input

inp = get_input()
#inp = '''.#.
#..#
####'''

inp = inp.splitlines()

def create_empty_layer(n):
    res = []
    for i in range(n):
        res.append('.' * n)
    return res

side = len(inp)
final_width = side * 6
def create_middle_layer(given):
    num_empty_sides = (final_width - side)// 2
    res = []
    empty_line = '.' * final_width
    for i in range(num_empty_sides):
        res.append(empty_line)
    empty_side1 = '.' * num_empty_sides
    num_end = final_width - num_empty_sides - side
    empty_side2 = '.' * num_end
    for line in given:
        res.append(empty_side1 + line + empty_side2)
    for i in range(num_end):
        res.append(empty_line)
    return res

def create_cube(final_width):
    empty_cube = []
    for i in range(final_width):
        empty_cube.append(create_empty_layer(final_width))
    return empty_cube

def create_hypercube(final_width):
    empty_hc = []
    for i in range(final_width):
        empty_hc.append(create_cube(final_width))
    return empty_hc

ml = create_middle_layer(inp)
hc = create_hypercube(final_width)
hc[final_width // 2][final_width // 2] = ml

def cycle(hypercube):
    new_hypercube = []
    for h in range(len(hypercube)):
        cube = hypercube[h]
        new_cube = []
        for i in range(len(cube)):
            square = cube[i]
            new_square = []
            for j in range(len(square)):
                line = square[j]
                new_line = ''
                for k in range(len(line)):
                    c = line[k]
                    new_c = get_new_c(h, i, j, k, c, hypercube)
                    new_line += new_c
                new_square.append(new_line)
            new_cube.append(new_square)
        new_hypercube.append(new_cube)
    return new_hypercube

def get_new_c(h, i, j, k, c, hypercube):
    fwm1 = final_width - 1
    if h < 1 or i < 1 or j < 1 or k < 1 or \
        h >= fwm1 or i >= fwm1 or j >= fwm1 or k >= fwm1:
        new_c = '.'
    else:
        around = count_around(h, i, j, k, hypercube)
        if c == '#':
            if 1 < around < 4:
                new_c = '#'
            else:
                new_c = '.'
        elif c == '.':
            if around == 3:
                new_c = '#'
            else:
                new_c = '.'
    return new_c

def get_offsets():
    off_h = [-1] * 27 + [0] * 27 + [1] * 27

    off_i = [-1] * 9 + [0] * 9 + [1] * 9
    off_i *= 3 # 4th dim

    off_j = [-1] * 3 + [0] * 3 + [1] * 3
    off_j *= 3
    off_j *= 3 # 4th dim

    off_k = [-1, 0, 1] * 9
    off_k *= 3 # 4th dim

    full_offsets = list(zip(off_h, off_i, off_j, off_k))
    full_offsets.remove((0,0,0,0))
    return full_offsets

offs = get_offsets()

def count_around(h, i, j, k, hc):
    count = 0
    for o in offs:
        oh, oi, oj, ok = o
        c = hc[h + oh][i + oi][j + oj][k + ok]
        if c == '#':
            count += 1
    return count


def relevant(hc):
    for cube in hc:
        if str(cube).count('#') > 0:
            for square in cube:
                if str(square).count('#') > 0:
                    for line in square:
                        print(line)
                    print('')

for i in range(7):
    print('count is now ' + str(str(hc).count('#')))
    #relevant(hc)
    hc = cycle(hc)

