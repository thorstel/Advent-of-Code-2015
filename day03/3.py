with open('input.txt', 'r') as file:
    data = file.read()

offsets = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

x = 0
y = 0
p1_visited = set()
p1_visited.add((0, 0))

xsanta = 0
ysanta = 0
xrobo = 0
yrobo = 0
p2_visited = set()
p2_visited.add((0, 0))
toggle = True

for d in data:
    x += offsets[d][0]
    y += offsets[d][1]
    p1_visited.add((x, y))
    if toggle:
        xsanta += offsets[d][0]
        ysanta += offsets[d][1]
        p2_visited.add((xsanta, ysanta))
    else:
        xrobo += offsets[d][0]
        yrobo += offsets[d][1]
        p2_visited.add((xrobo, yrobo))
    toggle = not toggle

print(len(p1_visited))
print(len(p2_visited))
