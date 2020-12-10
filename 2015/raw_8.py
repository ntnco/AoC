from aoc_0 import get_input, get_raw_input

inp = get_raw_input(8)
total_chars = 0
count = 0

for line in inp.split('\n'):
    to_add = 0
    for c in line:
        if c in "\\\"":
            to_add += 1
    to_add += 2
    total_chars += to_add
    print(line + " -> " + str(to_add))
    count += 1
    # if count > 10:
    #     break

print(total_chars)
    








### solution for part A 
# input_clean = get_input(8).split('\n')
# input_raw = get_raw_input(8).split('\n')
# total_chars = 0
# count = 0
# for i in range(len(input_clean)):
#     line = input_clean[i]
#     line_raw = input_raw[i]
#     
#     num_chars = len(line) 
#     print(line + " -> " + str(num_chars))
# 
#     num_chars_raw = len(line_raw)
#     print(line_raw + " -> " + str(num_chars_raw))
# 
#     increase = num_chars_raw - num_chars + 2
#     print(increase)
# 
#     total_chars += increase
#     count += 1
# 
# print(total_chars)
