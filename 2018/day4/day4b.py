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
        for i in range(asleepAt, minute):
            if currGuard not in totalAsleepByGuardByMinute:
                totalAsleepByGuardByMinute[currGuard] = dict()
            if i not in totalAsleepByGuardByMinute[currGuard]:
                totalAsleepByGuardByMinute[currGuard][i] = 0
            totalAsleepByGuardByMinute[currGuard][i] += 1
        asleepAt = None

maxGuardID = None
maxMinute = None
maxCount = 0
for guardID in totalAsleepByGuardByMinute:
    for minute in totalAsleepByGuardByMinute[guardID]:
        if totalAsleepByGuardByMinute[guardID][minute] > maxCount:
            maxCount = totalAsleepByGuardByMinute[guardID][minute]
            maxGuardID = guardID
            maxMinute = minute
print maxGuardID * maxMinute
