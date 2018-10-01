# -*- coding:utf-8 -*-
import math


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        """
        未解决，需要帮助。

        求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

        比如 1-13中包含1的数字有 1、10、11、12、13，所以 1 出现的次数为：
        1 + 1 + 2 + 1 + 1 = 6

        算法3：

        原书上的，算法2是根据数字含有 1 的个数划分为 n 种情况。这里将分为：

        1 出现在第一位、第二位 ... 第 logn + 1 位。

        对于 21345：

        1 在第一位：10000 - 19999，为 19999 - 10000 + 1 = 10000 个
        1 其他位：选择一位为 1，其他位可以是 0 - 9 有 10 种情况，

        看不懂，于是去牛客网上找其他解释。

        算法4：

        来自 https://www.nowcoder.com/questionTerminal/bd7f978302044eee894445e244c7eee6 #moluchase 的回答

        1. 令n的第一位为f，n的其余位为l；（如n=123，则f=1，l=23；n=234，则 f = 2, l = 34）
        2. 如果f大于1，表明n包含了最高位为1的全部情况（比如n=223，f=2；n的最高位包含了[100, 200)共100个数；
        类似的，当n的位数为4时，为 [1000, 2000)，有1000种情况，所以对于 m 位数，如果 f > 1，那么最高位为 1 的情况有 10 ^ (m-1) 种）；
        3. 如果f等于1，比如n=123，f=1；说明n包含了[100, 123]这24次最高位为1的情况，即l+1；
        4. 然后去除 f，剩下 l，对 l 使用同样的算法求出 1 的次数。

        对于 13，使用上述算法：

        * f 等于 1，属于首位为 1 的情况，所以有 l + 1 = 3 + 1 = 4种
        * l 等于 3，大于 1，所以为 10 ^ (1 - 1) = 1 种
        * 一共有 4 + 1 = 5，与题意的 6 不符，原因是少算了 11 的个位数的 1。

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
