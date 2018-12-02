#!/usr/local/bin/python
import sys

data = []
ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    data.append(int(ln))
    ln = sys.stdin.readline()

seen = set()
c = 0
i = 0

while True:
    c += data[i % len(data)]
    if c in seen:
        print c
        break
    seen.add(c)
    i += 1
