from aoc_get import get_input


inp = get_input()
num_list = inp.split()[0].split(',')
nums = [int(n) for n in num_list]


def solve(days):
    counters = [0] * 9
    for num in nums:
        counters[num] += 1
    
    for _ in range(days):
        sixes = counters[0]
        for i in range(8):
            counters[i] = counters[i + 1]
        counters[8] = sixes
        counters[6] += sixes

    return sum(counters)


p1 = solve(80)
p2 = solve(256)
print(p1, p2)
