# -*- coding: utf-8 -*-
import copy
import unittest

from has_subtree import Solution, TreeNode

s = Solution()


class Test(unittest.TestCase):

    """
    所有类型的情况有：
    * 两个树都为空
    * 一个为空，另一个不为空
    * 两个都不为空
    """

    def test_two_empty(self):
        got = s.HasSubtree(None, None)
        want = False
        self.assertEqual(got, want)

    def test_half_empty(self):
        first_node = TreeNode(1)

        got = s.HasSubtree(first_node, None)
        want = False
        self.assertEqual(got, want)
        
    def test_not_empty(self):
        """{12} 是 {12#3} 的子树，# 表示空。这个测试用例包含了普通树以及父树的尾部比子树还多一个节点的特殊情况。"""
        root1 = TreeNode(1)
        left1 = TreeNode(2)
        left1_left = TreeNode(3)
        root1.left = left1
        left1.left = left1_left

        root2 = TreeNode(1)
        left2 = TreeNode(2)
        root2.left = left2

        got = s.HasSubtree(root1, root2)
        want = True
        self.assertTrue(got, want)