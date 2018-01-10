#!/usr/bin/python

import pprint

def knot_hash(k):
    data_size = 256
    data = [i for i in range(data_size)]
    pos = 0
    skip_size = 0
    lengths = [ord(c) for c in k] + [17, 31, 73, 47, 23]

    for _ in range(64):
        for length in lengths:
            for i in range(length / 2):
                p1 = (pos + i) % data_size
                p2 = (pos + length - i - 1) % data_size
                data[p1], data[p2] = data[p2], data[p1]

            pos += length + skip_size
            pos %= data_size
            
            skip_size += 1

    dense_data = []
    for i in range(16):
        v = 0
        for j in range(16):
            v ^= data[i * 16 + j]
        dense_data.append(v)

    s = ''.join(["%02x" % v for v in dense_data])

    return s

#key_prefix = 'flqrgnkx'
key_prefix = 'hwlqcszp'

data = []

for i in range(128):
    key = '%s-%d' % (key_prefix, i)
    h = knot_hash(key)
    row_data = []
    for c in h:
        n = int(c, 16)
        for j in reversed(range(4)):
            if (n & (2 ** j)) != 0:
                row_data.append({'filled': True, 'region': None})
            else:
                row_data.append({'filled': False})
    data.append(row_data)

next_region = 0

def explore(i, j, r):
    if i < 0 or i >= 128:
        return
    if j < 0 or j >= 128:
        return
    if not data[i][j]['filled']:
        return
    if data[i][j]['region'] is not None:
        return

    data[i][j]['region'] = r
    explore(i -1, j, r)
    explore(i + 1, j, r)
    explore(i, j - 1, r)
    explore(i, j + 1, r)

for i in range(128):
    for j in range(128):
        if not data[i][j]['filled']:
            continue
        if data[i][j]['region'] is not None:
            continue
        next_region += 1
        explore(i, j, next_region)

print next_region
