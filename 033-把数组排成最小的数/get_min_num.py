# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        """
        输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
        例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

        算法1：

        将数组的元素转换为字符串，然后求数组的 permutation，然后输出其中的最小数字。

        复杂度分析：

        时间复杂度：O(n!)
        空间复杂度：O(1)。使用 generator 可以做到 O(1) 的空间复杂度。

        算法2：

        要求最小的数字，我们需要将小的数字排在前面。所以提出一个算法：

        * 选择首位最小的数字
        * 如果首位数字相同，选择第二位最小的数字
        * ...
        * 选择第 n 位最小的数字
        * 比如 32 和 31 就选择 31

        对于位数不一致的情况，比如 32 和 321，选择位数最长的。这个算法解决不了 3, 325, 32 这样的情况。
        这个算法会在 325 和 32 中选择 325，实际应该选择 32 3 325。所以我们选择一个数，还会受到其他数字
        的影响。

        如果考虑这个情况，算法会很复杂，所以换一种思路。

        算法3：

        可以通过排序算法实现。排序算法可以分解为 compare 和 swap 两个部分。默认的 compare(a, b) 是
        返回 a < b，我们这里将其改写成返回使 a, b 排列最小的数。如何解决不同长度呢？

        在 Python 中可以通过 cmp 参数实现：https://docs.python.org/3/howto/sorting.html#the-old-way-using-the-cmp-parameter

        复杂度分析：

        时间复杂度：O(nlogn)
        空间复杂度：O(n)。由于 Python2 不支持 list.sort() 的 cmp，所以是 O(n)，Python3 支持，所以可以为 O(1)

        特殊情况是数组为空。返回 ''。
        """
        if not numbers:
            return ''
        # 这里使用 map(str, iterator) 将数字转换为字符串以用于连接，map 返回的是 iterator，不会占用
        # 额外空间
        return int(''.join(map(str, sorted(numbers, cmp=self.compare))))

    @staticmethod
    def compare(a, b):
        if int('{}{}'.format(a, b)) < int('{}{}'.format(b, a)):
            return -1
        return 1