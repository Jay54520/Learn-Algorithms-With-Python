# -*- coding: utf-8 -*-
import unittest
from .merge_sort import merge_sort

cmp = lambda x, y: True if x < y else False


class Test(unittest.TestCase):

    def test_empty_list(self):
        got = merge_sort([], cmp)
        want = []
        self.assertEqual(want, got)

    def test(self):
        a_list = [9, 7, 8, 3, 2, 1]
        got = merge_sort(a_list, cmp)
        want = [1, 2, 3, 7, 8, 9]
        self.assertEqual(want, got)
