from aoc_get import get_input

inp = get_input()

# inp = '''[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]'''


openers = '([{<'

points = dict()
points[')'] = 3
points[']'] = 57
points['}'] = 1197
points['>'] = 25137
points['OK'] = 0

complete = dict()
complete[')'] = 1
complete['('] = 1
complete[']'] = 2
complete['['] = 2
complete['}'] = 3
complete['{'] = 3
complete['>'] = 4
complete['<'] = 4

def matches(c1, c2):
    if c1 == ')':
        return c2 == '('
    elif c1 == ']':
        return c2 == '['
    elif c1 == '}':
        return c2 == '{'
    elif c1 == '>':
        return c2 == '<'
    else:
        print('error:', c1)



def check_line(line):
    acc = []
    for c in line:
        if c in openers:
            acc.append(c)
        elif matches(c, acc[-1]):
            acc.pop()
        else:
            return c
    return 'OK'


def reduce_line(line):
    acc = []
    for c in line:
        if c in openers:
            acc.append(c)
        elif matches(c, acc[-1]):
            acc.pop()
    return acc


def score_completion(line):
    line = line[::-1]
    score = 0
    for c in line:
        score *= 5
        score += complete[c]
    return score


inp = inp.split()
pairs = ['()', '[]', '{}', '<>']
p1 = 0
scores = []
for line in inp:
    check = check_line(line)
    p1 += points[check]

    if check == 'OK':
        reduced_line = reduce_line(line)
        scores.append(score_completion(reduced_line))

print(scores)

p2 = sorted(scores)[len(scores) // 2]
print(p1, p2)
