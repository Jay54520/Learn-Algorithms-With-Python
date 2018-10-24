# -*- coding:utf-8 -*-

class Solution:

    def VerifySquenceOfBST(self, sequence):
        """
        输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
        如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

        二叉搜索树：

        1. 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
        2. 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
        3. 任意节点的左、右子树也分别是二叉查找树；
        4. 没有键值相等的节点。 -- 来自 https://zh.wikipedia.org/wiki/二元搜尋樹

        后序遍历指先遍历左子树，再遍历右子树，最后根节点。所以

        8
        | \
        3  10
         \  |
         6 14

        的后续遍历结果为 [6, 3, 14, 10, 8]

        将上方的 3 替换为 100 变为 [6, 100, 14, 10, 8]， 想着这样就能非法了，但实际上还是合法的后续遍历结果：

        8
        | \
        6 10
          \
          14
            \
            100

        非法：[7,4,6,5]

        5
         \
         6
         |
         4
          \
           7

         6, 4, 7 是合法的，但是 5, 6, 4, 7 就不合法了，因为 4 在右子树中但是小于根节点 5。

        算法与分析：

        * 为空，返回 False（根据题意）
        * 非空，分离出左子树数组、右子树数组、根节点，第一个大于根节点的是节点是右子树根节点，右子树根节点之前的所有节点是左子树：
            * 根节点应该大于左子树所有节点，小于右子树所有节点，如果对应的子树存在
            * 左右子树也要是二叉搜索树，如果对应的子树存在

        复杂度分析：

        时间复杂度：假设只有左子树，只有一个孩子，那么找第一个右子树的索引需要花费

        (n - 1) + (n - 2) + (n - 3) + ... + 1 = O(n^2)

        将根节点与所有左子树节点比较的花费也和上面一样，所以为 O(n^2)。

        空间复杂度：O(1)，切片后没有创建新元素(可以通过内存地址证明：https://stackoverflow.com/a/5131563/5238892)，所以为 O(1)

        反思：

        * 二叉搜索树和后续遍历的概念不够熟，需要查找资料后才清楚。对于这种常考的数据结构，需要熟练。
        * 忽视了左右子树的后代也要满足条件而不仅仅是孩子
        * 走偏了，一开始想要根据这个生成二叉搜索树，但发现题目是判断是否合法。

        """
        length = len(sequence)
        if length == 0:
            return False
        elif length == 1:
            return True

        left_sub = []
        right_sub = []
        root_val = sequence[-1]
        for index, node in enumerate(sequence[:-1]):
            if node > root_val:
                left_sub = sequence[:index]
                right_sub = sequence[index:-1]
                break
        if left_sub:
            for n in left_sub:
                if not n < root_val:
                    return False
            if not self.VerifySquenceOfBST(left_sub):
                return False
        if right_sub:
            for n in right_sub:
                if not root_val < n:
                    return False
            if not self.VerifySquenceOfBST(right_sub):
                return False
        return True
