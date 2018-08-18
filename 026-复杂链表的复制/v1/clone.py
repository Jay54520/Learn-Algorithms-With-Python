# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    def Clone(self, pHead):
        """
        输入一个复杂链表（每个节点中有节点值，以及两个指针，
        一个指向下一个节点，另一个特殊指针指向任意一个节点），
        返回结果为复制后复杂链表的head。
        （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

        node1 -> node2 -> node3

        node1.random = node3
        node2.random = node1
        node3.random = node2

        算法：

        遍历原链表，复制值和 next，然后考虑复制 random。

        * 复制链表的所有都与原链表相同，当然也包括 random 节点
        * random 也是链表中的一个节点
        * 通过原链表的节点能知道它的 random 节点

        在复制的时候建立一个原链表到新链表节点的字典。则原链表的 random 节点对应
        新链表的 random 节点。

        证明：
        为空，返回 []
        非空，由于是遍历，所以不会有遗漏，证明通过。

        复杂度分析：
        时间复杂度：O(n)，遍历一次复制值和 next —— O(n)，然后再遍历一次创建 random —— O(n)，
        所以为 O(n)。
        空间复杂度：O(n)，字典中含有所有的 n 个节点

        没有通过牛客网的测试用例，提示返回为 None，但在自己的测试用例中检查过了没有引用。
        """
        if not pHead:
            return pHead

        new_head = RandomListNode(pHead.label)
        origin_current = pHead.next
        new_current = new_head
        origin_to_new = {pHead: new_head}

        # origin_current 对应 new_current.next
        while origin_current is not None:
            new_next_node = RandomListNode(origin_current.label)
            origin_to_new[origin_current] = new_next_node
            new_current.next = new_next_node
            new_current = new_next_node
            origin_current = origin_current.next

        origin_current = pHead
        while origin_current is not None:
            new_current = origin_to_new[origin_current]
            new_random = origin_to_new[origin_current.random]
            new_current.random = new_random
            origin_current = origin_current.next
        return new_head