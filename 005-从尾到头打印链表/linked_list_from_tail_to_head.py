# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:

    def printListFromTailToHead(self, listNode):
        """
        返回从尾部到头部的列表值序列，例如[1,2,3]

        算法实现与证明

            根据定义，链表的尾部的 next 为 None，定义来自 https://zh.wikipedia.org/wiki/%E9%93%BE%E8%A1%A8#%E5%8D%95%E5%90%91%E9%93%BE%E8%A1%A8

            所以如果当前节点不为空，将当前节点的值放入一个列表，当前节点指向当前节点的下一个节点；
            如果当前节点为空，说明遍历完了整个链表，然后返回逆序的列表。

            特殊情况是链表为空，被“当前节点为空”包含了，所以不用额外做处理。

        :param listNode: ListNode 实例
        :return: list
        """
        raw_list = []

        current_node = listNode
        while current_node is not None:
            raw_list.append(current_node.val)
            current_node = current_node.next

        result = list(reversed(raw_list))
        return result
