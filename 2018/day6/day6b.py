#!/usr/local/bin/python

import operator
import sys

points = []
ln = sys.stdin.readline()
minX = None
maxX = None
minY = None
maxY = None

while ln:
    ln = ln.strip()
    x,y = ln.split(',')
    x = int(x.strip())
    y = int(y.strip())
    if minX is None or x < minX:
        minX = x
    if maxX is None or x > maxX:
        maxX = x
    if minY is None or y < minY:
        minY = y
    if maxY is None or y > maxY:
        maxY = y
    points.append((x,y))
    ln = sys.stdin.readline()


n = 0
for x in range(minX, maxX):
    for y in range(minY, maxY):
        totalD = 0
        for p in points:
            totalD += abs(p[0] - x) + abs(p[1] - y)
        if totalD < 10000:
            n += 1
print n
