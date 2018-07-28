# -*- coding: utf-8 -*-
import unittest

from find import Solution

s = Solution()


class TestFind(unittest.TestCase):

    def setUp(self):
        self.array = [
            [1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15],
        ]

    def test_found(self):
        target = 7
        got = s.Find(target, self.array)
        self.assertTrue(got)

    def test_not_found(self):
        target = 5
        got = s.Find(target, self.array)
        self.assertFalse(got)

    def test_empty_array(self):
        target = 1
        got = s.Find(target, [[], []])
        self.assertFalse(got)

        target = 1
        got = s.Find(target, [])
        self.assertFalse(got)
