#!/bin/python

b = 93
c = b

b *= 100
b += 100000

c = b
c += 17000

h = 0

def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    else:
        return True


while (b <= c):
    if not is_prime(b):
        h += 1

    """
    f = 1
    d = 2

    while (d != b):
        e = 2

        while (e != b):
                print b
                f = 0
                break

            e += 1

        d += 1
        if f == 0:
            break

    if f == 0:
        print b
        h += 1
    """

    b += 17

print h
