# -*- coding: utf-8 -*-
import unittest

from mirror import Solution, TreeNode

s = Solution()


class Test(unittest.TestCase):
    """
    所有类型的情况有：
    * 空
    * 一个节点
    * 多个节点
    """

    def test_empty(self):
        root = None
        got = s.Mirror(root)
        want = root
        self.assertEqual(got, want)

    def test_one_node(self):
        root = TreeNode(1)
        got = s.Mirror(root)
        want = root
        self.assertEqual(got, want)

    def test_not_empty(self):
        """{1234#} 的镜像为 {132###4} ，# 表示空。这个测试用例包含了单个节点与两个节点镜像的情况。"""
        root = TreeNode(1)
        left = TreeNode(2)
        right = TreeNode(3)
        left_left = TreeNode(4)

        root.left = left
        root.right = right
        left.left = left_left

        got = s.Mirror(root)
        self.assertEqual(got.val, 1)
        self.assertEqual(got.left.val, 3)
        self.assertEqual(got.right.val, 2)
        self.assertEqual(got.right.right.val, 4)