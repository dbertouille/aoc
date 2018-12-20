#!/usr/local/bin/python

import sys

data = dict()
gxmin = None
gxmax = None
gymin = None
gymax = None

def printData():
    global data, gxmin, gxmax, gymin, gymax
    for y in range(gymin, gymax+1):
        for x in range(gxmin, gxmax+1):
            if y in data and x in data[y]:
                print data[y][x],
            else:
                print '.',
        print ''
    print ''

def setDataElement(y, x, c):
    global data, gxmin, gxmax, gymin, gymax
    if y not in data:
        data[y] = dict()
    data[y][x] = c

    if gxmin is None or x < gxmin:
        gxmin = x
    if gxmax is None or x > gxmax:
        gxmax = x

    if gymin is None or y < gymin:
        gymin = y
    if gymax is None or y > gymax:
        gymax = y

def canMoveDown(y, x):
    global data, gxmin, gxmax, gymin, gymax

    y = y + 1

    if y < gymin:
        return False
    if y > gymax:
        return False

    if y not in data:
        return True
    if x not in data[y]:
        return True

    return data[y][x] == '.'

def canMoveLeft(y, x):
    global data, gxmin, gxmax, gymin, gymax

    x = x - 1
 
    # Check if a wall was it
    if y in data and x in data[y] and data[y][x] != '.':
        return False

    # Check there is solid ground below
    x = x + 1
    y = y + 1
    if y not in data:
        return False
    if x not in data[y]:
        return False
    return data[y][x] == '#' or data[y][x] == '~'

def canMoveRight(y, x):
    global data, gxmin, gxmax, gymin, gymax

    x = x + 1
 
    # Check if a wall was it
    if y in data and x in data[y] and data[y][x] != '.':
        return False

    # Check there is solid ground below
    x = x - 1
    y = y + 1
    if y not in data:
        return False
    if x not in data[y]:
        return False
    return data[y][x] == '#' or data[y][x] == '~'

def isDataAt(y, x, c):
    if y not in data:
        return False
    if x not in data[y]:
        return False
    return data[y][x] == c

ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    toks = [x.strip() for x in ln.split(',')]
    if toks[0][0] == 'y':
        toks[0],toks[1] = toks[1],toks[0]

    xtoks = toks[0].split('=')[1]
    ytoks = toks[1].split('=')[1]

    if '..' in xtoks:
        toks = xtoks.split('..')
        xmin = int(toks[0])
        xmax = int(toks[1])
    else:
        xmin = int(xtoks)
        xmax = int(xtoks)

    if '..' in ytoks:
        toks = ytoks.split('..')
        ymin = int(toks[0])
        ymax = int(toks[1])
    else:
        ymin = int(ytoks)
        ymax = int(ytoks)

    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            setDataElement(y, x, '#')

    ln = sys.stdin.readline()

iymin = gymin
setDataElement(0, 500, '+')
n = 0

while True:
    y = 0
    x = 500

    moved = True
    goneLeft = False
    goneRight = False
    while moved:
        moved = False

        # Go as far down as it can
        while canMoveDown(y, x):
            # print 'goin down'
            y += 1
            moved = True
            goneLeft = False
            goneRight = False

        while not goneRight and canMoveLeft(y, x):
            # print 'going left'
            x -= 1
            goneLeft = True
            moved = True
            continue

        while not goneLeft and canMoveRight(y, x):
            # print 'going right'
            x += 1
            moved = True
            goneRight = True
            continue

    if y == 0 and x == 500:
        break

    c = '~'
    if (y+1) > gymax or isDataAt(y+1, x, '|') or isDataAt(y, x-1, '|') or isDataAt(y, x+1, '|'):
        c = '|'

    setDataElement(y, x, c)

    if c == '|':
        xl = x - 1
        while xl in data[y] and data[y][xl] == '~':
            data[y][xl] = '|'
            xl = xl - 1

        xr = x + 1
        while xr in data[y] and data[y][xr] == '~':
            data[y][xr] = '|'
            xr = xr + 1
            
    # printData()
    if y >= iymin:
        n += 1

printData()
print n
