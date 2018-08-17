# -*- coding: utf-8 -*-
import unittest

from verify_sequence_of_bst import Solution, YES, NO

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(NO, s.VerifySquenceOfBST([]))

    def test_one_node(self):
        self.assertEqual(YES, s.VerifySquenceOfBST([1]))

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
        self.assertEqual(YES, s.VerifySquenceOfBST([1, 6, 3, 14, 10, 8]))
        self.assertEqual(YES, s.VerifySquenceOfBST([5, 4, 3, 2, 1]))

    def test_is_not_sequence(self):
        self.assertEqual(NO, s.VerifySquenceOfBST([7, 4, 6, 5]))
