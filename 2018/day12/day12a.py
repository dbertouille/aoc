#!/usr/local/bin/python

import pprint
import sys

# Initial State
ln = sys.stdin.readline().strip()
ln = ln.split(':')[1].strip()
data = []
for c in ln:
    data.append(c)

# Skip blank
ln = sys.stdin.readline()

rules = dict()
ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    req, _, res = ln.split(' ')
    d = rules
    for i in range(len(req)):
        if i == (len(req) - 1):
            d[req[i]] = res
        else:
            if req[i] not in d:
                d[req[i]] = dict()
            d = d[req[i]]
    ln = sys.stdin.readline()

print '0 : ',
for x in data:
    print x,
print ''

iterations = 20
for i in range(iterations):
    newData = []
    for j in range(-2, len(data)+2):
        k1 = (data[j-2] if j >= 2 else '.')
        k2 = (data[j-1] if (j >= 1 and j < (len(data) + 1)) else '.')
        k3 = (data[j] if (j >= 0 and j < len(data)) else '.')
        k4 = (data[j+1] if (j >= -1 and j < (len(data) - 1)) else '.')
        k5 = (data[j+2] if (j >= -2 and j < (len(data) - 2)) else '.')
        if k1 in rules and k2 in rules[k1] and k3 in rules[k1][k2] and k4 in rules[k1][k2][k3] and k5 in rules[k1][k2][k3][k4]:
            newData.append(rules[k1][k2][k3][k4][k5])
        else:
            newData.append('.')
    data = newData

    print str(i+1).ljust(2),': ',
    for x in data:
        print x,
    print ''

s = 0
for i in range(len(data)):
    if data[i] == '#':
        print (i - iterations*2)
        s += (i - iterations*2)
print s
