import itertools
import re
import sys

def solve(data):
    data = data.splitlines()
    assert len(data) == 4
    prop = []
    for line in data:
        _, p = line.split(': ')
        prop.append(list(map(lambda s: int(s.split()[1]), p.split(', '))))

    total_score1 = 0;
    total_score2 = 0;
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                h = 100 - i - j - k
                idx = [i, j, k, h]
                cap = max(0, sum(prop[p][0] * n for p, n in enumerate(idx)))
                dur = max(0, sum(prop[p][1] * n for p, n in enumerate(idx)))
                fla = max(0, sum(prop[p][2] * n for p, n in enumerate(idx)))
                tex = max(0, sum(prop[p][3] * n for p, n in enumerate(idx)))
                cal = max(0, sum(prop[p][4] * n for p, n in enumerate(idx)))
                score = cap * dur * fla * tex
                total_score1 = max(score, total_score1)
                if cal == 500:
                    total_score2 = max(score, total_score2)
    print(total_score1)
    print(total_score2)

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
