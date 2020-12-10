
from hashlib import md5
import requests
from aoc_0 import get_input

input = get_input(4)

res = 0
beg = ""

while(beg != "000000"):
    res += 1
    to_hash = input + str(res)
    m = md5(to_hash.encode()).hexdigest()
    beg = m[:6]

print(m)
print(to_hash)
print(res)
