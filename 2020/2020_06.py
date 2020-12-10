from aoc_get import get_input

inp = get_input()
groups = inp.split('\n\n')

res_union = 0
res_inter = 0
for group in groups:
    forms = group.splitlines()
    union = set(forms[0])
    inter = set(forms[0])
    for form in forms:
        union |= set(form)
        inter &= set(form)
    res_union += len(union)
    res_inter += len(inter)

print(res_union) # part 1
print(res_inter) # part 2

