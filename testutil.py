#!/usr/bin/env python

import unittest
import util

class TestUtil(unittest.TestCase):

    def testSieve(self):
        allnums, primes = util.sieve(50000000)
#        print allnums
#        print primes

    def testEdge(self):
        allnums, primes = util.sieve(1)
        self.assertEqual([], primes)

        allnums, primes = util.sieve(2)
        self.assertEqual([2], primes)

        allnums, primes = util.sieve(3)
        self.assertEqual([2, 3], primes)

        allnums, primes = util.sieve(4)
        self.assertEqual([2, 3], primes)

    def testCorrectness(self):
        top = 20
        allnums, primes = util.sieve(top)

        print primes

if __name__ == '__main__':
    unittest.main()
