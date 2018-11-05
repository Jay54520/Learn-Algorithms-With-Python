# -*- coding:utf-8 -*-
import math


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        """
        求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

        比如 1-13中包含1的数字有 1、10、11、12、13，所以 1 出现的次数为：
        1 + 1 + 2 + 1 + 1 = 6

        算法1：

        依次遍历所有数字，将数字转换为字符串，然后计算 1 的次数并添加到结果中。

        复杂度分析：
        时间复杂度：n 次循环，由于数字是有界的，无符号数的长度最大为 64，相比于 n 的最大 2 ^ 64 可以忽略，所以
        每次循环将数字转换为字符串以及计数需要数字长度的操作数可以忽略不计，所以为 O(n)
        空间复杂度：O(1)

        算法2：
        将数字看成字符串。
        则 digit 位数的所有情况是 0 - 9 的字符串排列。
        
        * 1 位数为 0 - 9，有 10 种
        * 2 为数为 {0-9}{0-9}，为 10 * 10 = 100

        但我们只需要求含有 1 的情况，可分为：

        * 含有 1 个 1，任意一位为 1，其他为位 [0, 1) 或 (1, 9]，有 1 * C(digit, 1) * 9 ^ (digit - 1) 个 1
        * 含有 2 个 1，任意两位为 1，其他为位 [0, 1) 或 (1, 9]，有 2 * C(digit, 2) * 9 ^ (digit - 2) 个 1
        * ...
        * 含有 digit 个 1，任意 digit 位为 1，其他为位 [0, 1) 或 (1, 9]，有 digit * C(digit, digit) * 9 ^ (digit - digit) 个 1

        由于要求小于等于 n，所以要排除大于 n 的含有 1 的数。遍历 (n, 10 ^ digit)，从总次数中减去其中 1 的次数

        复杂度分析：
        时间复杂度：n 含有 (logn + 1) 位数，所以遍历为 O(logn)。但排除时最多相差 10 * n - n，
        所以还是为 O(n)。所以能不能优化最后的排除使其变为 O(logn)？

        边界情况：

        * n = 0，返回 0
        """
        total = 0
        if n <= 0:
            return total
        digit = int(math.log10(n)) + 1
        for number_of_1 in range(1, digit + 1):
            total += number_of_1 * self.permutations(digit, number_of_1) * (9 ** (digit - number_of_1))

        for greater_num in range(n + 1, 10 ** digit):
            total -= str(greater_num).count('1')
        return total

    def permutations(self, n, k):
        """
        返回 C(n, k)，等于 n! / ((n - k)! * k!)
        根据https://en.wikipedia.org/wiki/Permutation
        :param n:
        :param k:
        :return:
        """
        return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))