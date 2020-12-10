from aoc_2020 import get_input
nums = [int(n) for n in get_input(1).split('\n')]

def find_n(n, nums):
    if nums:
        if nums[0] == n:
            return True
        else:
            return find_n(n, nums[1:])

def sum_2020(n, nums, total):
    if nums:
        goal = total - n
        if find_n(goal, nums[1:]):
            return n * goal
        else:
            return sum_2020(nums[1], nums[1:], total)

res1 = sum_2020(nums[0], nums, 2020)
print(res1)

def summable(n, nums, to_sum):
    if len(nums) > 1:
        goal = to_sum - n
        if find_n(goal, nums[1:]):
            return True
        else:
            return summable(nums[1], nums[1:], goal)

def triple_sum_2020(n, nums):
    if len(nums) > 2:
        goal = 2020 - n
        if summable(nums[1], nums[1:], goal):
            return n * sum_2020(nums[1], nums[1:], goal)
        else:
            return triple_sum_2020(nums[1], nums[1:])

res2 = triple_sum_2020(nums[0], nums)
print(res2)


lines = [str(n) for n in nums]
for i in range(len(lines) - 2):
    num_i = int(lines[i])
    for j in range(i + 1, len(lines) - 1):
        num_j = int(lines[j])
        for k in range(j + 1, len(lines)):
            num_k = int(lines[k])
            if num_i + num_j + num_k == 2020:
                print(num_i * num_j * num_k)
                exit() 
