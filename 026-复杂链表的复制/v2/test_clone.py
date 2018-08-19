# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from clone import Solution, RandomListNode

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(None, None)

    def test_not_empty(self):
        """[1,2,3,4,5, 3,5,#,2,#]"""
        node1 = RandomListNode(1)
        node2 = RandomListNode(2)
        node3 = RandomListNode(3)
        node4 = RandomListNode(4)
        node5 = RandomListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node1.random = node3
        node2.random = node5
        node4.random = node2

        self.assertEqual([1, 2, 3, 4, 5, 3, 5, '#', 2, '#'], self.string(node1))

        clone = s.Clone(node1)  # type: RandomListNode
        self.assertEqual([1, 2, 3, 4, 5, 3, 5, '#', 2, '#'], self.string(clone))
        self.check_reference(clone, node1)

    def check_reference(self, clone, original):
        """got 链表中不能引用 original 中的任何节点"""
        while clone is not None:
            if clone is original:
                raise AssertionError('{} 与 {} 相同'.format(clone, original))
            if clone.random is not None:
                if clone.random is original.random:
                    raise AssertionError('{} 与 {} 相同'.format(clone.random, original.random))
            clone = clone.next
            original = original.next

    def string(self, node):
        """
        按顺序返回节点和节点对应的 random 节点，
        对于 random 非空节点，返回 label，对于空节点，返回 #
        """
        results = []
        cur = node  # type: RandomListNode
        while cur:
            results.append(cur.label)
            cur = cur.next

        cur = node
        while cur:
            if cur.random:
                results.append(cur.random.label)
            else:
                results.append('#')
            cur = cur.next
        return results
