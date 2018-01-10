#!/usr/bin/python

import sys

ln = sys.stdin.readline()
s = 0
while ln:
    ln = ln.strip()
    numbers = [int(n) for n in ln.split()]
    s += (max(numbers) - min(numbers))
    ln = sys.stdin.readline()
print s
