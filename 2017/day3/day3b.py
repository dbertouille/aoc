#!/usr/bin/python

target = 368078

depth = 0
moving = "right"

data = dict()

x = 0
y = 0
i = 1
while 1:
    total = 0
    for sx in [-1, 0, 1]:
        for sy in [-1, 0, 1]:
            if sx == 0 and sy == 0:
                continue
            if (x + sx) not in data or (y + sy) not in data[x + sx]:
                continue
            total += data[x + sx][y + sy]
    if total == 0:
        total = 1
    if total > target:
        print total
        break
    if x not in data:
        data[x] = dict()
    data[x][y] = total
    i += 1

    if moving == "right":
        x += 1
        if x > depth:
            depth += 1
            moving = "up"
    elif moving == "up":
        y += 1
        if y == depth:
            moving = "left"
    elif moving == "left":
        x -= 1
        if x == (depth * -1):
            moving = "down"
    else:
        y -= 1
        if y == (depth * - 1):
            moving = "right"
