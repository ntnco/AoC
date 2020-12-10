import requests

cookies = {}
cookies["ru"] = "53616c7465645f5f837f00adeab431b368b12616d94dbe86755b069056d88f92"
cookies["session"] = "53616c7465645f5f9b572c57927b8b26ad62ea78a4e61e5fa7ea3e0779ac9be8d057be7af50c5cc6eb9f249cbbaed487"
url = "https://adventofcode.com/2015/day/2/input"
raw_input = requests.get(url=url, cookies=cookies).content
input = raw_input.decode()

trios = input.split("\n")

total = 0

def wrap(s):
    nums = [int(num) for num in s.split('x')]
    p1 = nums[0] * nums[1]
    p2 = nums[0] * nums[2]
    p3 = nums[1] * nums[2]
    return 2 * (p1 + p2 + p3) + min(p1, p2, p3)

def attach(s):
    nums = [int(num) for num in s.split('x')]
    nums.sort()
    return 2 * (nums[0] + nums[1]) + nums[0] * nums[1] * nums[2]

for trio in trios:
    if len(trio) > 0:
        total += attach(trio)

print(total)

print("1x1x10 gives: ", end="")
print(attach("1x1x10"))

print("2x3x4 gives: ", end="")
print(attach("2x3x4"))
