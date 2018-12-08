#!/usr/local/bin/python

import sys

ln = sys.stdin.readline().strip()
toks = ln.split()

def parseNode(toks):
    nnodes = int(toks.pop(0))
    nmeta = int(toks.pop(0))
    childValues = []

    for i in range(nnodes):
        childValues.append(parseNode(toks))

    v = 0
    for i in range(nmeta):
        m = int(toks.pop(0))
        if nnodes == 0:
            v += m
        elif m >= 1 and m <= len(childValues):
            v += childValues[m-1]

    return v

print parseNode(toks)
