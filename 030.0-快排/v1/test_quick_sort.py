# -*- coding: utf-8 -*-
import unittest
from .quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        got = quick_sort([])
        want = []
        self.assertEqual(want, got)

    def test_one_element_list(self):
        got = quick_sort([1])
        want = [1]
        self.assertEqual(want, got)

    def test_multiple_elements(self):
        got = quick_sort([15, 3, 7, 0, 18, 2, 16, 13, 19, 9, 6, 1, 12, 14, 5, 4, 10, 11, 17, 8])
        want = list(range(20))
        self.assertEqual(want, got)

