from hashlib import md5

puzzle_input = 'bgvyzdsv'
p1, p2 = False, False
N = 0

while not p1 or not p2:
    digest = md5((puzzle_input + str(N)).encode('ascii')).hexdigest()
    if not p1 and digest.startswith('00000'):
        print('Part 1:', N)
        p1 = True
    if not p2 and digest.startswith('000000'):
        print('Part 2:', N)
        p2 = True
    N += 1
