from aoc_get import get_input


inp = get_input()
inp = inp.split()
grid = [list(map(int, row)) for row in inp]


def get_coords_around(grid, i, j):
    coords = []
    if i > 0:
        coords.append((i - 1, j))
        if j > 0:
            coords.append((i - 1, j - 1))
        if j < len(grid) - 1:
            coords.append((i - 1, j + 1))
    if i < len(grid[0]) - 1:
        coords.append((i + 1, j))
        if j > 0:
            coords.append((i + 1, j - 1))
        if j < len(grid) - 1:
            coords.append((i + 1, j + 1))
    if j < len(grid) - 1:
        coords.append((i, j + 1))
    if j > 0:
        coords.append((i, j - 1))
    return coords


def do_round(grid):
    flashers = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            increase(grid, i, j, flashers)
    for flasher in flashers:
        grid[flasher[0]][flasher[1]] = 0
    return grid, flashers


def increase(grid, i, j, flashers):
    grid[i][j] = (grid[i][j] + 1) % 10
    if grid[i][j] == 0:
        if (i, j) not in flashers:
            flashers.add((i, j))
            coords_around = get_coords_around(grid, i, j)
            for coords in coords_around:
                increase(grid, coords[0], coords[1], flashers)



p1 = delta = 0
p2 = 1

while delta < 100:
    grid, flashers = do_round(grid)
    delta = len(flashers)

    if p2 <= 100:
        p1 += delta
    p2 += 1

print(p1, p2)
