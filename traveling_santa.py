from aoc_0 import get_input

lines = get_input(9).split('\n')
places = {}

for line in lines:
    words = line.split()
    beg, end, dist = words[0], words[2], words[4]
    
    if beg not in places:
        places[beg] = {end: dist}
    else:
        places[beg][end] = dist
    if end not in places:
        places[end] = {beg: dist}
    else:
        places[end][beg] = dist

print(places)
