from aoc_get import get_input
from time import sleep

inp = get_input(22)
#inp = '''Player 1:
#43
#19
#
#Player 2:
#2
#29
#14'''

#inp = '''Player 1:
#9
#2
#6
#3
#1
#
#Player 2:
#5
#8
#4
#7
#10'''

s1, s2 = inp.split('\n\n')

s1 = [int(n) for n in s1.splitlines()[1:]]
s2 = [int(n) for n in s2.splitlines()[1:]]

def combat(s1, s2):
    while s1 and s2:
        p1 = s1.pop(0)
        p2 = s2.pop(0)
        if p1 > p2:
            s1.extend([p1, p2])
        else:
            s2.extend([p2, p1])
    
    if s1:
        winner = s1
    else:
        winner = s2
    return winner

def score_hand(hand_s):
    res = 0
    for i in range(len(hand_s)):
        cur = hand_s[len(hand_s) - 1 - i]
        res += (i + 1) * cur
    return res

#p1 = score_hand(combat(s1, s2))

#print(p1)


##########################################################
##########################################################

calculated = {}
def rec_combat(s1, s2):
    decks = str(s1) + str(s2)
    if decks in calculated:
        return calculated[decks]

    played1 = set()
    played2 = set()

    while s1 and s2:
        c1, c2 = str(s1), str(s2)
        if c1 in played1 or c2 in played2:
            played1.add(c1)
            played2.add(c2)
            return 0, s1
        played1.add(c1)
        played2.add(c2)

        p1 = s1.pop(0)
        p2 = s2.pop(0)
        if len(s1) >= p1 and len(s2) >= p2:
            res, w = rec_combat(s1[:p1], s2[:p2])
            #played1 |= prevs1
            #played2 |= prevs2

            if res == 0:
                #print('hey')
                s1.extend([p1, p2])
            else:
                #print('ho')
                #print(w)
                #print(s1)
                #print(s2)
                s2.extend([p2, p1])
        elif p1 > p2:
            s1.extend([p1, p2])
        else:
            s2.extend([p2, p1])
    
    if s1:
        calculated[decks] = 0, s1
        return 0, s1
    else:
        calculated[decks] = 1, s2
        return 1, s2

s1, s2 = inp.split('\n\n')

s1 = [int(n) for n in s1.splitlines()[1:]]
s2 = [int(n) for n in s2.splitlines()[1:]]

res, ex2 = rec_combat(s1, s2)

p2 = score_hand(ex2)
print(p2)
print(ex2)
