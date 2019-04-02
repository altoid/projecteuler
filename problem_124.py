#!/usr/bin/env python

import util
import pprint
import sys

# https://projecteuler.net/problem=124

# many numbers will have the same radical

# the radicals of the numbers can be gotten
# through a sieving technique

# need a list of the primes from 1 .. 100000

# answer is 21417 ?

def problem_124(bigN, idx):
    if bigN > 100000:
        raise ValueError("%d is too big, use something < 100000" % bigN)
    
    pp = pprint.PrettyPrinter()

    radicals = [1] * (bigN + 1)
    radicals[0] = 0

    #print radicals

    for p in util.primes_to_100000:
        if p > bigN:
            break

        radicals[::p] = [x * p for x in radicals[::p]]

    #print radicals

    # e is pairs that are i, rad(i)
    e = list(enumerate(radicals))

    se = sorted(e, key = lambda x: (x[1], x[0]))
    # pp.pprint(se)

    return se[idx][0]


if __name__ == '__main__':
    print problem_124(100000, 10000)
    
