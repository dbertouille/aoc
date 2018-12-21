#!/usr/local/bin/python

"""
r0 = 1
r1 
r2 = 0
r3 = 16
r5 = 0

r2 = r2 + 2
r2 = r2 * r2
r2 = r2 * r3
r2 = r1 * 11

r5 = r5 + 3
r5 = r5 * r3
r5 = r5 + 3

r2 = r5 + r2
r3 = r0 + r3

r5 = r3
r5 = r3 * r5
r5 = r3 + r5
r5 = r3 * r5
r5 = r5 * 14
r5 = r5 * r3
r2 = r2 + r5
r0 = 0
r3 = 0


r1 = 1

g2:
r4 = 1

g1:
r5 = r1 * r4

if r5 == r2:
    r0 = r0 + r1
r4 = r4 + 1
if r4 <= r2:
    goto g1
r1 = r1 + 1
if r1 <= r2:
    goto g2:
"""


n = 10551305
s = 0
for i in range(1, 10551305+1):
    if (n % i) == 0:
        s += i
print s
