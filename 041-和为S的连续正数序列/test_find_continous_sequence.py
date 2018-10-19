# -*- coding: utf-8 -*-
import unittest
from .find_continous_sequence import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        got = s.FindContinuousSequence(2)
        want = []
        self.assertEqual(want, got)

    def test(self):
        got = s.FindContinuousSequence(15)
        want = [
            [1, 2, 3, 4, 5],
            [4, 5, 6],
            [7, 8]
        ]
        self.assertEqual(want, got)
