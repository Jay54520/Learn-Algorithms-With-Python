# -*- coding: utf-8 -*-
import unittest

from .min_stack import Solution

s = Solution()


class Test(unittest.TestCase):
    """
    所有类型的情况有：
    * 包含重复元素、多个元素
    """

    def setUp(self):
        self.nodes = [3, 3, 2, 2, 2, 3, 3, 0]

    def test_empty(self):
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.top()
        with self.assertRaises(IndexError):
            s.min()

    def test_push(self):
        self._push()
        self.assertEqual(
            self.nodes,
            s.normal_stack,
        )
        self.assertEqual(
            [3, 3, 2, 2, 2, 2, 2, 0],
            s.min_stack
        )

    def test_pop(self):
        self._push()
        for want in reversed(self.nodes):
            got = s.pop()
            self.assertEqual(want, got)

        with self.assertRaises(IndexError):
            s.pop()

    def test_min(self):
        self._push()
        for want in [0, 2, 2, 2, 2, 2, 3, 3]:
            got = s.min()
            s.pop()
            self.assertEqual(want, got)

        with self.assertRaises(IndexError):
            s.pop()

    def _push(self):
        for node in self.nodes:
            s.push(node)
