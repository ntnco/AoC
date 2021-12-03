from aoc_get import get_input


lines = get_input().splitlines()



# part 1
sums = [0] * len(lines[0])
for line in lines:
    for i in range(len(sums)):
        sums[i] += int(line[i])

binarized = [str(x // (len(lines)//2)) for x in sums]
gamma = int(''.join(binarized), 2)
epsilon = gamma ^ 2 ** (len(lines[0])) - 1

print(gamma * epsilon)

#part 2
def keep_common_at(bins, i: int = 0, oxy=True):
    num_bins = len(bins)
    if num_bins == 1:
        return bins[0]

    total = 0
    for b in bins:
        total += b[i] == '1' 
    if total >= num_bins / 2:
        keep_only = '1'
    else:
        keep_only = '0'
    
    if oxy:
        res = [b for b in bins if b[i] == keep_only]
    else:
        res = [b for b in bins if b[i] != keep_only]

    return keep_common_at(res, i + 1, oxy=oxy)


oxygen = int(keep_common_at(lines), 2)
co2 = int(keep_common_at(lines, oxy=False), 2)

print(oxygen * co2)
