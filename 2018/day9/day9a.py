#!/usr/local/bin/python

import operator

data = [0]

nturns = 71975
nplayers = 416

pos = 0
player = 0
scores = dict()

for i in range(1,nturns+1):
    if (i % 1000 ) == 0:
        print i,'/',nturns
    if (i % 23) == 0:
        if player not in scores:
            scores[player] = 0
        scores[player] += i
        pos = (pos - 7) % len(data)
        scores[player] += data.pop(pos)
    else:
        idx = (pos + 1)  % len(data) + 1
        data.insert(idx, i)
        pos = idx
    # print data
    player = (player + 1) % nplayers

print max(scores.iteritems(), key=operator.itemgetter(1))[1]
