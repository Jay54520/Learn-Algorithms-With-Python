# -*- coding:utf-8 -*-

VALID_CHARS = [str(i) for i in range(9)] + ['+', '-']


class Solution:
    def StrToInt(self, s):
        """
        不使用字符串转换整数的库函数将字符串转换为数字。字符串的范围是 ASCII。
        对于不合法的返回 0。
        比如 +214 -> 214；1a3 -> 0。

        1. 如果字符串中存在非数字或 +、-，则说明存在非法字符，返回 0
        2. 如果 +、- 不在首位，说明 +、- 位置非法，返回 0
        3. 取出 +、- 号后，数字 = 10 ^ (n - 1) * 第一位 + 10 ^ (n - 2) * 第二位 + ... + 10 ^ (n - n) * 最后一位
           然后如果存在 - 号，则加上 - 号

        复杂度分析：
        时间复杂度：O(n)。遍历了两次字符串。
        空间复杂度：O(1)
        """
        num = 0
        if not s:
            return 0
        for index, char in enumerate(s):
            if char not in VALID_CHARS:
                return num
            if char in ['+', '-'] and index != 0:
                return num

        negative = False
        digits = len(s)
        start_index = 0
        if s[0] in ['+', '-']:
            digits -= 1
            if s[0] == '-':
                negative = True
            start_index = 1

        for index, char in enumerate(s[start_index:]):
            num += 10 ** (digits - 1 - index) * int(char)
        if negative:
            return 0 - num
        return num