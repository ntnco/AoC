from aoc_get import get_input
import re

inp = get_input()

inp = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

inp = '''0: 1 2
1: "a"
2: 1 1 | 3 3
3: "b"

ab
ba'''

rule_block, example_block = inp.split('\n\n')
rules = rule_block.splitlines()

rule_dict = {}
for rule in rules:
    n, rule_defs = rule.split(': ')

    if rule_defs.count(' ') == 0:
        options = [[rule_defs[1]]]
    else:
        options = [rule.split() for rule in rule_defs.split(' | ')]
        options = [[int(n) for n in gr] for gr in options]

    rule_dict[int(n)] = options

#def check(w, n):
#    r = rule_dict[n]
#    fst = r[0][0]
#    if isinstance(fst, str) and fst == w[0]:
#        return ''
#    elif len(r) == 1:
#        return check_list(w, n, r[0])
#    else:
#        for li in r:
#            if check_list(w, n, li):
#                return ''
#            else:
#                return None
#
#def check_list(w, n, li):
#    i = 0
#    cur = li[i]


class Node:
    def __init__(self, k):
        self.k = k
        self.rules = rule_dict[k]

        if len(self.rules) == 1 and len(self.rules[0]) == 1 and \
                re.match(r'^[ab]$', self.rules[0][0]):
            self.lists = None
            self.val = self.rules[0][0]
        else:
            self.lists = [[Node(n) for gr in self.rules for n in gr]]
            self.val = None

    def get_concats(self):
        if self.val:
            return [self.val]
        res = []
        for li in self.lists:
            res.extend(cross_concat(li))
        return res

def cross_concat(nodeList) -> [str]:
    ncs = [node.get_concats() for node in nodeList]
    print('node_concats -> ' + str(ncs))

    ws = []
    ws_prev = ['']
    for nc in ncs:
        for w in nc:
            for wp in ws_prev:
                cur_w = wp + w
                ws.append(cur_w)
        ws_prev = ws
        ws = []
    print(ws_prev)
        
    return ws_prev

root = Node(0) # builds the entire tree

n1 = Node(1)
c1 = n1.get_concats()
print(c1)

#print('---\n')
#
#all_w = root.get_concats()
#print(all_w)
