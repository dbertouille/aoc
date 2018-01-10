#!/usr/bin/python

import sys

data_size = 256
data = [i for i in range(data_size)]
pos = 0
skip_size = 0
lengths = [int(t) for t in sys.stdin.readline().strip().split(',')]

for length in lengths:
    for i in range(length / 2):
        p1 = (pos + i) % data_size
        p2 = (pos + length - i - 1) % data_size
        data[p1], data[p2] = data[p2], data[p1]

    pos += length + skip_size
    pos %= data_size
    
    skip_size += 1

print data[0] * data[1]
