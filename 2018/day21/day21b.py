#!/usr/local/bin/python

import sys

r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

seen = set()
lastr3 = None

def code28():
    global r0,r1,r2,r3,r4,r5,seen,lastr3
    if r3 in seen:
        print lastr3
        sys,exit(0)
    lastr3 = r3
    seen.add(r3)
    if r3 == r0:
        sys.exit(0)
    return code6

def code26():
    global r0,r1,r2,r3,r4,r5

    r2 = r5
    return code8

def code6():
    global r0,r1,r2,r3,r4,r5

    r2 = r3 | 65536
    r3 = 1397714
    return code8

def code8():
    global r0,r1,r2,r3,r4,r5

    r5 = r2 & 255
    r3 = r3 + r5
    r3 = r3 & 16777215
    r3 = r3 * 65899
    r3 = r3 & 16777215
    if 256 > r2:
        return code28
    r5 = 0
    return code18

def code18():
    global r0,r1,r2,r3,r4,r5

    r1 = r5 + 1
    r1 = r1 * 256
    if r1 > r2:
        return code26
    r5 = r5 + 1
    return code18

while True:
    r3 = 123
    r3 = r3 & 456
    if r3 == 72:
        break

r3 = 0
n = code6()
while True:
    n = n()
