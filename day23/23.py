from collections import *
from math import *
import itertools
import re
import sys

def solve(data):
    prog = data.splitlines()

    def run(start):
        reg = defaultdict(int)
        reg['a'] = start
        pc = 0
        while pc < len(prog):
            instr = prog[pc]
            op = instr[:3]
            args = instr[4:].split(', ')
            if op == 'hlf':
                reg[args[0]] //= 2
                pc += 1
            elif op == 'tpl':
                reg[args[0]] *= 3
                pc += 1
            elif op == 'inc':
                reg[args[0]] += 1
                pc += 1
            elif op == 'jmp':
                pc += int(args[0])
            elif op == 'jie':
                if reg[args[0]] % 2 == 0:
                    pc += int(args[1])
                else:
                    pc += 1
            elif op == 'jio':
                if reg[args[0]] == 1:
                    pc += int(args[1])
                else:
                    pc += 1
            else:
                assert False
        return reg['b']

    print(run(0))
    print(run(1))

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
