# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def Merge(self, pHead1, pHead2):
        """
        输入两个单调递增的链表，输出两个链表合成后的链表，要求合成的链表满足单调不减。

        比如 [1, 3, 5, 7] 与 [2, 4, 6, 8]，合并后为 [1, 2, 3, 4, 5, 6, 7, 8]

        算法1：

        将两个链表转换为数组，然后合并、排序，然后再将数组转换为链表。由于转换包含了所有节点（情况），所以证明通过。

        复杂度分析：

        n 指两个链表的节点数之和。
        时间复杂度：O(nlogn)
        空间复杂度：O(n)。所有的元素都要储存到数组中。

        这里的思考局限是将两个单调递增的列表看做了整体，而没有拆分成一个一个元素看待。

        算法2：

        比较两个链表的当前节点，然后选择更小的节点添加到新的链表中，然后移动到更小节点的下一个节点。终止条件是：两个链表的当前节点都为空。
        比较算法：一个节点为空，另一个不为空：返回不为空的节点；两个节点都不为空：返回更小的节点；如果都相等或者都为空，返回第二条链的节点；
        由于是遍历，所以涉及了所有情况，所以证明通过。

        复杂度分析：

        时间复杂度：O(n)。只需要遍历完两个链表即可。
        空间复杂度：O(1)。没有占用额外的空间。

        参考：原书。书中的图很形象。

        :param pHead1: ListNode
        :param pHead2: ListNode
        :return: ListNode
        """
        merged = None
        merged_current = merged
        current1 = pHead1
        current2 = pHead2

        while current1 or current2:
            if self.less(current1, current2):
                less = current1
                current1 = current1.next
            else:
                less = current2
                current2 = current2.next

            if not merged_current:
                merged_current = less
                merged = less
            else:
                merged_current.next = less
                merged_current = merged_current.next
        return merged

    def less(self, node1, node2):
        """
        node1 是否小于 node2。
        如果两个节点都为空，返回 True；
        如果一个节点为空，那么不为空的节点更小；
        如果两个节点都不为空，比较节点的 val
        :param node1:
        :param node2:
        :return:
        """
        if not node1 and not node2:
            return True
        if node1 and not node2:
            return True
        if node2 and not node1:
            return False

        if node1.val < node2.val:
            return True
        else:
            return False