#!/usr/local/bin/python

import operator

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


n = Node(0)
n.next = n
n.prev = n

nturns = 7197500
nplayers = 416
player = 0
scores = dict()

for i in range(1,nturns+1):
    if (i % 1000 ) == 0:
        print i,'/',nturns

    if (i % 23) == 0:
        if player not in scores:
            scores[player] = 0
        scores[player] += i
        for i in range(7):
            n = n.prev
        scores[player] += n.val
        n.prev.next = n.next
        n = n.next
    else:
        n = n.next

        newNode = Node(i)
        newNode.prev = n
        newNode.next = n.next

        n.next.prev = newNode
        n.next = newNode

        n = newNode

    player = (player + 1) % nplayers

print max(scores.iteritems(), key=operator.itemgetter(1))[1]
