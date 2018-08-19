# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Convert(self, pRootOfTree):
        """
        输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
        要求不能创建任何新的结点，只能调整树中结点指针的指向。

            10
            |   \
            6   14
            | \  |  \
            4 8  12 16

            4 <-> 6 <-> 8 <-> 10 <-> 12 <-> 14 <-> 16

            顺序就是二叉搜索树的中序遍历顺序，然后将它们串起来变成双向链表。

        算法：

        * 空，返回空
        * 非空，如上所述

        证明

        二叉搜索树的中序遍历结果就是从小到大。

        对于空树或者只有一个节点，显然符合；
        对于多个节点，根据树的结构，只需要证明

        1. 左子树的中序遍历是有序的、
        2. 右子树的中序遍历是有序的
        3. 根节点在它们之间

        根据二叉搜索树的定义，根节点大于左子树，小于右子树，所以 3 成立。

        一直按上面的方式递归左子树，最后一定能得到这样的树：

        root
        |          \
        left_leaf  right_leaf

        左右节点可能为空。这时，这棵树的中序遍历满足从小到大的顺序。然后
        递归往上，左子树的中序遍历满足从小到大的顺序。右子树同理，证明完成。

        复杂度分析

        时间复杂度：遍历 O(n)、生成链表 O(n)，所以为 O(n)
        空间复杂度：O(n)，用于储存遍历结果

        总结

        * 看到问题，觉得很复杂，束手无策。这意味着你没有想到合适的解法，因为算法题的思路
        都不会很复杂。
        * 看不懂“只能调整树中结点指针的指向”，以及对 Python 的变量传递机制不够清楚。
        一开始认为只能通过 left 或 right 操作，没有想到可以将 left = node.left
        也只是引用操作
        * 不知道二叉搜索树的中序遍历结果就是从小到大（维基百科上也没写）
        """
        if not pRootOfTree:
            return None

        middle_traverse_results = self.middle_traverse(pRootOfTree)

        for index, node in enumerate(middle_traverse_results):
            if index == len(middle_traverse_results) - 1:
                break

            cur_node = node
            next_node = middle_traverse_results[index + 1]
            if index == 0:
                pRootOfTree = cur_node
                cur_node.left = None

            cur_node.right = next_node
            next_node.left = cur_node
        return pRootOfTree

    def middle_traverse(self, pRootOfTree):
        """返回中序遍历的节点列表，pRootOfTree 不会为空"""
        results = []
        self._middle_traverse(pRootOfTree.left, results)
        results.append(pRootOfTree)
        self._middle_traverse(pRootOfTree.right, results)
        return results

    def _middle_traverse(self, pRootOfTree, results):
        if not pRootOfTree:
            return

        self._middle_traverse(pRootOfTree.left, results)
        results.append(pRootOfTree)
        self._middle_traverse(pRootOfTree.right, results)
