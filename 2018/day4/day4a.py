#!/usr/local/bin/python

import operator
import sys

data = dict()
ln = sys.stdin.readline()
while ln:
    ln = ln.strip()

    date, time, action = ln.split(' ', 2)
    date = date.strip('[')
    time = time.strip(']')

    year, month, day = date.split('-')
    hour, minute = time.split(':')

    k = (int(year), int(month), int(day), int(hour), int(minute))
    data[k] = action

    ln = sys.stdin.readline()

asleepTimes = dict()
totalSleepTime = dict()

currGuard = None
asleepAt = None
totalAsleepByGuard = dict()
totalAsleepByGuardByMinute = dict()

keys = data.keys()
keys = sorted(keys)

for t in keys:
    action = data[t]
    minute = t[4]

    if "begins shift" in action:
        _, currGuard, _ = action.split(' ', 2)
        currGuard = int(currGuard.strip('#'))
        asleepAt = None
    elif action == "falls asleep":
        if currGuard is None:
            print "expected guard but have none"
            sys.exit(1)
        if asleepAt is not None:
            print "expected asleepAt none but have not none"
            sys.exit(1)
        asleepAt = minute
    elif action == "wakes up":
        if currGuard is None:
            print "expected guard but have none"
            sys.exit(1)
        if asleepAt is None:
            print "expected alseep but have none"
            sys.exit(1)
        if currGuard not in totalAsleepByGuard:
            totalAsleepByGuard[currGuard] = 0
        totalAsleepByGuard[currGuard] += minute - asleepAt
        for i in range(asleepAt, minute):
            if currGuard not in totalAsleepByGuardByMinute:
                totalAsleepByGuardByMinute[currGuard] = dict()
            if i not in totalAsleepByGuardByMinute[currGuard]:
                totalAsleepByGuardByMinute[currGuard][i] = 0
            totalAsleepByGuardByMinute[currGuard][i] += 1
        asleepAt = None

guardID = max(totalAsleepByGuard.iteritems(), key=operator.itemgetter(1))[0]
minute = max(totalAsleepByGuardByMinute[guardID].iteritems(), key=operator.itemgetter(1))[0]
print guardID * minute
