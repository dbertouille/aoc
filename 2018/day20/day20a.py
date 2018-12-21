#!/usr/local/bin/python

import copy
import sys

ln = sys.stdin.readline().strip()
ln = ln[1:-1]

def doit(ln, grid, x, y, d, maxd, t):
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

            maxGrid = None
            for opt in options:
                subln = opt + ln[i:]
                if (d+len(subln)) < maxd:
                    continue
                gridCopy = copy.deepcopy(grid)
                optd = doit(subln, gridCopy, x, y, d, maxd, t+1)
                if optd > maxd:
                    maxd = optd
                    maxGrid = gridCopy

            if maxGrid is not None:
                for x in maxGrid:
                    if x not in grid:
                        grid[x] = dict()
                    for y in maxGrid[x]:
                        grid[x][y] = True
    
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
            grid[x][y] = True
            d += 1
        else:
            return d

    return d

print doit(ln, dict(), 0, 0, 0, 0, 1)
