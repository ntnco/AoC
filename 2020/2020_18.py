from aoc_get import get_input
import re

single_num = re.compile(r'^\d+$')

inp = get_input().splitlines()

def eval_beg(match):
    return '(' + str(eval(match.group()[1:]))

def eval_op(match):
    return str(eval(match.group()))

def remove_paren(match):
    return match.group()[1:-1]

def simplify1(s):
    s = '(' + s + ')'
    while not re.match(single_num, s):
        s = re.sub(r'(\(\d+ [*\+] \d+)', eval_beg, s)
        s = re.sub(r'(\(\d+\))', remove_paren, s)
    return int(s)


def eval_top_level(s):
    while s.count('+') > 0:
        s = re.sub(r'(\d+ \+ \d+)', eval_op, s)
    while s.count('*') > 0:
        s = re.sub(r'(\d+ \* \d+)', eval_op, s)
    return s

def top_split(s):
    beg_top = s.rindex('(')
    before = s[:beg_top]
    end_top = s.find(')', beg_top)
    after = s[end_top + 1:]
    top_s = s[beg_top + 1:end_top]
    return before, top_s, after 

def simplify2(s):
    if s.count('(') == 0:
        return eval_top_level(s)
    else:
        beg, top, end = top_split(s)
        s = simplify2(beg + simplify2(top) + end)
        return s

p1 = 0
p2 = 0

for line in inp:
    num1 = simplify1(line)
    p1 += num1

    num2 = simplify2(line)
    p2 += int(num2)

print(p1)
print(p2)
