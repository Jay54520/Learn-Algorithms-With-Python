# -*- coding: utf-8 -*-
import unittest

from find import Solution

s = Solution()


class TestGenerateTimes(unittest.TestCase):
    """
    涉及的操作有：
    为空
    初始化
    加一
    减一
    删除
    """

    def test_empty(self):
        self.assertEqual({}, s.generate_times([]))

    def test_init(self):
        got = s.generate_times([1])
        want = {1: 1}
        self.assertEqual(want, got)

    def test_plus_one(self):
        got = s.generate_times([1, 1])
        want = {1: 2}
        self.assertEqual(want, got)

    def test_subtract_one(self):
        got = s.generate_times([1, 1, 2])
        want = {1: 1}
        self.assertEqual(want, got)

    def test_delete(self):
        got = s.generate_times([1, 2])
        want = {}
        self.assertEqual(want, got)


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(0, s.MoreThanHalfNum_Solution([]))

    def test_has_number(self):
        numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
        self.assertEqual(2, s.MoreThanHalfNum_Solution(numbers))

    def test_not_has_number(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(0, s.MoreThanHalfNum_Solution(numbers))
