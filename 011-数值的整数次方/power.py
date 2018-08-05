# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        """
        给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

        算法1：使用编程语言自带的特性

        算法2：根据 https://zh.wikipedia.org/wiki/冪 的定义和题目的要求，总结出规律如下：

        如果 exponent 大于 0，那么 b ^ exponent = b 自乘 exponent 次；
        如果 exponent 等于 0，那么结果为 1；
        否则，结果为 1 / (b 自乘 exponent 次)

        从上可以总结出，初始结果是 1。由于第一种和第三种互为倒数，所以代码可以合并。

        如果 exponent 可以为分数，那么还要加条件。

        这种题目的关键是要弄清楚需求，然后不要遗漏某些情况。但我一看到就默认 exponent 大于 0 而不是
        想到整数可以为负数、0 和正数。因为对 power 的定义不熟悉，不知道这种情况能不能搜索 power（问题） 的定义。

        复杂度分析：

        时间复杂度：O(n)，操作 exponent 次
        空间复杂度：O(1)
        """
        result = 1
        if exponent != 0:
            for i in range(abs(exponent)):
                result *= base
            if exponent < 0:
                result = 1 / result
        return result
