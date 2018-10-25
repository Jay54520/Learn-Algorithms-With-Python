# -*- coding: utf-8 -*-
import unittest

from .convert import Solution, TreeNode

s = Solution()

root = TreeNode(10)
left = TreeNode(6)
right = TreeNode(14)
left_right = TreeNode(8)
right_left = TreeNode(12)

root.left = left
root.right = right
left.right = left_right
right.left = right_left


class TestConvert(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(None, s.Convert(None))

    def test_not_empty(self):
        new_root = s.Convert(root)
        want_traverse = [6, 8, 10, 12, 14, 12, 10, 8, 6]
        self.assertEqual(want_traverse, self.traverse_double_linked_list(new_root))

    def traverse_double_linked_list(self, double_linked_list):
        """先遍历 right，然后遍历 left，忽略 None"""
        results = []
        cur_node = double_linked_list

        while cur_node.right:
            results.append(cur_node.val)
            cur_node = cur_node.right

        while cur_node:
            results.append(cur_node.val)
            cur_node = cur_node.left

        return results