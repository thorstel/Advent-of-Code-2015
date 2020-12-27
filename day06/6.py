import fileinput
import re

grid1 = [[False for _ in range(1000)] for _ in range(1000)]
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]

for line in fileinput.input():
    m = re.match(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line.strip())
    assert m
    cmd = m.group(1)
    r1, c1 = int(m.group(2)), int(m.group(3))
    r2, c2 = int(m.group(4)), int(m.group(5))
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if cmd == 'turn on':
                grid1[r][c] = True
                grid2[r][c] += 1
            elif cmd == 'toggle':
                grid1[r][c] = not grid1[r][c]
                grid2[r][c] += 2
            elif cmd == 'turn off':
                grid1[r][c] = False
                grid2[r][c] = max(grid2[r][c] - 1, 0)
            else:
                assert False

print(sum(sum(1 for on in row if on) for row in grid1))
print(sum(sum(row) for row in grid2))
