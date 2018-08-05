# -*- coding: utf-8 -*-
import unittest

from re_order_array import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_five_elements_array(self):
        got = s.reOrderArray([1, 2, 3, 4, 5])
        want = [1, 3, 5, 2, 4]
        self.assertEqual(got, want)

    def test_empty_array(self):
        got = s.reOrderArray([])
        want = []
        self.assertEqual(got, want)
