#!/usr/local/bin/python

import sys

ln = sys.stdin.readline().strip()

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

print len(ln)
