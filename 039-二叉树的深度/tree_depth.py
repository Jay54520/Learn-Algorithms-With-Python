# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        """
        输入一棵二叉树，求该树的深度。
        从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
        0
        |  \
        0  0
        |
        0
        上面这棵树的路径是 3。二叉树的路径有很多条，怎么求出最长的那条呢？

        算法1：
        树的题目一般都与树的递归定义有关。树的深度 = max(左子树深度, 右子树深度) + 1
        空子树的深度为 0，这个为递归的 base。
        复杂度分析：
        时间复杂度：O(n)，没有分叉的树。
        空间复杂度：O(1)
        """
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1