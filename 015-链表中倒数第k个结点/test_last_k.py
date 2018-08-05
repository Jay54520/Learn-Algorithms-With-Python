# -*- coding: utf-8 -*-
import unittest

from last_k import Solution, ListNode

s = Solution()


class Test(unittest.TestCase):

    def test_three_nodes(self):
        first_node = ListNode(1)
        second_node = ListNode(2)
        third_node = ListNode(3)
        first_node.next = second_node
        second_node.next = third_node

        got = s.FindKthToTail(first_node, 2)
        want = second_node
        self.assertEqual(got, want)

    def test_one_node(self):
        first_node = ListNode(1)
        self.assertEqual(s.FindKthToTail(first_node, 1), first_node)