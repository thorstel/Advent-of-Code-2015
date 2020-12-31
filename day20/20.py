from collections import *
from math import *
import itertools
import re
import sys

def solve(data):
    target = int(data)

    # Part 1
    presents = [0 for _ in range(target // 10)]
    for house in range(1, target // 10):
        for h in range(house, target // 10, house):
            presents[h] += house * 10
    print(next(h for h, p in enumerate(presents) if p > target))

    # Part 2
    presents = [0 for _ in range(target // 10)]
    for house in range(1, target // 10):
        cnt = 0
        for h in range(house, target // 10, house):
            if cnt >= 50: break
            presents[h] += house * 11
            cnt += 1
    print(next(h for h, p in enumerate(presents) if p > target))

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
34000000
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
