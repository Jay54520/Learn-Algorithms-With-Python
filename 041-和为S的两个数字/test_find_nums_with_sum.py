# -*- coding: utf-8 -*-
import unittest
from .find_nums_with_sum import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        got = s.FindNumbersWithSum([], 1)
        want = []
        self.assertEqual(want, got)

    def test(self):
        array = [1, 2, 3, 4, 7, 11, 12, 15]
        got = s.FindNumbersWithSum(array, 15)
        want = [3, 12]
        self.assertEqual(want, got)