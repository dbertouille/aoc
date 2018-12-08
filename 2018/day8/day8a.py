#!/usr/local/bin/python

import sys

ln = sys.stdin.readline().strip()
toks = ln.split()
s = 0

def parseNode(toks):
    global s

    nnodes = int(toks.pop(0))
    nmeta = int(toks.pop(0))
    
    for i in range(nnodes):
        parseNode(toks)

    for i in range(nmeta):
        s += int(toks.pop(0))

parseNode(toks)
print s
