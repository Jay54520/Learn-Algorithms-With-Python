# -*- coding: utf-8 -*-
import unittest

from clone import Solution, RandomListNode

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(None, None)

    def test_not_empty(self):
        node1 = RandomListNode(1)
        node2 = RandomListNode(3)
        node3 = RandomListNode(3)

        node1.next = node2
        node2.next = node3
        node1.random = node3
        node2.random = node1
        node3.random = node1

        got = s.Clone(node1)  # type: RandomListNode
        self.check_reference(got, node1)
        self.assertEqual(node1.label, got.label)
        self.assertEqual(node2.label, got.next.label)
        self.assertEqual(node3.label, got.next.next.label)

        self.assertEqual(node1.random.label, got.random.label)
        self.assertEqual(node2.random.label, got.next.random.label)
        self.assertEqual(node3.random.label, got.next.next.random.label)

    def check_reference(self, got, original):
        """got 链表中不能引用 original 中的任何节点"""
        while got is not None:
            if got is original:
                raise AssertionError('{} 与 {} 相同'.format(got, original))
            if got.random is original.random:
                raise AssertionError('{} 与 {} 相同'.format(got.random, original.random))
            got = got.next
            original = original.next
