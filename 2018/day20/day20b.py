#!/usr/local/bin/python

import copy
import sys

ln = sys.stdin.readline().strip()
ln = ln[1:-1]

def doit(ln, grid, x, y, d, t):
    # print d, ln
    i = 0
    while i < len(ln):
        c = ln[i]
        i += 1

        if c == '(':
            depth = 0
            optstart = i
            options = []
            while ln[i] != ')' or depth > 0:
                if (ln[i] == '|' or ln[i] == ')') and depth == 0:
                    options.append(ln[optstart:i])
                    optstart = i + 1

                if ln[i] == '(':
                    depth += 1
                elif ln[i] == ')':
                    depth -= 1

                i += 1
            options.append(ln[optstart:i])
            i += 1

            maxd = d
            for opt in options:
                subln = opt + ln[i:]
                optd = doit(subln, grid, x, y, d, t+1)
                if optd > maxd:
                    maxd = optd
    
            # print '*'*t,maxd
            return maxd

        if c == 'W':
            x -= 1
        elif c == 'E':
            x += 1
        elif c == 'N':
            y += 1
        elif c == 'S':
            y -= 1

        if x not in grid:
            grid[x] = dict()
        if y not in grid[x]:
            d += 1
            grid[x][y] = d
        elif d < grid[x][y]:
            d += 1
            grid[x][y] = d
        else:
            return d

    return d

grid = dict()
print doit(ln, grid, 0, 0, 0, 1)

n1000 = 0
for x in grid:
    for y in grid[x]:
        if grid[x][y] >= 1000:
            n1000 += 1
print n1000
