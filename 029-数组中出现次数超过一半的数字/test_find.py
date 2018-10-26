# -*- coding: utf-8 -*-
import unittest

from .find import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(0, s.MoreThanHalfNum_Solution([]))

    def test_has_number(self):
        numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
        self.assertEqual(2, s.MoreThanHalfNum_Solution(numbers))

    def test_not_has_number(self):
        numbers = [1, 2, 1, 2, 3]
        self.assertEqual(0, s.MoreThanHalfNum_Solution(numbers))
