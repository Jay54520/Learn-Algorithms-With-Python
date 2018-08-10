# -*- coding: utf-8 -*-
import unittest

from matrix import Solution

s = Solution()


class Test(unittest.TestCase):
    """
    所有类型的情况有：
    * 空
    * 一行矩阵
    * 多行矩阵
    """

    def test_empty(self):
        matrix = []
        got = s.printMatrix(matrix)
        want = []
        self.assertEqual(got, want)

    def test_one_row(self):
        matrix = [[1, 2, 3]]
        got = s.printMatrix(matrix)
        want = [1, 2, 3]
        self.assertEqual(got, want)

    def test_multiple_rows(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        got = s.printMatrix(matrix)
        want = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(got, want)
