#!/usr/bin/python

a_factor = 16807
b_factor = 48271
base = 2147483647

# a = 65
a = 783
# b = 8921
b = 325

n = 40000000

c = 0
for _ in range(n):
    a = (a * a_factor) % base
    b = (b * b_factor) % base
    if (a & 65535) == (b & 65535):
        c += 1
print c
