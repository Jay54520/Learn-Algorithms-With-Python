# -*- coding:utf-8 -*-
class Solution:

    def Power(self, base, exponent):
        """
        给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

        算法2：根据 https://zh.wikipedia.org/wiki/冪 的定义和题目的要求，总结出规律如下：

        如果 exponent 大于 0，那么 b ^ exponent = b 自乘 exponent 次；
        如果 exponent 等于 0，那么结果为 1；
        否则，如果 base 为 0，那么结果为 1，否则结果为 1 / (b 自乘 exponent 次)

        算法3：

        如果 n 是偶数，那么 result = base ^ (n / 2) * base ^ (n / 2) = power(base, n / 2) * power(base, n / 2)；
        否则 n 是奇数，result =  base ^ ( (n -1) / 2) * base ^ ( (n - 1) / 2) * base =
        power(base, (n-1) / 2) * power(base, (n-1) / 2) * base；

        终止条件是 n 为 0 或 1。

        复杂度分析：

        时间复杂度：O(logn)，2 ^ k = n => k = logn
        空间复杂度：O(1)
        """
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base

        abs_exponent = abs(exponent)
        half_result = self.Power(base, abs_exponent // 2)
        result = half_result * half_result
        if abs_exponent % 2 == 1:
            result *= base
        if exponent < 0:
            if result == 0:
                result = 1
            else:
                result = 1 / result
        return result
