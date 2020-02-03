# -*- coding: utf-8 -*-
import unittest

from re_order_array import Solution
from v2 import Solution as Solution2

ss = [Solution(), Solution2()]


class Test(unittest.TestCase):

    def test_five_elements_array(self):
        for s in ss:
            got = s.reOrderArray([1, 2, 3, 4, 5])
            want = [1, 3, 5, 2, 4]
            self.assertEqual(want, got)

    def test_empty_array(self):
        for s in ss:
            got = s.reOrderArray([])
            want = []
            self.assertEqual(got, want)
