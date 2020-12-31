from collections import *
from math import *
import itertools
import re
import sys

def solve(data):
    boss_hp, boss_dmg, boss_ac = [int(l.split(': ')[1]) for l in data.splitlines()]
    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    armors = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
    rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
    victories, defeats = [], []
    for weapon in weapons:
        for armor in armors:
            for i in range(3):
                for comb in itertools.combinations(rings, i):
                    hp = 100
                    cost = weapon[0] + armor[0] + sum(r[0] for r in comb)
                    dmg = weapon[1] + sum(r[1] for r in comb)
                    ac = armor[2] + sum(r[2] for r in comb)
                    turns_to_kill = boss_hp // max(dmg - boss_ac, 1)
                    turns_to_die = hp // max(boss_dmg - ac, 1)
                    if turns_to_kill <= turns_to_die:
                        victories.append(cost)
                    else:
                        defeats.append(cost)
    print(min(victories))
    print(max(defeats))

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
Hit Points: 100
Damage: 8
Armor: 2
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
