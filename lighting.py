import aoc
input = aoc.get_input(6)

grid = [[0] * 1000 for i in range(1000)]

instrs = input.split('\n')

def toggle(rg):
    start = [int(x) for x in rg[0].split(',')]
    end = [int(x) for x in rg[2].split(',')]
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            grid[i][j] += 2

def switch(rg, x):
    start = [int(x) for x in rg[0].split(',')]
    end = [int(x) for x in rg[2].split(',')]
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if x == 0 and grid[i][j] > 0:
                grid[i][j] -= 1
            elif x == 1:
                grid[i][j] += 1


for instr in instrs:
    words = instr.split(' ')
    if words[0] == "toggle":
        toggle(words[1:])
    elif words[1] == "on":
        switch(words[2:], 1)
    elif words[1] == "off":
        switch(words[2:], 0)

total = sum([sum(row) for row in grid])

print(total)
