# -*- coding: utf-8 -*-
import unittest
from .get_number_of_k import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty_list(self):
        got = s.GetNumberOfK([], 1)
        want = 0
        self.assertEqual(want, got)

    def test(self):
        got = s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3)
        want = 4
        self.assertEqual(want, got)
