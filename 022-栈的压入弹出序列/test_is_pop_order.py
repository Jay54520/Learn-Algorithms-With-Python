# -*- coding: utf-8 -*-
import unittest

from is_pop_order import Solution

s = Solution()


class Test(unittest.TestCase):

    def setUp(self):
        self.push_v = [1, 2, 3, 4, 5]

    def test_empty(self):
        self.assertTrue(s.IsPopOrder([], []))

    def test_is_pop_order(self):
        pop_v = [4, 3, 5, 2, 1]
        self.assertTrue(s.IsPopOrder(self.push_v, pop_v))

    def test_is_not_pop_order(self):
        pop_v = [4, 3, 5, 1, 2]
        self.assertFalse(s.IsPopOrder(self.push_v, pop_v))