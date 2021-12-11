from aoc_get import get_input


inp = get_input()
inp = inp.split()
grid = [list(map(int, row)) for row in inp]


def get_coords_around(grid, i, j):
    coords = []
    for m in range(i - 1, i + 2):
        for n in range(j - 1, j + 2):
            if 0 <= m < len(grid) and\
                    0 <= n < len(grid[0]) and\
                    not (i == m and j == n):
                coords.append((m, n))
    return coords


def do_round(grid):
    flashers = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            increase(grid, i, j, flashers)
    for i, j in flashers:
        grid[i][j] = 0
    return grid, flashers


def increase(grid, i, j, flashers):
    grid[i][j] = (grid[i][j] + 1) % 10
    if grid[i][j] == 0 and (i, j) not in flashers:
        flashers.add((i, j))
        for coords in get_coords_around(grid, i, j):
            increase(grid, coords[0], coords[1], flashers)



p1 = num_flashes = 0
p2 = 1

while num_flashes < 100:
    grid, flashers = do_round(grid)
    num_flashes = len(flashers)

    if p2 <= 100:
        p1 += num_flashes
    p2 += 1

p2 -= 1
print(p1, p2)
