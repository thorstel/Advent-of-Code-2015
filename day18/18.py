from collections import *
from math import *
import itertools
import re
import sys

def solve(data, steps = 100):
    starting_grid = data.splitlines()
    grid = starting_grid
    dim = len(grid)

    def count(row, col):
        cnt = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r < 0 or r >= dim or c < 0 or c >= dim:
                    continue
                if r == row and c == col:
                    continue
                if grid[r][c] == '#':
                    cnt += 1
        return cnt

    # Part 1
    for _ in range(steps):
        new_grid = []
        for r in range(dim):
            row = ''
            for c in range(dim):
                cnt = count(r, c)
                if grid[r][c] == '#':
                    row += '#' if 2 <= cnt <= 3 else '.'
                else:
                    row += '#' if cnt == 3 else '.'
            new_grid.append(row)
        grid = new_grid
    print(sum(sum(1 for c in row if c == '#') for row in grid))

    # Part 2
    grid = starting_grid
    for _ in range(steps):
        new_grid = []
        for r in range(dim):
            row = ''
            for c in range(dim):
                if (r, c) in [(0, 0), (0, dim - 1), (dim - 1, 0), (dim - 1, dim - 1)]:
                    row += '#'
                else:
                    cnt = count(r, c)
                    if grid[r][c] == '#':
                        row += '#' if 2 <= cnt <= 3 else '.'
                    else:
                        row += '#' if cnt == 3 else '.'
            new_grid.append(row)
        grid = new_grid
    print(sum(sum(1 for c in row if c == '#') for row in grid))

########################################################################
#                             SETUP STUFF                              #
########################################################################

actual_input = r"""
####.#.##.###.#.#.##.#..###.#..#.#.#..##....#.###...##..###.##.#.#.#.##...##..#..#....#.#.##..#...##
.##...##.##.######.#.#.##...#.#.#.#.#...#.##.#..#.#.####...#....#....###.#.#.#####....#.#.##.#.#.##.
###.##..#..#####.......#.########...#.####.###....###.###...#...####.######.#..#####.#.###....####..
....#..#..#....###.##.#.....##...#.###.#.#.#..#.#..##...#....#.##.###.#...######......#..#.#..####.#
..###.####..#.#.#..##.#.#....#......#.##.##..##.#.....##.###.#..###...###.#.##..#.#..###....####.#.#
#.#...#......####.#..##.####.#.#.#...##..###.##.#...#..#..###....#.#....#..##..#....##.....##.#...#.
....##.#.#.#.##..##...##..##..#....#....###...####.###...##.#...#..#....##.....#..#.#####.###.###.##
#...##..#.#..#....#..########.##....##..##.###..#.#..#..#.##.##.#..##..######....####..#####.#.###..
.####...######.#..#.##.#.#..####...####.##.#.#......#...##....##..#...###..#.####......###......#.##
.####.###..#..#####.##...###......#...###..#..##..#.#....##.##.#.##.###..#..#..###.#..#.#....####.##
#..#..##.##.##.###.#.##.##.#.#.#....#....#.####.#.##...#####...###.#####.#.#.#....####..###..###..##
#.##....#...########..##...#.#.##.......#.#..##...####...#.####.####..##...##.#....###.#.####...#.##
#.#...##..#.##.##..##....#.....##.##.....#...###...#..#...####.##.####..#...##..##.##.##.##..##...##
.#..###...#.#.....#######..##.###....##..#.##.#......###.##....#......###...#.##....#.....##......##
..##....#.###...###..####.##..#..##.##......##.#.....#...#..#..##...###..#.####...#...#..##.#..##..#
...#.#.#...#.#..#.##....##..#...#.##..#......#.#.....#####.##.#...#######.#.#..#.####..###.....###.#
.#....#.#.##..####.#####..#.#######..#.##.###...##.##....##..###..#.##.###.......#....#..######.####
#..#.##.##..#..#..##.####.#.#.#.#..#.##...#..######....#.##.#..##.##.######.###.###.###...#.....#.#.
.#.......#...#.####.##...#####..##..#.#....##..#.#.#.####.#.##....#..##.##..#.###.....#.##.##.#.##.#
#..##..##...#....#.##.#...#.#....#......####...##..#...##.##.#..#########..#..#.##.##..#.#.#######..
#.......#####..###..######.#..##.#.#####..##...###...#.####.##...###..#.#.#####....#...#.##...#.#..#
.##..#...#####.##.##......#...#.#.#.###.#.#.#...##.#..#....###.....#..#.#.###......#####.###.#..##.#
.....###.#.#.#..##...#...###..#...#.#.##..###.##.#####.##..#.#.#.#.#####....#.#.#####...##.#..#.#.#.
###...##.#..#.####..##.#..##.#.#.#...#.#..#..##..##..#.#.#.#.##...##..#..#.....#....#####.#.#.####.#
....##....#.#.....#...###.#...##..##.##..#..###..##.###..#####..#...#####.##.#..#.#.#.###...####.###
##.##.##.#...#..#...........##.##.###.#...###.####.#..#..#...#..#..####.#.###########..#.###.###.#.#
##.##..##.####..###...##...#....###.###.#..##..#..#.###.#..####.#..##.#.#...#..#.#.##.##...#...#....
..##...#.#.##....##...#.#.#......##.##.#.#.####.####....####.#.###.##.#.#..####..#..######..#..#.#..
####.#.##.......##.###....##.#..####.#.#######..#...###..##.##..#...#...####........#.#..##...#....#
#..#.#.....#..#.###..#.#...###..##...#.#..#.#.##..#...##.##.##.#.#.#..#.####.########....########..#
#...#..##.##..#.#.#.##.##.##.#..#..#.##....#....###.#.###.#.#..#....#...##..#.....####...##.#..#...#
.###...##...####....###.##.#..####...##.#.##.#..##..##....#....##.#...#..#..##..##..##.#...#...###..
.#..##.#..##..####..#.#.##..###.#...#....##.###...#.###....#.#.#........#..#.#.#..##..#####..#..#.#.
.#.##.....#..#...#.##.....#.##..#..#....#..#..#....#.##..##...#.##.##..##..#.#.#.##..####.##..#.#..#
...###.#.....#...#.##.#.###.#...##..#.###..#..#..#.#..#...###.#.##.##.##.#.##.#####.#..#.#..#.#...##
#.#.#.#.##.#.....##..#.###......##.#.##..#...#.########.##.###..#..#..##..##.#..##..###.#.###...#.#.
..##...##...#...###.#..##..#..#..#.#.##..##......##..##.....##.....####..#.##......#..####...###..##
##.......#..##....###...###......#.##.##....######..###.##...##.#...#...#.....#.###.#.#..#.##..#..#.
#.#..#..#.#####.##.##.###..#...###.....#..##..####...#.#.###....#..#.#.###.####..#.#........##.#....
..###.#...##.#.####.#.##.##.....##...#.##.#.###.#.#..##.#..##..#..##.##....#.#####.##..#######.....#
###.###..##.#..##...#####..##.####....#.##......##......#.#....##.####.#.#.#.###...#..####..#.######
#..###...#.#.......#..####.####...#....###.###...#.##..##..#..##.##.......####.##...#.#.#.##.#.#..#.
..#...#..###.##..#.#.#.##..#..#.#.......###..###..#####.#.#.#.#.#..#.#.#.#..###....#.####..###...#..
...######.###....#..####.####......#...#.###.#....#...####.##........##...##.#..##.###.#..#..##..###
.#..###.####.###.#.#..#..#..#.##.#.#.###.##..####.#####..##....##.#.##...###.####.#.#######.#..#..#.
.#..##.#..##..#...##...#..#..##.#.#....##.##...###.#.#...##..##..#.###.#.#.#.#...#....#.#..#.#.###.#
.###..#.#..####.#########...####....####.#.##...##.##..#.##.#........#.....###.###.######.##.....###
..##.##..##..#.####.#..#####.#....##.##.#####.....#.#......##...#####..####....###..#.#...#..####..#
.#..##..##.##.##.##.#.###.###.#..#..#...###.#.##..##...##...###...##.###..#.#.#####.#.#.##....#.##..
...#.#....##.#.....###.##...#..##....#...###....#..#.###...##.#...###.#....#...##..###.#.....##....#
.#######..#...##.#.###.##.#.###...##......#.###.#...#.###.#.#.#..#..#####..#########...##..##...#..#
.#..#.##...#.#..#.##..#.#.#.##.....####.#..#.###..##.#.#.#...#....#.#..##.######...#.#..##.##...#..#
#.#######.#####..#####.##.##.#.#.##.###..#....####.#..##.##.######..###...#.#..#.####.##.##....####.
...##..#...##..#..#.....#.##...#.....##.#####.###.########.######..#...###..#.##.#.#.##..#.#.##..##.
#..#..#.#....###.#...##..####.#.##..#.####.###..##.#...#.###.#..#.##..#######.#...#..#.#..##.#....##
..#.##.#.####..##.###.###..#.##.#.####..##....##.###.#..##.#.###.###.##.##.#####..#.#...########....
.#.#.###..###...#...#..##.##......#..#...#.#.#.######.#.#...##..##........#....###..##...#..##.##...
##..#....##.###...##.#.##.##.##..#....#.#.#..#..####.##..#...#...#..#..#####.###...#..###..#...#.#..
##.#.#.##.###.....######.#.....#...#.##....###.#.##.#.#.##..##.######.#####....#.#####...##.#..###.#
######.#...####..###..##..#..##...#.#....##.#...##...#.....#...##....#.##..###..###...###..#..######
.....##.........#####.#.##..#..#.#.#.#.##...#....#.....###.########...#..####..#...#...##..#.##.##.#
#..###...#.##.##.#.#..####.#.....##..###....##..#...#.#...##.##..###..####...#.####..##..#..##..#...
#.####.#..##.#..#.....#..#.#..###...######.#.........####....###..#.#.#.##.#..#...#..####.....##..#.
..##....#.###.......##.#...#.####..##....##.#..#....#######...####.##..#####.#.#.#.#.##..##..#.#.#..
#.#.#.###..#..#.#..#.#.###....#...#####.###...........#.#....#####...#..####....#...###.#..#..####..
.......#.####.##...#..#.##..###..#..#.#.#.#.###....#....#.#.#..#.#..##.#####.#.....#.##.#.###.###.##
..###...#..#...####.#..##..##.#.#..#...#.#..#....###.#..####..######...####.#.##..#.#..###...##.####
..#.###..#.#...##...#.#....#..#...#.#..##.######.######.#.##.....#..##.#..###..#..#.##.###...#..#.##
####..##.####.....#...#.#.###..#...####.###.#.#.#.......##...#....#..#....#.#......###...#####.#.##.
#..##..#..#.####...#####.#.###.##.#.##.....#.#..#.##........######.#.#.###....##.##..##..########.##
#.#....###.##....#######.#...#.#.#.#..##.#.##...#.###...#.#.#..#.#..####.#.#..#..#.##.####....#..##.
####.##....#.......###..#..##.#.#.##..#...#...##.###....##..###.#.#...#..#.....##.###.##...###....##
..##.#..#....######..#.##.#.#...##..####.#####...##.#..###.##...#..####..###.##..##.##.#####.#..#.#.
.#.##..#..##.#.###.###....#.#..#....#...###.##.#.#.####.....#....#...#.....#....#.#.###.#..#.##..###
..###.#.#.##...##.##.##.#...#####.#..##.#....##..####...###..#....#.##...#........#####.#.###.#..#..
....#..##..##....#.#....#.#..##...##.#...##.###.#.#..###..##.##.##..#.#.#..#.#.##.......#.##.###..#.
.#..##.##.####.##....##.##.....###..##.#.##...#..###....###.###....#.#....#....#.##.#.##.#.##.....##
#.#..#.##.###.#.######.....###.#..#...#.#.....##.###.#...#.#..###.#.....##.###.#.###.####..#####.#..
#.#.##......#.##.#.#..##....#..###.#.###...##...###.#..#.##...#..#.##..##.#...######.##.....#####.##
#.#..#####....###.###...#.......#....###.##...#..#.##..#...#####..#..#.##......###...#...###..#.#..#
#.##..##.##.#..#.##.##..#.###.##.........###.#.#..#.#.....#.#...#.#.##.#.##.#...#...####.#.......##.
.#...####.##..#..##....####..######...#.#..##.##.....#####.#...#..#.####.#######...#.#####..#.###...
.#..######.#.##..##...##.....###.#..##..#...####..###...###.###..#..######.#....########..#####...#.
#..##.......#####...###..#.#.##.#..###.#...##.#..#.##.###...###...##.#..##..########..#.#..##..#.###
.#.#..#...#.#..#..##...#.#.##...###..#..#....###.#....#.##....###.###..##..#.#.####..####.#######.##
...##..##.##.###.##.###...##.#.#.....##.####..#..##.#..#.####...##..#..#.##...##...###.##.#.......##
.#.....#.##..#.#.....#.##.##..###..#....###...#.#....##########.##.###.#...#.####..####.#..#.#..###.
.##.#.#.##..#..###.###.##.#########.#.#.#.#.##.###..##..#.##.####......#####...#..####.#.##..#####.#
..#....###...##....#.###..##..#..####.##..####.#..####.###.#....####.....#.###..##...##..####...##.#
.###.....###.##.##..###.###.....##..#.######.#.#..##..#.##.#..#.#.#....#...#.#.#...#...##....#..##.#
..##....#..#####....#..####.#.#...##.#....##..##.###.###....###......#...#.#####.......#...#.....###
###.#..#.#.##..#..#...#.#....###.##.#.###.#...#.##.#..#.#.......#.#.#.###.####.###....#..##..#####..
.#..#######.#..###.#.##.#####.#####...##..#.####.#.#.##..###...#..##.##..#.#.###..#....#..#...###.#.
..#####..#.##.....###..##.#...#.#.#..#######.#..#...#.##.##.#.#....####...###..##...#....####.#..#.#
.####..#.#.##.###.#.##.....#..##.#.....###.....#..##...#....###.###..#......###.#.#.#.##.#.##..#...#
##.#..##.#..##...#.#....##..######..#.....#..#...#####....##......####.##..#...##..#.##.#.#######..#
##..####.#...##...#.#####.#.#..#....#.#..##.####.#..######.#..#..#.......#####..#..#..###.##...##.##
#.####......#.###...#..####.#..##.##..#.#...##.###.#...#####..####.#..#.#.....#.##...###...#.#....##
###.#.#.##.######......#.#.#.#.#........#..#..###.#.#.#..#.........#..#....#.#..#..#..###.##......##
##.#########...#...###..#.###.....#.#.##.........###....#.####.#...###.#..##..#.###..#..##......#.##
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    solve(actual_input)
