#!/usr/bin/python

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

key_prefix = 'hwlqcszp'

count = 0
for i in range(128):
    key = '%s-%d' % (key_prefix, i)
    h = knot_hash(key)
    for c in h:
        n = int(c, 16)
        for j in range(4):
            if (n & (2 ** j)) != 0:
                count += 1
print count
