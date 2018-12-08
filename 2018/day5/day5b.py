#!/usr/local/bin/python

import sys

og = sys.stdin.readline().strip()

uniqueUnits = set()
for c in og:
    uniqueUnits.add(c.lower())

n = 0
minLen = None
for toRemove in uniqueUnits:
    print n, '/', len(uniqueUnits)
    n += 1

    ln = og.replace(toRemove, '')
    ln = ln.replace(toRemove.upper(), '')

    madeChange = True
    startAt = 0
    while madeChange and startAt < (len(ln) - 1):
        madeChange = False
        prev = ln[startAt]
        for i in range(startAt + 1, len(ln)):
            curr = ln[i]
            if prev != curr and prev.lower() == curr.lower():
                ln = ln[:i-1] + ln[i+1:]
                madeChange = True
                break
            prev = curr
            startAt = max(i - 2, 0)

    if minLen is None or len(ln) < minLen:
        minLen = len(ln)

print minLen
