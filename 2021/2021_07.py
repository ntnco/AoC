from aoc_get import get_input

inp = get_input()
nums = [int(s) for s in inp.split(',')]
nums.sort()

# p1
med = nums[len(nums) // 2]
p1 = sum(abs(num - med) for num in nums)
print(p1)


# p2
def cost(x1, x2):
    diff = abs(x1 - x2)
    return diff * (diff + 1) // 2

avg = sum(nums) // len(nums)
p2 = sum(cost(num, avg) for num in nums)
print(p2)
