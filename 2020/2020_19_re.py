from aoc_get import get_input
import re
import time

inp = get_input()

#inp = '''0: 4 1 5
#1: 2 3 | 3 2
#2: 4 4 | 5 5
#3: 4 5 | 5 4
#4: "a"
#5: "b"
#
#ababbb
#bababa
#abbbab
#aaabbb
#aaaabbb'''

#inp = '''0: 1 2
#1: "a"
#2: 1 1 | 1
#4: "c"
#5: "d"
#
#ab
#ba'''

rule_block, given_words = inp.split('\n\n')
rules = rule_block.splitlines()

rule_dict = {}
for rule in rules:
    n, rule_defs = rule.split(': ')

    if rule_defs.count(' ') == 0:
        if rule_defs.count('"') == 2:
            options = [rule_defs[1]]
        else:
            options = [rule_defs]
    else:
        options = rule_defs.split(' | ')

    rule_dict[n] = options


all_words = rule_dict['0']

def get_fst_val(keys):
    key = keys[0]
    return rule_dict[key][0]

def get_snd_val(keys):
    key = keys[0]
    return rule_dict[key][1]

at_least_one_digit = re.compile(r'.*\d+')
def has_num(word):
    return re.match(at_least_one_digit, word)

digit = re.compile(r'\d+')
i = 0
while(has_num(all_words[-1])):
    while has_num(all_words[i]):
        cur = all_words[i]
        fst = re.findall(digit, cur)[0]
    
        all_words[i] = re.sub(digit, get_fst_val, cur, count=1)
        if len(rule_dict[fst]) > 1:
            all_words.append(re.sub(digit, get_snd_val, cur, count=1))
        #time.sleep(0.5)
    all_words[i] = ''.join(all_words[i].split())
    i += 1

print(all_words[-1])

print(len(all_words))
aws = set(all_words)

print(len(aws))

words = given_words.splitlines()
res = 0
for w in words:
    if w in all_words:
        res += 1

print(res)
