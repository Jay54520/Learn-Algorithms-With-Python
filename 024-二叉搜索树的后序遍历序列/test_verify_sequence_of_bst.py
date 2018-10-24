# -*- coding: utf-8 -*-
import unittest

from .verify_sequence_of_bst import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(False, s.VerifySquenceOfBST([]))

    def test_one_Falsede(self):
        self.assertEqual(True, s.VerifySquenceOfBST([1]))

    def test_is_sequence(self):
        """
        8
        | \
        3  10
         \  |
         6 14

        由于是递归的遍历，所以这个测试用例包含了：

        * 有左右子树
        * 只有右子树
        * 只有左子树

        的情况
        """
        self.assertEqual(True, s.VerifySquenceOfBST([1, 6, 3, 14, 10, 8]))
        self.assertEqual(True, s.VerifySquenceOfBST([5, 4, 3, 2, 1]))

    def test_is_Falset_sequence(self):
        self.assertEqual(False, s.VerifySquenceOfBST([7, 4, 6, 5]))
