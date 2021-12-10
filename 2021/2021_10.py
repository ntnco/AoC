from aoc_get import get_input


points_p1 = {')':3, ']':57, '}':1197, '>':25137}
points_p2 = {'(':1, '[':2, '{':3, '<':4}
matches = {'(':')', '[':']', '{':'}', '<':'>'}


def reduce_line(line):
    acc = []
    for c in line:
        if c in '([{<':
            acc.append(c)
        elif c == matches[acc[-1]]:
            acc.pop()
        else:
            return c
    return acc


def score_completion(reduced_line):
    score = 0
    for c in reduced_line[::-1]:
        score *= 5
        score += points_p2[c]
    return score


inp = get_input()
inp = inp.split()

p1 = 0
scores = []
for line in inp:
    reduced_line = reduce_line(line)
    if len(reduced_line) == 1:
        p1 += points_p1[reduced_line]
    else:
        scores.append(score_completion(reduced_line))

p2 = sorted(scores)[len(scores) // 2]
print(p1, p2)
