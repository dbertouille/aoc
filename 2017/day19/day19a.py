#!/usr/bin/python

import sys

data = []

ln = sys.stdin.readline()
while ln:
    data.append([c for c in ln[:-1]])
    ln = sys.stdin.readline()

x = 0
y = 0
for i in range(len(data[0])):
    if data[0][i] == '|':
        x = i
        break

moving = 'down'
letters = []

while 1:
    if data[y][x] == ' ':
        break

    if data[y][x] >= 'A' and data[y][x] <= 'Z':
        letters.append(data[y][x])

    if moving == 'down':
        y += 1
        if data[y][x] == '+' and data[y][x - 1] != ' ':
            moving = 'left'
        elif data[y][x] == '+' and data[y][x + 1] != ' ':
            moving = 'right'

    elif moving == 'right':
        x += 1
        if data[y][x] == '+' and data[y - 1][x] != ' ':
            moving = 'up'
        elif data[y][x] == '+' and data[y + 1][x] != '':
            moving = 'down'

    elif moving == 'up':
        y -= 1
        if data[y][x] == '+' and data[y][x - 1] != ' ':
            moving = 'left'
        elif data[y][x] == '+' and data[y][x + 1] != ' ':
            moving = 'right'

    elif moving == 'left':
        x -= 1
        if data[y][x] == '+' and data[y - 1][x] != ' ':
            moving = 'up'
        elif data[y][x] == '+' and data[y + 1][x] != '':
            moving = 'down'


print ''.join(letters)
