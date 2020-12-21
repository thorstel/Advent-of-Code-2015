import math

with open('input.txt', 'r') as file:
    data = file.read().splitlines()

paper = 0
ribbon = 0

for elem in data:
    dim = [int(x) for x in elem.split('x')]
    dim.sort()
    sides = [dim[0] * dim[1], dim[0] * dim[2], dim[1] * dim[2]]
    paper += (2 * sum(sides)) + min(sides)
    ribbon += (2 * dim[0]) + (2 * dim[1]) + math.prod(dim)

print(paper)
print(ribbon)
