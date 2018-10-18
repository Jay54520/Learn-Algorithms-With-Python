# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self._is_balanced = True

    def IsBalanced_Solution(self, pRoot, depth=0):
        """
        输入一棵二叉树，判断该二叉树是否是平衡二叉树。
        A balanced binary tree is a binary tree structure in which
        the left and right subtrees of every node differ in height by no more than 1.

        The height of a node is the number of edges on the longest path from the node to a leaf.

        Example 1:

        Given the following tree [3,9,20,null,null,15,7]:

            3
           / \
          9  20
            /  \
           15   7
        Return true.

        Example 2:

        Given the following tree [1,2,2,3,3,null,null,4,4]:

               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        Return false.

        算法1：
        遍历树，对节点的左右子树调用 tree_depth，如果两者的 depth 之差不超过 1，那么这两个节点符合平衡二叉树的定义；
        否则，不符合定义。遍历完成后，返回 True。
        复杂度分析：
        时间复杂度：O(n ^ 2)。要遍历 n 个节点，获取深度的复杂度为 n + n - 1 + ... + 1 = n * (1 + n) = O(n^2)
        空间复杂度：O(1)

        算法2：
        算法1在计算深度时重复计算了。我们可以从子树的深度获取当前根节点的深度：root_depth = max(sub_tree_depths) + 1。
        所以我们先遍历左右子树，
            * 如果左右子树不符合要求，那么整棵树都不符合要求；
            * 否则，返回当前根节点的深度
        根节点的深度为 max(sub_tree_depths) + 1
        复杂度分析：
        时间复杂度：O(n)。要遍历 n 个节点，由于根节点的深度等于最大的子节点深度加 1，而之前已经计算过了子树的深度，所以为 O(1)，n 个 O(1) 为 O(n)
        空间复杂度：O(1)
        """
        self._is_balance(pRoot)
        return self._is_balanced

    def _is_balance(self, pRoot):
        """
        返回当前根节点的深度，
        如果不符合要求，将 self._is_balanced 设置为 False，并返回 -1。因为没有必要计算下去了，当不符合要求的时候。
        """
        if pRoot is None:
            return 0
        if not self._is_balanced:
            return -1
        left_depth = self._is_balance(pRoot.left)
        right_depth = self._is_balance(pRoot.right)
        if abs(left_depth - right_depth) > 1:
            self._is_balanced = False
            return -1
        return max(left_depth, right_depth) + 1

