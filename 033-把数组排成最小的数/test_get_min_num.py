# -*- coding: utf-8 -*-
import unittest
from .get_min_num import Solution

s = Solution()


class Test(unittest.TestCase):

    def test(self):
        numbers = [3, 32, 321]
        got = s.PrintMinNumber(numbers)
        want = 321323
        self.assertEqual(want, got)

    def test_empty_list(self):
        numbers = []
        got = s.PrintMinNumber(numbers)
        want = ''
        self.assertEqual(want, got)
