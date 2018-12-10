#!/usr/local/bin/python

import sys

class Node:
    def __init__(self, p, v):
        self.p = p
        self.v = v

nodes = []

ln = sys.stdin.readline()
while ln:
    start = ln.index('<')
    end = ln.index('>')
    x, y = ln[start+1:end].split(',')
    x = int(x.strip())
    y = int(y.strip())

    ln = ln[end+1:]
    start = ln.index('<')
    end = ln.index('>')
    vx, vy = ln[start+1:end].split(',')
    vx = int(vx.strip())
    vy= int(vy.strip())

    nodes.append(Node([x,y], [vx,vy]))

    ln = sys.stdin.readline()

for i in range(100000):
    data = dict()
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    for n in nodes:
        x = n.p[0]
        y = n.p[1]
        if x not in data:
            data[x] = dict()
        data[x][y] = True
        minX = min(x, minX)
        maxX = max(x, maxX)
        minY = min(y, minY)
        maxY = max(y, maxY)

    #print maxX-minX,maxY-minY
    if (maxX - minX) < 300 and (maxY - minY) < 300:
        print '\n\n'
        print i
        for y in range(maxY, minY - 1, -1):
            for x in range(minX, maxX+1):
                if x in data and y in data[x]:
                    print '#',
                else:
                    print '.',
            print ''

    for n in nodes:
        n.p[0] += n.v[0]
        n.p[1] += n.v[1]
