# -*- coding: utf-8 -*-
import unittest
from .find_nums_appear_once import Solution

s = Solution()

class Test(unittest.TestCase):

    def test_empty_array(self):
        got = s.FindNumsAppearOnce([])
        want = []
        self.assertEqual(want, got)

    def test(self):
        array = [2, 6, 3, 4, 3, 2, 5, 5]
        got = s.FindNumsAppearOnce(array)
        want = [6, 4]
        self.assertEqual(want, got)

    def test_reverse(self):
        array = [2, 4, 3, 6, 3, 2, 5, 5]
        got = s.FindNumsAppearOnce(array)
        want = [4, 6]
        self.assertEqual(want, got)
