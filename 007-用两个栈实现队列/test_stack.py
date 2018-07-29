# -*- coding: utf-8 -*-
import unittest

from stack_array import Stack, Solution


class TestStack(unittest.TestCase):

    def setUp(self):
        self.s = Stack()

    def test_is_empty(self):
        self.assertTrue(self.s.is_empty())

    def test_is_not_empty(self):
        # 这里不使用 push，避免造成测试相互依赖
        self.s._list.append(1)
        self.assertFalse(self.s.is_empty())

    def test_push_pop(self):
        elements = [1, 2, 3]

        for e in elements:
            self.s.push(e)
        for e in reversed(elements):
            self.assertEqual(e, self.s.pop())

    def test_pop_empty(self):
        with self.assertRaises(ValueError):
            self.s.pop()


class TestArray(unittest.TestCase):

    def test_push_pop(self):
        elements = range(5)

        array = Solution()

        for e in elements:
            array.push(e)
        for e in elements:
            self.assertEqual(e, array.pop())
