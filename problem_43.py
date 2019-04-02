#!/usr/bin/env python

import itertools
import sys

# - the 4th digit must be even - if it is 0 then 6th must be 5
# - the 6th digit has to be either 5 or 0

# generate these sets:
# -  * * * [2468] * [05] * * * *
# -  * * * 0 * 5 * * * *

# - so instead of 10! numbers, we generate
#   4 . 2 . 8 . 7 . 6 . 5 . 4 . 3 . 2 . 1 + 8!
#  = 8! (8 + 1) = 9! = 362880.  not too bad

# takes 8s without the optimization
# takes 1.8s with the optimization

primes = [2, 3, 5, 7, 11, 13, 17]

def is_subdivisible(s):
    global primes
    substr_size = 3
    l = len(s)
    i = 0
    while i < l - substr_size:
        k = i + 1
        n = int(s[k:k+3])
        if n % primes[i] != 0:
            return False
        i += 1
    return True

tally = 0

evens = ['2', '4', '6', '8']
zfive = ['0', '5']
digits = '0123456789'

for e in evens:
    for z in zfive:
        l = list(digits)
        l.remove(e)
        l.remove(z)

        for p in itertools.permutations(l):
            x = list(p)
            x.insert(3, e)
            x.insert(5, z)
            nstr = ''.join(x)
            if is_subdivisible(nstr):
                print x
                tally += int(nstr)


p1 = '12346789'
for p in itertools.permutations(p1):
    x = list(p)
    x.insert(3, '0')
    x.insert(5, '5')
    nstr = ''.join(x)
    if is_subdivisible(nstr):
        print x
        tally += int(nstr)

print tally
