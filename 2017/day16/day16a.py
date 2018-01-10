#!/usr/bin/python

import sys

nslots = 16
data = [chr(ord('a') + i) for i in range(nslots)]

def spin(n):
    global data
    data = [data[(i - n) % nslots] for i in range(nslots)]

def exchange(a, b):
    data[a], data[b] = data[b], data[a]

def partner(a, b):
    exchange(data.index(a), data.index(b))

moves = [t for t in sys.stdin.readline().strip().split(',')]
for move in moves:
    if move[0] == 's':
        spin(int(move[1:]))
    elif move[0] == 'x':
        toks = move[1:].split('/')
        exchange(int(toks[0]), int(toks[1]))
    elif move[0] == 'p':
        toks = move[1:].split('/')
        partner(toks[0], toks[1])

print ''.join(data)
