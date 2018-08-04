# -*- coding: utf-8 -*-
import sys

MAXINT = 2 * (sys.maxint + 1)


class Solution:
    """
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

    算法3：
    观察二进制的减法：

     1100
    -0001
    ------
     1011

     从右边开始，第一位 0 < 1，向前借一位，第二位同理，第三位借了一位给第二位，于是变成 0；
     第二位变成 10；第二位借给了第一位，变成了 1，第一位变成了 10，第一位减去 1，变成了 1。

     1100 & 1011 = 1000，所以假设 n & (n-1) 会使 n 的最后一个 1 变为 0。所以 n 有多少个 1
     就能执行多少次这样的操作，直到变为 0 为止。

     证明：如果 n 的最后一位是 1，那么 n - 1 的最后一位是 0，n & (n - 1) 使 n 的最后一个 1 变为 0 了；
     如果 n 的第 m 位是 1，那么减一就要像上面那样一直结尾，使得第 m 位变为 0，m 位右边的所有位变为 1，
     所以 n & (n-1) 还是会使 n 的最后一个 1 变为 0，因为 m 位和 m 位右边的每两个位中都有一个 0 存在。

     参考原书。
    """

    def NumberOf1(self, n):
        number_of_1 = 0

        if n < 0:
            n = self.get_complement(abs(n))

        while n:
            number_of_1 += 1
            n = n & (n - 1)

        return number_of_1

    def get_complement(self, num):
        """获取当前 Python 的下 num 的 2 的补数"""
        if num < 0:
            raise ValueError('num 不能小于 0')
        # 32 位 Python 是 2 ** 32，64 位 Python 是 2 ** 64
        # 参考 https://stackoverflow.com/a/7604981/5238892
        return MAXINT - num
