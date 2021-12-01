from aoc_get import get_input

nums = [int(x) for x in get_input().split()]

# part 1
last = nums[0]
total = 0
for num in nums[1:]:
    total += num > last
    last = num
print(total)
    
# part 2
last = sum(nums[:3])
total = 0
for i in range(3, len(nums)):
    cur = last - nums[i - 3] + nums[i]
    total += cur > last
print(total)
