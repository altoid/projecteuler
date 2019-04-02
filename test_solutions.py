#!/usr/bin/env python

import unittest
import util

import problem_124

class TestSolutions(unittest.TestCase):

    def test_124(self):
        # NFI if this is the right answer
        self.assertEqual(21417, problem_124.problem_124(100000, 10000))

if __name__ == '__main__':
    unittest.main()
