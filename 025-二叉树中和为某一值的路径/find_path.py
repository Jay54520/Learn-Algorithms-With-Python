# -*- coding:utf-8 -*-
from copy import deepcopy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def FindPath(self, root, expectNumber):
        """
        输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
        路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
        (注意: 在返回值的list中，数组长度大的数组靠前)

        10
        | \
        5 12
        |\
        4 7

        有两条路径
        * 10 12
        * 10 5 7

        算法及分析

        过滤出和为指定数的所有路径。由于可能存在负数，所以不能提前终止。

        根据题意，一个树的所有路径为根节点 + 左右子树的所有路径，子树的路径也为子树的根节点 +
        子树左右子树的所有路径（递归）。为了节约空间，我们不想先找到所有路径，然后再过滤，而是一条一条直接过滤。

        所以算法为：
        如果当前节点是叶子节点，
            如果路径符合要求，那么将其加入结果；
            否则，返回
        否则，将当前节点加入当前路径，然后再对它的非空节点调用函数

        由于数组长度大的数组靠前，所以再对 paths 中的元素按照长度个数排倒叙。

        证明：
        对于空节点，符合；
        对于一个节点，符合；
        对于多个节点，由于遍历了所有路径，所以符合。

        复杂度：
        时间复杂度：最大路径数，相当于叶子节点的个数。为 2h + 1，2logn + 1 为 O(logn)。
        然后排序为 O(logn * log(logn))。（h 为二叉树的高度，n 为二叉树的节点数。）
        空间复杂度：O(1)
        """
        paths = []
        if not root:
            return paths

        self.find_path(root, [], expectNumber, paths)
        return sorted(paths, key=len, reverse=True)

    def find_path(self, root, tmp_path, expectNumber, paths):
        tmp_path.append(root.val)
        if (not root.left) and (not root.right):
            if sum(tmp_path) == expectNumber:
                paths.append(tmp_path)
        else:
            length = len(tmp_path)
            if root.left:
                # 使用切片的原因是为了获取当前的 tmp_path，而不是被影响后的 tmp_path
                self.find_path(root.left, tmp_path[:length], expectNumber, paths)
            if root.right:
                self.find_path(root.right, tmp_path[:length], expectNumber, paths)
        return
