#!/usr/local/bin/python

import sys

ln = sys.stdin.readline()
data = dict()

noCollisionIDs = set()

while ln:
    ln = ln.strip()
    claimID, _, loc, sz = ln.split()
    noCollisionIDs.add(claimID)
    x, y = loc.strip(':').split(',')
    w, h = sz.split('x')
    for i in range(int(x),int(x)+int(w)):
        if i not in data:
            data[i] = dict()
        for j in range(int(y), int(y)+int(h)):
            if j not in data[i]:
                data[i][j] = claimID
            else:
                if claimID in noCollisionIDs:
                    noCollisionIDs.remove(claimID)
                if data[i][j] in noCollisionIDs:
                    noCollisionIDs.remove(data[i][j])
    ln = sys.stdin.readline()

print noCollisionIDs.pop()
