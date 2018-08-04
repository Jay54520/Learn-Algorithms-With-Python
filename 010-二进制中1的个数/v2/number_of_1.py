# -*- coding: utf-8 -*-
import sys

MAXINT = sys.maxint + 1


class Solution:
    """
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

    算法2：
    依次检查所有的 bit，Python2 最大是 64 bit，所以要检测 64 次。
    检查第 k（0<=k<64） 位是否是1：将其与 0000...1（从右开始数第k个，k从0开始）...0 进行位与操作，
    如果结果是 0，说明第 k 位是 0，否则第 k 位是 1。因为 0 与任何数位与都为 0，而另一个数除了第 k 位
    都是0，所以只有当第 k 位为 1 时的位与结果才不会为 0.
    """

    def NumberOf1(self, n):
        number_of_1 = 0
        flag = 1
        while flag <= MAXINT:
            if flag & n:
                number_of_1 += 1
            flag <<= 1
        return number_of_1