from collections import *
from functools import *
import itertools
import operator
import re
import sys

def solve(data):
    xs = [int(x) for x in data.splitlines()]
    assert sum(xs) % 3 == 0 and sum(xs) % 4 == 0

    def minimum_entanglement(ngroups):
        weight = sum(xs) // ngroups
        ans = []
        for i in range(len(xs)):
            for c in itertools.combinations(xs, i):
                if sum(c) == weight:
                    ans.append(reduce(operator.mul, c, 1))
        return min(ans)

    print(minimum_entanglement(3))
    print(minimum_entanglement(4))

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
1
3
5
11
13
17
19
23
29
31
37
41
43
47
53
59
67
71
73
79
83
89
97
101
103
107
109
113
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
