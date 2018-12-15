#!/usr/local/bin/python

import sys

scores = [3,7]
e1idx = 0
e2idx = 1
t = str(702831)

while True:
    #print scores
    ss = scores[e1idx] + scores[e2idx]

    if ss >= 10:
        scores.append(int(ss/10)%10)
        if len(scores) >= len(t) and ''.join([str(n) for n in scores[len(t)*-1:]]) == t:
            break
            

    scores.append(ss%10)
    if len(scores) >= len(t) and ''.join([str(n) for n in scores[len(t)*-1:]]) == t:
        break

    e1idx = (e1idx + scores[e1idx] + 1) % len(scores)
    e2idx = (e2idx + scores[e2idx] + 1) % len(scores)

print len(scores) - len(t)
