# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        """
        v1 使用的模拟法，可以看到代码很多，很繁琐，虽然复杂度方面没有问题。

        模拟魔方逆时针旋转的方法，一直做取出第一行的操作
        例如
        1 2 3
        4 5 6
        7 8 9
        输出并删除第一行后，再进行一次逆时针旋转，就变成：
        6 9
        5 8
        4 7
        重复上述操作直到 matrix 为空。

        复杂度：

        时间复杂度：O(n)，需要转向的次数就是魔方翻转的次数
        空间复杂度：O(n)，增加了翻转后的矩阵

        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        if not matrix:
            return []

        turned_matrix = []
        col_num = len(matrix[0])

        for col_index in range(col_num - 1, -1, -1):
            new_col = [row[col_index] for row in matrix]
            turned_matrix.append(new_col)
        return turned_matrix
