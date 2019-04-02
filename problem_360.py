#!/usr/bin/env python

import math

def coords(r):
    """
    for a circle at the origin with radius r (an integer),
    give me all of the points on the circle with integer coordinates.
    """

    # start from x = 0 to x = r, first quadrant for now
    for x in xrange(r + 1):
        y = math.sqrt(r ** 2 - x ** 2)
        iy = int(y)
        if y == iy:
            print "(%d, %d) - %d" % (x, iy, int(math.sqrt(x ** 2 + iy ** 2)))
#            if x != 0 and iy != 0:
#                print "(%d, %d)" % (x, iy)
#                print "(%d, %d)" % (-x, iy)
#                print "(%d, %d)" % (x, -iy)
#                print "(%d, %d)" % (-x, -iy)
#            elif x != 0:
#                print "(%d, %d)" % (x, iy)
#                print "(%d, %d)" % (-x, iy)
#            else:
#                print "(%d, %d)" % (x, iy)
#                print "(%d, %d)" % (x, -iy)

def coords_sphere(r):
    """
    same thing, but for a sphere.
    """

    # for each 0 <= x <= r
    #     for each y that lies within the circle projected onto the xy plane
    #         find z...

    result = set()

    r2 = r ** 2
    for x in xrange(r + 1):
        x2 = x ** 2
        ybound = math.sqrt(r2 - x2)
        y = 0
        while y <= ybound:
            fz = math.sqrt(r2 - (x2 + y ** 2))
            z = int(fz)
            if z == fz:
#                print x, y, z
                result.add((x, y, z))
                result.add((x, y, -z))
                result.add((x, -y, z))
                result.add((x, -y, -z))
                result.add((-x, y, z))
                result.add((-x, y, -z))
                result.add((-x, -y, z))
                result.add((-x, -y, -z))
            y += 1

    total = 0
    for r in result:
        total += (abs(r[0]) + abs(r[1]) + abs(r[2]))

    return total

def take2(r):
    # for each 0 <= x <= r
    #     if x <= r/sqrt(2)
    #     

    result = set()

    r2 = r ** 2
    for x in xrange(r + 1):
        x2 = x ** 2
        if x <= r / math.sqrt(2):
            ybound = x
        else:
            ybound = math.sqrt(r2 - x2)

        y = 0
        while y <= ybound:
            y2 = y ** 2
            fz = math.sqrt(r2 - (x2 + y2))
            z = int(fz)
            if z == fz:
                print x, y, z, int(math.sqrt(x2 + y2 + z ** 2))
                result.add((x, y, z))
                result.add((x, y, -z))
                result.add((x, -y, z))
                result.add((x, -y, -z))
                result.add((-x, y, z))
                result.add((-x, y, -z))
                result.add((-x, -y, z))
                result.add((-x, -y, -z))

                # now add points that are symmetric across y = x
                result.add((y, x, z))
                result.add((y, x, -z))
                result.add((y, -x, z))
                result.add((y, -x, -z))
                result.add((-y, x, z))
                result.add((-y, x, -z))
                result.add((-y, -x, z))
                result.add((-y, -x, -z))
            y += 1
                

    total = 0
    for r in result:
        total += (abs(r[0]) + abs(r[1]) + abs(r[2]))

    return total

def test(r):
    print "take2:", take2(r)
#    print "coords_sphere:", coords_sphere(r)

if __name__ == '__main__':
    test(45)
#    test(10 ** 6)
