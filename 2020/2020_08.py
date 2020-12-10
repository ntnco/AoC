from aoc_get import get_input
import re

inp = get_input().split('\n')

def runnit(code):
    acc = 0
    done = set()
    i = 0
    while i < len(code):
        if i < 0:
            return None
        if i not in done:
            done.add(i)
            ins, n = code[i].split()
            if ins == 'acc':
                i += 1
                acc += int(n)
            elif ins == 'jmp':
                i += int(n)
            elif ins == 'nop':
                i += 1
        else:
            return None
    return acc

changeables = []
for i in range(len(inp)):
    ins = inp[i].split()[0]
    if ins in ['nop', 'jmp']:
        changeables.append(i)

def change_inp(given, line_num):
    changed = given[:]
    ins, n = given[line_num].split()
    if ins == 'nop':
        new_ins = 'jmp'
    else:
        new_ins = 'nop'
    changed[line_num] = ' '.join([new_ins, n])
    return changed

res = None
i = 0
while res == None:
    changed = change_inp(inp, changeables[i])
    res = runnit(changed)
    i += 1

print(res)
