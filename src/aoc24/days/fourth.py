# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pathlib

def xmas_search(lines, x, y) -> int:
    count = 0
    x_size = len(lines)
    print(f'xsize {x_size}')
    y_size = len(lines[0])
    print(f'ysize {y_size}')
    for aa in [-1, 0, 1]:
        for bb in [-1 , 0 , 1]:
            if aa == 0 and bb == 0:
                continue 
            sample = ''
            for cc in range(4):
                new_x = x + aa * cc
                new_y = y + bb * cc
                # don't wrap
                if new_x < 0 or new_y < 0 or new_x >=  x_size or new_y >= y_size:
                    continue 
                sample += lines[new_x][new_y]
            if sample == 'XMAS':
                count += 1
    return count


def part_one(path: pathlib.Path) -> int:
    """search"""

    # Read into numpy array

    # search for X's and return coordinates

    lines = []
    xs = 0
    with path.open() as f:
        lines = [line.rstrip() for line in f]
    for ii in range(len(lines)):
        for jj in range(len(lines[0])):
            if lines[ii][jj] == 'X':
                xs += xmas_search(lines, ii, jj)
    


    return xs

def x_mas(lines , y, x) -> int:

    diag_1 = lines[y - 1][x - 1] + lines[y][x] + lines[y + 1][x + 1]
    diag_2 = lines[y - 1][x + 1] + lines[y][x] + lines[y + 1][x - 1]

    if (diag_1 == 'MAS' or diag_1 == 'SAM') and (diag_2 == 'MAS' or diag_2 == 'SAM'):
        return 1
    return 0

def part_two(path: pathlib.Path) -> int:
    lines = []
    x_masses = 0
    with path.open() as f:
        lines = [line.rstrip() for line in f]
    for ii in range(1,len(lines) - 1):
        for jj in range(1, len(lines[0]) - 1):
            if lines[ii][jj] == 'A':
                x_masses += x_mas(lines, ii, jj)
    return x_masses