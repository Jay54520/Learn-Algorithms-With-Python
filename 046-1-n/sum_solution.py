# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self._sum = 0

    def Sum_Solution(self, n):
        """
        求1+2+3+...+n，要求不能使用乘除法、
        for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

        使用 and 运算符代替 if 执行判断。and 前面对应的布尔值为 True 就还会执行
        and 后面的语句，否则不会执行后面的语句。
        """
        self.sum(n)
        return self._sum

    def sum(self, n):
        self._sum += n
        n -= 1
        return n >= 1 and self.sum(n)