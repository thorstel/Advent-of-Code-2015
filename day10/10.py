import itertools

def gen(s):
    res = ''
    for x, xs in itertools.groupby(s):
        res += str(len(list(xs))) + x
    return res

data = '1113222113'
for n in range(50):
    if n == 40: print(len(data))
    data = gen(data)
print(len(data))
