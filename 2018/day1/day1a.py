#!/usr/local/bin/python
import sys

ln = sys.stdin.readline()
n = 0
while ln:
    ln = ln.strip()
    n += int(ln)
    ln = sys.stdin.readline()
print n
