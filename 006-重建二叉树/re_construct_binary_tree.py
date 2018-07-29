# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def reConstructBinaryTree(self, pre, tin):
        """
        输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

        算法及证明

            二叉树是一种每个节点最多只含有两个孩子的树形结构。递归的定义是：一个非空的二叉树是一个 tuple (L, S, R)，
            L 和 R 是二叉树或空集合，S 是一个只含有一个元素的集合。—— https://en.wikipedia.org/wiki/Binary_tree

            前序遍历、中序遍历中的前、中都是指根节点相对左右子树的遍历顺序，所以：

            前序遍历：[root_value, left_sub_tree, right_sub_tree]，这里的左右子树，同样是以前序遍历。

            中序遍历： [left_sub_tree, root_value, right_sub_tree]，这里的左右子树以中序遍历。

            从上面我们可以知根节点的值以及它的左右子树的前序、中序遍历。
                由于不含有重复的结果以及中序遍历的特性，所以中序遍历以 root_value 作为左右子树的分界线，
                据此能得到左右子树的中序遍历；
                根据左子树的中序遍历，能得到左子树的节点数目，将其代入前序遍历中，就能得到左右子树在前序遍历
                中的分界点，从而得到左右子树的前序遍历。


            根据左子树的前序、中序遍历，调用本方法得到左子树；同样，得到右子树，那么这个树就为 (左子树, 根节点, 右子树)

            终止条件是当前节点是一棵树——只有一个节点或者为空。如果只有一个节点，那么左右子树都是空的，可以被为空的条件处理，
            所以终止条件只需要是节点为空即可。

        复杂度分析

        时间复杂度：算法的每次操作是获取当前层的根节点。所以最大操作数为树的深度的两倍（因为有左右子树）。
        令节点数为 n，那么最大深度为 logn。所以时间复杂度为 O(2 * logn) 为 O(logn)。

        空间复杂度：没有占用额外空间，所以为 O(1)。

        :param pre: list 类型，前序遍历结果
        :param tin: list 类型，中序遍历结果
        :return: 构造的树的根节点
        """
        if not pre:
            return None

        root_value = pre[0]
        root_value_index = tin.index(root_value)
        left_sub_tree_tin = tin[:root_value_index]
        right_sub_tree_tin = tin[root_value_index+1:]
        left_sub_tree_num = len(left_sub_tree_tin)
        # 切片是左闭右开，所以开始索引是左子树的第一个节点的索引，结束节点是左子树的最后一个节点的下一个节点。
        # 1 表示根节点后面的位置；1 + left_sub_tree_num 表示左子树后面的那个位置
        left_sub_tree_pre = pre[1:1+left_sub_tree_num]
        # 左子树后面的那个位置就是右子树的第一个节点
        right_sub_tree_pre = pre[1+left_sub_tree_num:]

        left_sub_tree = self.reConstructBinaryTree(left_sub_tree_pre, left_sub_tree_tin)
        right_sub_tree = self.reConstructBinaryTree(right_sub_tree_pre, right_sub_tree_tin)

        root = TreeNode(root_value)
        root.left = left_sub_tree
        root.right = right_sub_tree
        return root

