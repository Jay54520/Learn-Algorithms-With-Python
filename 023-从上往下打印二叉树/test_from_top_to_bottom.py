# -*- coding: utf-8 -*-
import unittest

from from_top_to_bottom import Solution, TreeNode

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(s.PrintFromTopToBottom(None), [])

    def test_not_empty(self):
        root = TreeNode(1)
        left = TreeNode(2)
        right = TreeNode(3)
        left_left = TreeNode(4)
        right_right = TreeNode(5)

        root.left = left
        root.right = right
        left.left = left_left
        right.right = right_right

        self.assertEqual(
            s.PrintFromTopToBottom(root),
            [1, 2, 3, 4, 5]
        )
