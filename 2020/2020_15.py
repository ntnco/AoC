from aoc_get import get_input

inp = [int(n) for n in get_input().split(',')]
turn = last = 1
nums = {}

for n in inp:
    nums[n] = [turn]
    turn += 1
    last = n

def add_num(rank, last):
    if len(nums[last]) > 1:
        new_num = rank - 1 - nums[last][-2]
    else:
        new_num = 0

    if new_num in nums:
        if len(nums[new_num]) == 1:
            nums[new_num].append(rank)
        else:
            a, b = new[new_num]
            nums[new_num] = b, rank
    else:
        nums[new_num] = [rank]

    return new_num
    

def get_num(n, last):
    for i in range(len(nums) + 1, n + 1):
        number = add_num(i, last)
        last = number
    return number

print(get_num(30000000, last))
# for p1, just change 30000000 to 2020
