
import requests

cookies = {}
cookies["ru"] = "53616c7465645f5f837f00adeab431b368b12616d94dbe86755b069056d88f92"
cookies["session"] = "53616c7465645f5f9b572c57927b8b26ad62ea78a4e61e5fa7ea3e0779ac9be8d057be7af50c5cc6eb9f249cbbaed487"
url = "https://adventofcode.com/2015/day/5/input"
raw_input = requests.get(url=url, cookies=cookies).content
input = raw_input.decode()

total = 0
words = input.split('\n')

def is_nice(s):
    return has_pair_twice(s) and has_sandwich(s)

def has_pair_twice(s):
    for i in range(1, len(s) - 1):
        pair = s[i - 1: i + 1]
        if pair in s[i + 1:]:
            return True
    return False

def has_sandwich(s):
    for i in range(2, len(s)):
        trio = s[i - 2: i + 1]
        if trio[0] == trio[2]:
            return True
    return False

for word in words:
    if len(word) > 0:
        total += is_nice(word)

print(total)
