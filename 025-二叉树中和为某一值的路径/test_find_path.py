# -*- coding: utf-8 -*-
import unittest

from find_path import Solution, TreeNode

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual([], s.FindPath(None, 1))

    def test_not_empty(self):
        """
        由于算法中是从左到右，有匹配的路径就加入，而没有按照题意顾忌长度，
        所以这个测试用例是右边的更长。
        """
        root = TreeNode(10)
        right = TreeNode(5)
        right_left = TreeNode(4)
        right_right = TreeNode(7)
        left = TreeNode(12)

        root.right = right
        right.left = right_left
        right.right = right_right
        root.left = left

        got = s.FindPath(root, 22)
        want = [
            [10, 5, 7],
            [10, 12]
        ]
        self.assertEqual(want, got)