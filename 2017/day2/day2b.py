#!/usr/bin/python

import sys

ln = sys.stdin.readline()
s = 0
while ln:
    ln = ln.strip()
    numbers = [int(n) for n in ln.split()]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if (numbers[i] % numbers[j]) == 0:
                s += numbers[i] / numbers[j]
    ln = sys.stdin.readline()
print s
