from aoc_2020 import get_input

inp = get_input(2).split('\n')

valid_count = 0
for line in inp:
    cs, car, pw = line.split()
    c_min, c_max = [int(c) for c in cs.split('-')]
    valid_count += c_min <= int(pw.count(car[0])) <= c_max
print(valid_count)

valid_count = 0
for line in inp:
    cs, car, pw = line.split()
    i_1, i_2 = [int(c) - 1 for c in cs.split('-')]
    valid_count += (pw[i_1] == car[0]) != (pw[i_2] == car[0])
print(valid_count)

