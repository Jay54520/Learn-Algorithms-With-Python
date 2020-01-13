# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        """使实例用到的所有属性在 __init__ 中都能读到，可以提高可读性"""
        self.row_start = 0
        self.row_end = 0
        self.col_start = 0
        self.col_end = 0
        self.result = []
        self.matrix = []

    def printMatrix(self, matrix):
        """
        从外方向里顺时针顺序读取矩阵，并返回读取结果。

        示例：

        输入：
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        输出 [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

        算法：

        观察得出，依次向右、向下、向左、向上，然后再向右进入循环；
        读取的范围：矩阵的边界和已读行、列的最小范围。如果将已读行列设置为边界，那么就能将
        读取的范围合并为矩阵的边界。

        循环：从某个坐标开始，向右读取，到边界后；向下移动一个位置并向下读取，到边界后；
        向左移动一个位置并向左读取，到边界后；向上移动一个位置并向上读取，到边界后；
        又向右移动一个位置并开始读取；然后又向右，这样一直循环。

        终止条件：开始移动时碰到边界
        [
            [1]
        ]
        假设向右：row_start += 1, row_start = 1
        假设向下：col_end -= 1, col_end = -1
        向左：row_end -= 1, row_end = -1
        向上： col_start += 1, col_start = 1
        总结就是 row_start > row_end or col_start > col_end

        证明：

        不考虑矩阵不合法的情况，比如所有行的数目不一致，如 [[1], [1, 2]]。

        * 空矩阵，包括 [] 返回 []；
        * 一行矩阵，读取第一行，碰到边界，向下还是边界，于是返回第一行的数据，符合条件；
        * 多行矩阵，不知道怎么证明。感觉算法已经将问题描述表现出来了。

        复杂度：

        时间复杂度：O(n)，n 为矩阵中的元素个数。
        空间复杂度：O(1)

        总结

        写的过程中遇到的问题有：

        * 有多种情况，每种情况还有差异，所以要思考清楚再写
        * 没有抽取出读取行、列的函数，导致重复，使代码逻辑更复杂

        """
        if not matrix or not matrix[0]:
            return self.result

        self.matrix = matrix
        self.row_end = len(matrix) - 1
        self.col_end = len(matrix[0]) - 1
        self.right()
        return self.result

    def right(self):
        if self.out_of_border():
            return
        self.result.extend(self.matrix[self.row_start][self.col_start:self.col_end + 1])
        self.row_start += 1
        self.down()

    def down(self):
        if self.out_of_border():
            return
        for i in range(self.row_start, self.row_end + 1):
            self.result.append(self.matrix[i][self.col_end])
        self.col_end -= 1
        self.left()

    def left(self):
        if self.out_of_border():
            return
        self.result.extend(reversed(self.matrix[self.row_end][self.col_start:self.col_end + 1]))
        self.row_end -= 1
        self.up()

    def up(self):
        if self.out_of_border():
            return
        for i in range(self.row_end, self.row_start - 1, -1):
            self.result.append(self.matrix[i][self.col_start])
        self.col_start += 1
        self.right()

    def out_of_border(self):
        return self.row_start > self.row_end or self.col_start > self.col_end
