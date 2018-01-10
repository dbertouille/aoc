#!/usr/bin/python

import sys
ln = sys.stdin.readline().strip()

print sum([int(ln[i]) if ln[i] == ln[(i+1) % len(ln)] else 0 for i in range(len(ln))])
