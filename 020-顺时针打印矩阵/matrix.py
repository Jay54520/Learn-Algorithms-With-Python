# -*- coding:utf-8 -*-
from collections import defaultdict

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

NEXT_DIRECTIONS = {
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
    UP: RIGHT
}


class Solution:

    def __init__(self):
        """使实例用到的所有属性在 __init__ 中都能读到，可以提高可读性"""
        self.matrix = []
        self.result = []
        self.start_row = 0
        self.end_row = 0
        self.start_col = 0
        self.end_col = 0
        self.whole_cols = defaultdict(list)

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

        终止条件：碰到边界，转向后还是边界。

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
        # 空矩阵
        if not matrix:
            return []

        # 这些初始化放在 __init__ 中更好，但是题目已经固定了，就不好改了。
        self.matrix = matrix
        self.init_original_cols()
        self.result = []

        # ------------通过开始、结束行、列的索引来划定边界------------
        self.start_row = 0
        self.end_row = len(matrix) - 1
        self.start_col = 0
        self.end_col = len(matrix[0]) - 1
        # ------------通过开始、结束行、列的索引来划定边界------------

        direction = RIGHT
        current_row = 0
        current_col = 0
        self.move(current_row, current_col, direction)
        return self.result

    def move(self, current_row, current_col, direction):
        """
        将当前行或列按照 direction 方向加入 result。然后试探能否向下一个方向移动，
        如果不能，返回；否则，调整边界和当前坐标，将已读的行、列设置为新边界，当前坐标
        是转向后的下一个元素。
        """
        if direction == RIGHT:
            # 读取当前行
            self.result.extend(self.get_row(current_row, direction))
            # 如果是最后一行，那么就不能向下了
            if current_row == self.end_row:
                return
            else:
                # 将已读行设置为边界
                self.start_row += 1
                # ------- 当前元素变为下一行最后一个元素 ------------
                current_row = self.start_row
                current_col = self.end_col
                # ------- 当前元素变为下一行最后一个元素 ------------
                self.move(current_row, current_col, NEXT_DIRECTIONS[direction])
        elif direction == DOWN:
            # 读取当前列
            self.result.extend(self.get_col(current_col, direction))
            # 如果是第一列，那么就不能向左了
            if current_col == self.start_col:
                return
            else:
                # 将已读列设置为边界
                self.end_col -= 1
                # ------- 当前元素变为最后一行最后一列 ------------
                current_row = self.end_row
                current_col = self.end_col
                # ------- 当前元素变为最后一行最后一列 ------------
                self.move(current_row, current_col, NEXT_DIRECTIONS[direction])
        elif direction == LEFT:
            self.result.extend(self.get_row(current_row, direction))
            # 如果当前行是第一行，那么不能向上了
            if current_row == self.start_row:
                return
            else:
                # 将已读行设置为边界
                self.end_row -= 1
                # ------- 当前元素变为最后一行第一个元素 ------------
                current_row = self.end_row
                current_col = self.start_col
                # ------- 当前元素变为下一行最后一个元素 ------------
                self.move(current_row, current_col, NEXT_DIRECTIONS[direction])
        else:  # 向上
            self.result.extend(self.get_col(current_col, direction))
            # 如果当前列是最后一列，那么不能向右了
            if current_col == self.end_col:
                return
            else:
                # 将已读列设置为边界
                self.start_col += 1
                # ------- 当前元素变为第一行第一个元素 ------------
                current_row = self.start_row
                current_col = self.start_col
                # ------- 当前元素变为第一行第一个元素 ------------
                self.move(current_row, current_col, NEXT_DIRECTIONS[direction])

    def get_row(self, row, direction):
        """按照 direction 返回第 row 行的元素（使用当前边界）"""
        result = self.matrix[row][self.start_col:self.end_col + 1]
        if direction == RIGHT:
            return result
        else:
            return reversed(result)

    def get_col(self, col, direction):
        """按照 direction 返回第 col 列的元素（使用当前边界）"""
        whole_col = self.whole_cols[col]
        result = whole_col[self.start_row: self.end_row + 1]
        if direction == UP:
            return reversed(result)
        else:
            return result

    def init_original_cols(self):
        """初始化原始矩阵的列，避免之后重复计算"""
        if not self.matrix:
            raise ValueError('没有初始化原始矩阵')
        col_num = len(self.matrix[0])
        for row in self.matrix:
            for col in range(col_num):
                self.whole_cols[col].append(row[col])

