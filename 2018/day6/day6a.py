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


closestCountsByPoint = dict()
infiniteAreas = set()

for x in range(minX, maxX):
    for y in range(minY, maxY):
        closestPoint = None
        closestDistance = None
        isMultiple = False
        for p in points:
            d = abs(p[0] - x) + abs(p[1] - y)
            # print x,y,p,d
            if closestDistance is None or d < closestDistance:
                closestPoint = p
                closestDistance = d
                isMultiple = False
            elif d == closestDistance:
                isMultiple = True
        if isMultiple or closestPoint in infiniteAreas:
            continue
        if x == minX or x == maxX or y == minY or y == maxY:
            infiniteAreas.add(closestPoint)
            continue
        if closestPoint not in closestCountsByPoint:
            closestCountsByPoint[closestPoint] = 0
        closestCountsByPoint[closestPoint] += 1

# print infiniteAreas
# print closestCountsByPoint
print max(closestCountsByPoint.iteritems(), key=operator.itemgetter(1))[1]
