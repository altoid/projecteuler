#!/usr/bin/env python

from __future__ import division
import math

# longest short leg for a given perimiter
# is the leg of an isoceles right triangle
# with that perimiter

ISOC_FACTOR = (1 + 1 + math.sqrt(2))

def starting_leg(p):
    return int(math.floor(p / ISOC_FACTOR))

def other_sides(l, p):
    """
    given short leg and perimeter, get the other leg and the h of a right
    triangle with that leg.

    returns a tuple of (l, r, h) where h is hypotenuse
    """

    h_plus_r = p - l
    h_minus_r = (l ** 2) / h_plus_r
    h = (h_plus_r + h_minus_r) / 2
    r = h_plus_r - h
    return l, r, h

def all_ints(triple):
    l, r, h = triple
    return (l == int(math.floor(l)) and
            r == int(math.floor(r)) and
            h == int(math.floor(h)))

# starting from the longest short leg, iterate down until
# short leg is 1

def get_tuples(p):
    l = starting_leg(p)
    return filter(all_ints, 
                  [other_sides(i, p) for i in xrange(1, l + 1)])

def find_max_p():
    x = [get_tuples(s) for s in xrange(1001)]
    result = max(enumerate(x), key=lambda r: len(r[1]))
    return result[0]

print find_max_p()



