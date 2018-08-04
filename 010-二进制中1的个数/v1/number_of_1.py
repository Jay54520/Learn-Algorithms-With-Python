# -*- coding: utf-8 -*-
import sys

MAXINT = 2 * (sys.maxint + 1)


class Solution:
    """
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

    算法1：

    如果可以使用编程语言自带的特性，那么就将数字 n 转换成二进制字符串，然后计算
    其中 1 的个数。但由于考点是二进制，所以不能这样做。
    另外，Python 中的二进制负数没有使用补码的形式，而是带了符号，所以需要我们自己转换。

    复杂度分析：时间、空间复杂度都是 O(1)。因为最大是 64 位。
    """

    def NumberOf1(self, n):
        if n < 0:
            # 根据 《编码》，2 的补数等于该数求反后加一
            n = self.get_complement(abs(n))
        return bin(n).count('1')

    def get_complement(self, num):
        """获取当前 Python 的下 num 的 2 的补数"""
        if num < 0:
            raise ValueError('num 不能小于 0')
        # 32 位 Python 是 2 ** 32，64 位 Python 是 2 ** 64
        # 参考 https://stackoverflow.com/a/7604981/5238892
        return MAXINT - num
