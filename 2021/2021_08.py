from aoc_get import get_input


# find easy digits and put them in an array
# in their positions. For unknown digits, leave
# an empty string
def find_1478(nums):
    digits = [''] * 10
    for num in nums:
        ln = len(num)
        if ln == 2:
            digits[1] = num
        elif ln == 4:
            digits[4] = num
        elif ln == 3:
            digits[7] = num
        elif ln == 7:
            digits[8] = num
    return digits


# get the characters 2 strings have in common
def common_chars(str_list):
    common = set()
    for s in str_list:
        common &= set(s)
    return ''.join(common)


# output the character for 2 lines: left-top and left-bottom
def find_left_top_bottom_lines(nums):
    for c in 'abcdefg':
        cnt = init_nums.count(c)
        if cnt == 6:
            LT = c # left-top
        elif cnt == 4:
            LB = c # left-bottom
    return LT, LB


inp = get_input()
p1 = p2 = 0

for line in inp.splitlines():
    init_nums, output = line.split(' | ')
    LT, LB = find_left_top_bottom_lines(init_nums)
    nums = set(init_nums.split())
    digits = find_1478(nums) # we now have 1, 4, 7, 8

    five_liners = [n for n in nums if len(n) == 5]
    for num in five_liners:
        if LB in num:
            digits[2] = num
        elif LT in num:
            digits[5] = num
        else:
            digits[3] = num

    six_liners = [n for n in nums if len(n) == 6]
    for num in six_liners:
        if len(set(num) & set(digits[5])) == len(digits[5]) \
                and LB in num:
            digits[6] = num
        elif len(set(num) & set(digits[4])) == len(digits[4]):
            digits[9] = num
        else:
            digits[0] = num

    ans = ''
    for num in output.split():
        for i in range(len(digits)):
            if set(num) == set(digits[i]):
                ans += str(i)
                if i in (1,4,7,8):
                    p1 += 1
    p2 += int(ans)

print(p1, p2)
