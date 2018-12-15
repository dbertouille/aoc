#!/usr/local/bin/python

import sys

scores = [3,7]
e1idx = 0
e2idx = 1

n = 702831

n += 10

while True:
    #print scores
    ss = scores[e1idx] + scores[e2idx]

    if ss >= 10:
        scores.append(int(ss/10)%10)
    if len(scores) >= n:
        break

    scores.append(ss%10)
    if len(scores) >= n:
        break

    e1idx = (e1idx + scores[e1idx] + 1) % len(scores)
    e2idx = (e2idx + scores[e2idx] + 1) % len(scores)

print scores[-10:]
print ''.join([str(n) for n in scores[-10:]])
