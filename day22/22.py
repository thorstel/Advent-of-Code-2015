from collections import *
from math import *
import itertools
import re
import sys

def solve(data):
    boss_hp, boss_dmg = [int(l.split(': ')[1]) for l in data.splitlines()]
    costs = []
    SEEN = set()
    part2 = False

    def player_turn(hp, mp, t1, t2, t3, boss_hp, mana_spent):
        state = (hp, mp, t1, t2, t3, boss_hp, mana_spent)
        if state in SEEN: return
        SEEN.add(state)

        if part2:
            hp -= 1
            if hp <= 0: return

        if t1 > 0: t1 -= 1
        if t2 > 0:
            boss_hp -= 3
            t2 -= 1
        if t3 > 0:
            mp += 101
            t3 -= 1
        if boss_hp <= 0:
            costs.append(mana_spent)
            return

        if mp >= 53:
            boss_turn(hp, mp - 53, t1, t2, t3, boss_hp - 4, mana_spent + 53)
        if mp >= 73:
            boss_turn(hp + 2, mp - 73, t1, t2, t3, boss_hp - 2, mana_spent + 73)
        if mp >= 113 and t1 == 0:
            boss_turn(hp, mp - 113, 6, t2, t3, boss_hp , mana_spent + 113)
        if mp >= 173 and t2 == 0:
            boss_turn(hp, mp - 173, t1, 6, t3, boss_hp , mana_spent + 173)
        if mp >= 229 and t3 == 0:
            boss_turn(hp, mp - 229, t1, t2, 5, boss_hp, mana_spent + 229)

    def boss_turn(hp, mp, t1, t2, t3, boss_hp, mana_spent):
        ac = 0
        if t1 > 0:
            ac = 7
            t1 -= 1
        if t2 > 0:
            boss_hp -= 3
            t2 -= 1
        if t3 > 0:
            mp += 101
            t3 -= 1
        if boss_hp <= 0:
            costs.append(mana_spent)
            return
        hp -= max(1, boss_dmg - ac)
        if hp <= 0: return
        player_turn(hp, mp, t1, t2, t3, boss_hp, mana_spent)

    player_turn(50, 500, 0, 0, 0, boss_hp, 0) 
    print(min(costs))

    # reset for part 2
    costs = []
    SEEN = set()
    part2 = True
    player_turn(50, 500, 0, 0, 0, boss_hp, 0) 
    print(min(costs))

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
Hit Points: 58
Damage: 9
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
