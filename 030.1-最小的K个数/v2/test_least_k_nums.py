# -*- coding: utf-8 -*-
import unittest

from least_k_nums import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_multiple_elements(self):
        got = set(s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
        want = {1, 2, 3, 4}
        self.assertEqual(want, got)

    def test_k_equal_length(self):
        got = set(s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 8))
        want = {1, 2, 3, 4, 5, 6, 7, 8}
        self.assertEqual(want, got)

    def test_k_greater_than_length(self):
        got = s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 10)
        want = []
        self.assertEqual(want, got)

    def test_k_equal_0(self):
        got = s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 0)
        want = []
        self.assertEqual(want, got)
