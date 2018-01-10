#!/usr/bin/python

import sys

ln = sys.stdin.readline().strip()
data = [int(t) for t in ln.split()]

seen = set()
loopstart = None
inloop = False
loopsize = 0
while 1:
    idx = data.index(max(data))
    count = data[idx]
    data[idx] = 0
    for _ in range(count):
        idx += 1
        idx %= len(data)
        data[idx] += 1
    key = ' '.join([str(i) for i in data])
    if not inloop:
        if key in seen:
            inloop = True
            loopstart = key
        seen.add(key)
    elif key == loopstart:
        break
    else:
        loopsize += 1

print loopsize + 1
