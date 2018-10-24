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

        v1 中的空间复杂度是 O(n)，由于空间复杂度是最差情况下除了结果外占用的复杂度，
        所以如果采用相同的数据结构——链表储存旧节点 random 到新节点 random 的关系，
        就可以减少空间复杂度。

        按照上面的思路，将新节点插入到旧节点后面，比如：

        old_n1 -> new_n1 -> old_n2 -> new_n2 -> old_n3 -> new_n3

        则新旧节点的关系为：

        1. new_n = old_n.next
        2. 根据上面可以推断出：
            如果 new_n.random 不为 None: new_n.random = old_n.random.next。假设
            old_n.random = old_random，则 old_random.next = new_random。
            否则，当 new_n.random 为 None 时，old_n.random 也为 None

        根据第 2 点设置好新链表的 random，然后拆分得到完整的新链表：

        设置 random：

            * 新链表的头是第二个节点
            * new_n.next 是当前链表的 next.next
            * 终止条件是 old_cur 为 None

        拆分：
            拆分出新、旧链表。拆分出旧链表的原因是尽量不要改变函数的输入，并且
            牛客网的测试用例会根据输入来判断新链表是否引用了原链表。

            将新链表的 next 改为指向新链表的节点而不是现在的旧链表的节点。
            终止条件是 new_n.next = None

        复杂度分析：
        时间复杂度：O(n)
        空间复杂度：O(1)

        总结

        * 通过与结果相同的数据结构来储存关系从而避免了空间的占用
        * 牛客网的判例有问题，返回的结果正确的情况下，因为输入被改变了，就判定错误，
        而我认为改变输入只是算编码规范问题而不算正确性问题。
        """
        if not pHead:
            return None

        # ------------插入新节点------------
        old_cur = pHead  # type: RandomListNode
        while old_cur:
            new_node = RandomListNode(old_cur.label)
            next = old_cur.next
            old_cur.next = new_node
            new_node.next = next
            old_cur = next
        # ------------插入新节点------------

        # ------------设置新链表的 random------------        
        old_cur = pHead  # type: RandomListNode
        while old_cur:
            new_node = old_cur.next
            old_random = old_cur.random
            if old_random:
                new_random = old_random.next
            else:
                new_random = None
            new_node.random = new_random
            old_cur = new_node.next
        # ------------设置新链表的 random------------

        # ------------拆分得到新链表------------
        new_head = pHead.next

        old_cur = pHead
        new_cur = new_head
        while new_cur.next:
            old_cur.next = new_cur.next
            new_cur.next = new_cur.next.next

            old_cur = old_cur.next
            new_cur = new_cur.next

        # 将旧链表的最后一个由 new_cur 变为 None，至此旧链表（输入）完全恢复
        old_cur.next = None
        # ------------拆分得到新链表------------

        return new_head