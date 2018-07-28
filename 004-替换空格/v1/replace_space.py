# -*- coding:utf-8 -*-

class Solution:
    def replaceSpace(self, s):
        """
        请实现一个函数，将一个字符串中的每个空格替换成“%20”。
        例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

        对于 Python 来说，自带的特性已经处理了这个问题，如果面试官同意的话，就使用它。

        :param s: 原字符串
        :return:
        """
        return s.replace(' ', '%20')