# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        """
        把字符串前面的若干个字符移动到字符串的尾部。
        比如输入 'abcdefg' 和 2，则输出为 'cdefgab'。

        算法1：
        real_rotate = n % length。结果等于 real_rotate 后的字符串与 real_rotate 前的字符串
        进行拼接。

        复杂度分析：
        时间复杂度：O(n)。拼接出长度为 n 的字符串
        空间复杂度：O(1)
        """
        if not s:
            return s
        real_rotate = n % len(s)
        return s[real_rotate:] + s[:real_rotate]