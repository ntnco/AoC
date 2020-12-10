
import requests

cookies = {}
cookies["ru"] = "53616c7465645f5f837f00adeab431b368b12616d94dbe86755b069056d88f92"
cookies["session"] = "53616c7465645f5f9b572c57927b8b26ad62ea78a4e61e5fa7ea3e0779ac9be8d057be7af50c5cc6eb9f249cbbaed487"
url = "https://adventofcode.com/2015/day/3/input"
raw_input = requests.get(url=url, cookies=cookies).content
input = raw_input.decode()

grid = []
for i in range(4000):
    grid.append([0] * 4000)

print(len(grid))
print(len(grid[0]))
print("chat")

x = x0 = x1 = 2000
y = y0 = y1 = 2000

total = 1
grid[x][y] += 1

for i in range(len(input)):
    car = input[i]
    if i % 2 == 0:
        x = x0
        y = y0
    else: 
        x = x1
        y = y1
    
    if car == '>':
        x += 1
    elif car == '<':
        x -= 1
    elif car == '^':
        y += 1
    elif car == 'v':
        y -= 1
    if grid[x][y] == 0:
        total += 1

    grid[x][y] += 1
    if i % 2 == 0:
        x0 = x
        y0 = y
    else:
        x1 = x
        y1 = y

print(str(total) + " ")

# a = b = c = d = 0
# for car in input:
#     if car == ">":
#         a += 1
#     elif car == "<":
#         b += 1
#     elif car == "^":
#         c += 1
#     elif car == "v":
#         d += 1
# 
# print(a)
# print(b)
# print(c)
# print(d)
