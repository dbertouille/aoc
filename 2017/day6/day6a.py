#!/usr/bin/python

import sys

ln = sys.stdin.readline().strip()
data = [int(t) for t in ln.split()]

seen = set()
while 1:
    idx = data.index(max(data))
    count = data[idx]
    data[idx] = 0
    for _ in range(count):
        idx += 1
        idx %= len(data)
        data[idx] += 1
    key = ' '.join([str(i) for i in data])
    if key in seen:
        break
    seen.add(key)

print len(seen) + 1
