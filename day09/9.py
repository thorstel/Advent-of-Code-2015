import fileinput
import itertools

cities = set()
distance = {}
for line in fileinput.input():
    src, _, dst, _, dist = line.strip().split()
    distance.setdefault(src, {})[dst] = int(dist)
    distance.setdefault(dst, {})[src] = int(dist)
    cities.add(src)
    cities.add(dst)

routes = []
for perm in itertools.permutations(cities):
    dist = 0
    for src, dst in zip(perm, perm[1:]):
        if src in distance and dst in distance[src]:
            dist += distance[src][dst]
        else:
            break
    else:
        routes.append(dist)

print(min(routes))
print(max(routes))
