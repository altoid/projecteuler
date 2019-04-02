#!/usr/bin/env python

import math
import re
import util

def rotations(sn):
    """
    sn is a string representation of a number.
    """

    l = list(sn)
    ndigits = len(l)

    i = 0
    while i < ndigits:
        l = l[1:] + l[:1]
        k = int(''.join(l))
        yield k
        i += 1


if __name__ == '__main__':

    top = 1000000

    allnums, primes = util.sieve(top)

    total = 3 # counting 2, 3, 5

    regex = re.compile(r'[245680]')

    for p in primes[3:]:

        circular = True
        sp = str(p)
        if regex.search(sp) is not None:
            continue

        print "prime", p
        for r in rotations(sp):
            print "    checking", r
            if allnums[r] == 0:
            if r not in primes:
                circular = False
                break

        if circular:
            total += 1

    print "total:  %d" % total

# optimizations:
# 1.  with the exception of 2 itself, no number that has the digits [245680] will qualify.
# 2.  once we check a number, we don't have to check its rotations too.

# runtime without optimizations:  1s
# with optimization 1:  0.81s
# with optimization 2:  takes longer
