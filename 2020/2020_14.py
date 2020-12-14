from aoc_get import get_input

inp = get_input().splitlines()

def pad_bin(n: int, num_digits) -> str:
    binum = "{0:b}".format(n)
    return binum.zfill(num_digits)


def apply_mask(mask: str, num: str) -> str:
    res = ''
    for i in range(len(mask)):
        if mask[i] != 'X':
            res += mask[i]
        else:
            res += num[i]
    return res


cur_mask = ''
mem = {}
for line in inp:
    beg, eq, end = line.split()
    if beg == 'mask':
        cur_mask = end
    else:
        mem_addr = int(beg[4:-1])
        fbn = pad_bin(int(end), 36)
        masked = apply_mask(cur_mask, fbn)
        mem[mem_addr] = int(masked, 2)
    
p1 = 0
for val in mem.values():
    p1 += val

print(p1)

#p2
def apply_mem_mask(mask: str, mem_num: str) -> str:
    res_list = []
    x_indices = []
    res = ''
    for i in range(len(mask)): 
        if mask[i] == 'X':
            res += 'X'
            x_indices.append(i)
        elif mask[i] == '1':
            res += mask[i]
        else:
            res += mem_num[i]

    # we have our res with Xs, now we should get all possibilities
    # the idea here is to map all binary numbers in [0..2**num_of_Xs] onto the Xs
    lbin = len(x_indices)

    for i in range(2 ** lbin):
        b36 = pad_bin(i, lbin)
        bin_index = 0
        cur_res = ''
        for j in range(len(res)):
            if res[j] == 'X':
                cur_res += b36[bin_index]
                bin_index += 1
            else:
                cur_res += res[j]
        res_list.append(int(cur_res, 2))

    return res_list

mem2 = {}
for line in inp:
    beg, eq, end = line.split()
    if beg == 'mask':
        cur_mask = end
    else:
        mem_addr = int(beg[4:-1])
        num = int(end)
        fba = pad_bin(num, 36)
        addrs = apply_mem_mask(cur_mask, fba)

        for addr in addrs:
            mem2[addr] = num

p2 = sum(mem2.values())
print(p2)
