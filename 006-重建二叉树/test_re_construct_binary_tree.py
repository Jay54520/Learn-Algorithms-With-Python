# -*- coding: utf-8 -*-
import unittest

from re_construct_binary_tree import Solution, TreeNode

s = Solution()


class TestLinkedListFromTailToHead(unittest.TestCase):

    def test_success(self):
        pre = [1, 2, 4, 7, 3, 5, 6, 8]
        tin = [4, 7, 2, 1, 5, 3, 8, 6]
        got = s.reConstructBinaryTree(pre, tin)

        want = TreeNode(1)

        # pre = [2, 4, 7]
        # tin = [4, 7, 2]
        left = TreeNode(2)
        # pre = [4, 7]
        # tin = [4, 7]
        left_left = TreeNode(4)
        left_left_right = TreeNode(7)

        want.left = left
        left.left = left_left
        left_left.right = left_left_right

        # pre = [3, 5, 6, 8]
        # tin = [5, 3, 8, 6]
        right = TreeNode(3)
        right_left = TreeNode(5)
        # pre = [6, 8]
        # tin = [8, 6]
        right_right = TreeNode(6)
        right_right_left = TreeNode(8)

        want.right = right
        right.left = right_left
        right.right = right_right
        right_right.left = right_right_left

        self.assert_tree_equal(got, want)

    def assert_tree_equal(self, got, want):
        """
        断言两棵树相同
        从树的定义知道，树为 [L, S, R]，所以两课树相等，则它们的根节点的值相同并且左右子树也是相同的数。
        终止条件是两个节点为空。

        参考 https://codereview.stackexchange.com/a/159148
        """
        if (not got) and (not want):
            return

        if got and want:
            if got.val != want.val:
                raise AssertionError
            self.assert_tree_equal(got.left, want.left)
            self.assert_tree_equal(got.right, want.right)
            return

        raise AssertionError
