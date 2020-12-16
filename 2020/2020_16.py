from aoc_get import get_input

inp = get_input()

rules, mine, nearby = inp.split('\n\n')

all_rules = {}

# populate all_rules dictionary
for rule in rules.splitlines():
    title, checks = rule.split(': ')
    r1, r2 = checks.split(' or ')
    r1 = [int(n) for n in r1.split('-')]
    r2 = [int(n) for n in r2.split('-')]

    all_rules[title] = [r1, r2]

def check_rule(n: int, rule: [[int]]) -> bool:
    for r in rule:
        if r[0] <= n <= r[1]:
            return True 
    return False

def check_all_rules(n: int) -> bool:
    for rule in all_rules.values():
        if check_rule(n, rule):
            return True
    return False

def is_valid(ticket: str) -> bool:
    invalid_sum = 0
    fields = ticket.split(',')
    for field in fields:
        f = int(field)
        if not check_all_rules(f):
            invalid_sum += f
    return invalid_sum

def sum_ticket(ticket: str) -> int:
    res = 0
    for n in ticket.split(','):
        res += int(n)
    return res

valid_tickets = []
nearby_tickets = nearby.splitlines()[1:]
p1 = 0
for ticket in nearby_tickets:
    error_rate = is_valid(ticket)
    p1 += error_rate
    if error_rate == 0 and '0' not in ticket.split(','):
        valid_tickets.append(ticket)

print(p1)

def remove_except(i):
    to_remove = list(rule_order[i])[0]
    for j in range(len(rule_order)):
        if j != i:
            if to_remove in rule_order[j]:
                rule_order[j].remove(to_remove)
                if len(rule_order[j]) == 1:
                    remove_except(j)

rule_order = []
for i in range(len(all_rules)):
    rule_order.append(set(all_rules.keys()))

# surprisingly, 1 interation of this was enough.
# I expected taking recursive guesses to be necessary here, they were not.
for vt in valid_tickets:
    vt = vt.split(',')
    for i in range(len(vt)):
        field = int(vt[i])
        for key in list(rule_order[i]):
            rule = all_rules[key]
            if not check_rule(field, rule):
                rule_order[i].remove(key)
                if len(rule_order[i])== 1:
                    remove_except(i)

print([list(rules)[0] for rules in rule_order])

indices = []
for i in range(len(rule_order)):
    key = list(rule_order[i])[0]
    if key.startswith('departure'):
        indices.append(i)

mine = mine.split(',')

p2 = 1
for i in indices:
    p2 *= int(mine[i])

print(p2)
