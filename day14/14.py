import itertools
import re
import sys

def calc_dist(target, speed, dur, pause):
    period = dur + pause
    dist = int(target / period) * speed * dur
    dist += min(target % period, dur) * speed
    return dist

def solve(data, target = 2503):
    max_dist = 0
    deers = []
    score = {}
    for line in data.splitlines():
        xs = line.split()
        name, speed, dur, pause = xs[0], int(xs[3]), int(xs[6]), int(xs[13])
        dist = calc_dist(target, speed, dur, pause)
        max_dist = max(dist, max_dist)
        deers.append((name, speed, dur, pause))
        score[name] = 0
    print(max_dist)

    for sec in range(1, target + 1):
        distances = [(name, calc_dist(sec, s, d, p)) for name, s, d, p in deers]
        winning_dist = max(x for _, x in distances)
        for name, dist in distances:
            if dist == winning_dist:
                score[name] += 1
    print(max(score.values()))

########################################################################
#                             SETUP STUFF                              #
########################################################################

sample_input = r"""
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip()

actual_input = r"""
Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    print('=== SAMPLE ===')
    solve(sample_input, 1000)
    print('=== ACTUAL ===')
    solve(actual_input)
