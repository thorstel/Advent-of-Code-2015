import fileinput

wires = {}
for line in fileinput.input():
    ins, w = line.strip().split(' -> ')
    wires[w] = ins

memory = {}
def eval_wire(w):
    if w in memory:
        return memory[w]
    if w not in wires:
        return int(w)
    ins = wires[w].split(' ')
    if len(ins) == 1:
        res = eval_wire(ins[0])
    elif ins[0] == 'NOT':
        res = (~eval_wire(ins[1])) % 0x10000
    else:
        a, op, b = ins
        if op == 'AND':
            res = eval_wire(a) & eval_wire(b)
        elif op == 'OR':
            res = eval_wire(a) | eval_wire(b)
        elif op == 'LSHIFT':
            res = (eval_wire(a) << eval_wire(b)) % 0x10000
        elif op == 'RSHIFT':
            res = (eval_wire(a) >> eval_wire(b)) % 0x10000
        else:
            assert False
    memory[w] = res
    return res

# Part 1
signal = eval_wire('a')
print(signal)

# Part 2
wires['b'] = str(signal)
memory = {}
print(eval_wire('a'))
