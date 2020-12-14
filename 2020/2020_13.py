from aoc_get import get_input

inp = get_input().splitlines()

timestamp, buses = inp
timestamp = int(timestamp)

b = []
b2 = []
buses = buses.split(',')
for i in range(len(buses)):
    bus = buses[i]
    if bus.isnumeric():
        b.append(int(bus))
        b2.append((int(bus) - i, (int(bus))))

bests = []
for bus in b:
    bests.append(bus - timestamp % bus)

mini = min(bests)

for i in range(len(bests)):
    is_found = False
    if bests[i] == mini and not is_found:
        p1 = bests[i] * b[i]
        print(p1)
        is_found = True


# p2
# it was high time for me to learn the Chinese Remainder Theorem.

def find_facts(x, y):
    a = x
    b = y
    while abs(a - b) != 1:
        if a < b:
            a = x * (b // x) + x
        else:
            b = y * (a // y) + y
    fact_x = a // x
    fact_y = b // y
    if a < b:
        fact_x *= -1
    else:
        fact_y *= -1
    return fact_x, fact_y


# here as everywhere, a pair is (r, m), with r being the
# remainder and m the modulo - or , in other words,
# r is the timestamp and m the bus number.
def congruence(pair1, pair2):
    (r1, m1), (r2, m2) = pair1, pair2
    f1, f2 = find_facts(m1, m2)
    c = f1 * m1 * r2 + f2 * m2 * r1
    prod = m1 * m2
    c %= prod
    return c, prod

def congru_rec(pairs):
    if len(pairs) == 1:
        return pairs[0][0]
    else: 
        new_last = congruence(pairs[-2], pairs[-1])
        return congru_rec(pairs[:-2] + [new_last])

print(congru_rec(b2))
