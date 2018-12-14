#!/usr/local/bin/python

import sys

class Cart:
    def __init__(self, facing):
        self.facing  = facing
        self.nextTurn = 'l'

class Node:
    def __init__(self, typ, cart):
        self.typ = typ
        self.cart = cart
        self.handled = False

grid = []
ln = sys.stdin.readline()
while ln:
    ln = ln.rstrip()
    row = []
    for c in ln:
        if c == '<':
            n = Node('-', Cart('l'))
        elif c == '>':
            n = Node('-', Cart('r'))
        elif c == '^':
            n = Node('|', Cart('u'))
        elif c == 'v':
            n = Node('|', Cart('d'))
        else:
            n = Node(c, None)
        row.append(n)
    grid.append(row)
    ln = sys.stdin.readline()

i = 0
while True:
    i += 1
    cartCount = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            n = grid[y][x]
            n.handled = False
            if n.cart is not None:
                cartCount += 1
                lastCartCoord = [x,y]

    if cartCount == 1:
        print lastCartCoord
        sys.exit(0)

    if (i % 1000) == 0:
        print 'Carts Remaining:',cartCount

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            n = grid[y][x]
            if n.cart is None or n.handled:
                continue
            newX = x
            newY = y
            newFacing = n.cart.facing
            newNextTurn = n.cart.nextTurn
            if n.cart.facing == 'l' and n.typ == '-':
                newX -= 1
            elif n.cart.facing == 'l' and n.typ == '\\':
                newY -= 1
                newFacing = 'u'
            elif n.cart.facing == 'l' and n.typ == '/':
                newY += 1
                newFacing = 'd'
            elif n.cart.facing == 'l' and n.typ == '+' and n.cart.nextTurn == 'l':
                newY += 1
                newFacing = 'd'
                newNextTurn = 's'
            elif n.cart.facing == 'l' and n.typ == '+' and n.cart.nextTurn == 's':
                newX -= 1
                newNextTurn = 'r'
            elif n.cart.facing == 'l' and n.typ == '+' and n.cart.nextTurn == 'r':
                newY -= 1
                newFacing = 'u'
                newNextTurn = 'l'
            elif n.cart.facing == 'r' and n.typ == '-':
                newX += 1
            elif n.cart.facing == 'r' and n.typ == '\\':
                newY += 1
                newFacing = 'd'
            elif n.cart.facing == 'r' and n.typ == '/':
                newY -= 1
                newFacing = 'u'
            elif n.cart.facing == 'r' and n.typ == '+' and n.cart.nextTurn == 'l':
                newY -= 1
                newNextTurn = 's'
                newFacing = 'u'
            elif n.cart.facing == 'r' and n.typ == '+' and n.cart.nextTurn == 's':
                newX += 1
                newNextTurn = 'r'
            elif n.cart.facing == 'r' and n.typ == '+' and n.cart.nextTurn == 'r':
                newY += 1
                newNextTurn = 'l'
                newFacing = 'd'
            elif n.cart.facing == 'd' and n.typ == '|':
                newY += 1
            elif n.cart.facing == 'd' and n.typ == '/':
                newX -= 1
                newFacing = 'l'
            elif n.cart.facing == 'd' and n.typ == '\\':
                newX += 1
                newFacing = 'r'
            elif n.cart.facing == 'd' and n.typ == '+' and n.cart.nextTurn == 'l':
                newX += 1
                newNextTurn = 's'
                newFacing = 'r'
            elif n.cart.facing == 'd' and n.typ == '+' and n.cart.nextTurn == 'r':
                newX -= 1
                newNextTurn = 'l'
                newFacing = 'l'
            elif n.cart.facing == 'd' and n.typ == '+' and n.cart.nextTurn == 's':
                newY += 1
                newNextTurn = 'r'
            elif n.cart.facing == 'u' and n.typ == '|':
                newY -= 1
            elif n.cart.facing == 'u' and n.typ == '\\':
                newX -= 1
                newFacing = 'l'
            elif n.cart.facing == 'u' and n.typ == '/':
                newX += 1
                newFacing = 'r'
            elif n.cart.facing == 'u' and n.typ == '+' and n.cart.nextTurn == 'l':
                newX -= 1
                newFacing = 'l'
                newNextTurn = 's'
            elif n.cart.facing == 'u' and n.typ == '+' and n.cart.nextTurn == 's':
                newY -= 1
                newNextTurn = 'r'
            elif n.cart.facing == 'u' and n.typ == '+' and n.cart.nextTurn == 'r':
                newX += 1
                newFacing = 'r'
                newNextTurn = 'l'
            else:
                print 'unsppported...cart facing',n.cart.facing,' and type ',n.typ,' and next turn ',n.cart.nextTurn
                sys.exit(1)

            if grid[newY][newX].cart is not None:
                print 'collision at ',newX,',',newY
                grid[newY][newX].cart = None
            else:
                grid[newY][newX].cart = Cart(newFacing)
                grid[newY][newX].cart.nextTurn = newNextTurn
                grid[newY][newX].handled = True
            grid[y][x].cart = None
