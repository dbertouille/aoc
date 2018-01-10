#!/usr/bin/python

import math
import sys

def process(ln):
    toks = [t for t in ln.split(',')]
    x = 0
    y = 0
    z = 0
    for tok in toks:
        if 'n' == tok:
            y += 1
        elif 's' == tok:
            y -= 1
        elif 'ne' == tok:
            x += 1
            y += 0.5
        elif 'nw' == tok:
            x -= 1
            y += 0.5
        elif 'se' == tok:
            x += 1
            y -= 1
        elif 'sw' == tok:
            x -= 1
            y -= 0.5
    #print x, y, z
    print math.floor(max([abs(x), abs(y), abs(z)]))

ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    process(ln)
    ln = sys.stdin.readline()
