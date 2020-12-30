from collections import *
from math import *
import itertools
import re
import sys

def solve(data, target = 150):
    data = [int(x) for x in data.splitlines()]
    ways = Counter()
    for i in range(len(data) + 1):
        for c in itertools.combinations(data, i):
            if sum(c) == target:
                ways[i] += 1
    print(sum(ways.values()))
    print(ways[min(ways)])

########################################################################
#                             SETUP STUFF                              #
########################################################################

sample_input = r"""
20
15
10
5
5
""".strip()

actual_input = r"""
11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    print('=== SAMPLE ===')
    solve(sample_input, 25)
    print('=== ACTUAL ===')
    solve(actual_input)
