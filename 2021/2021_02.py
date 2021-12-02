from aoc_get import get_input


lines = get_input().splitlines()


# part 1
f = 0
u = 0
for line in lines:
    instr, magn = line.split()
    if instr == 'forward':
        f += int(magn)
    elif instr == 'up':
        u += int(magn)
    elif instr == 'down':
        u -= int(magn)
print(f * -u)


# part 2
f = 0
aim = 0
depth = 0
for line in lines:
    instr, magn = line.split()
    if instr == 'forward':
        f += int(magn)
        depth += aim * int(magn)
    elif instr == 'up':
        aim += int(magn)
    elif instr == 'down':
        aim -= int(magn)
print(-depth * f)
