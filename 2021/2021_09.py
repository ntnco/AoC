from aoc_get import get_input

inp = get_input()
inp = inp.split()


def get_coords_around(grid, point):
    i, j = point
    coords = []
    if i > 0:
        coords.append((i - 1, j))
    if j > 0:
        coords.append((i, j - 1))
    if i < len(grid) - 1:
        coords.append((i + 1, j))
    if j < len(grid[0]) - 1:
        coords.append((i, j + 1))
    return coords


def val_at(grid, point):
    s = grid[point[0]][point[1]]
    return int(s)


def get_basin(grid, point, the_basin):
    around = get_coords_around(grid, point)
    cur = val_at(grid, point)
    the_basin.add((i, j))

    for point in around:
        if point not in the_basin:
            v = val_at(grid, point)
            if 9 > v > cur:
                the_basin.add(point)
                get_basin(grid, point, the_basin)
    return the_basin


def mul_max_3(li):
    ans = 1
    for x in sorted(li)[-3:]:
        ans *= x
    return ans


basin_sizes = []
p1 = p2 = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        coords_around = get_coords_around(inp, (i, j))
        center = int(inp[i][j])
        is_low = True

        for point in coords_around:
            is_low &= val_at(inp, point) > center
        if is_low:
            p1 += center + 1
            basin = get_basin(inp, (i, j), set())
            basin_sizes.append(len(basin))

p2 = mul_max_3(basin_sizes)

print(p1, p2)
