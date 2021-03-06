# -*- coding:utf-8 -*-
from __future__ import division
import math


class Solution:
    def FindContinuousSequence(self, tsum):
        """
        输出所有和为S的连续（至少包括两个数）正数序列。
        序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

        比如输入 15，结果是 1~5、4~6、7~8。

        分析：
        连续正数：连续指 x, x + 1 ... x + n。正数指大于 0 的整数。

        算法1：
        求和公式为
        (x1 + xn) * n / 2，这里的 n >= 2。0 < x1 < (1 + tsum) // 2

        遍历 [1, tsum)：
            x1 = 当前遍历的元素
            n 的范围是 [x1 + 1, tsum)
            如果符合要求，就加入结果中
        复杂度分析：
        时间复杂度：O(n^2)。[1, tsum] 遍历 tsum 次，[x1+1, tsum) 是 n - 1 次，所以为 (n-1) + (n-2) + ... + 1 = O(n^2)
        空间复杂度：O(1)

        算法2：
        书上的，证明不出正确性，而且比较复杂。
        连续正数序列是一个递增的序列。我们以 [small, ... big] 表示一个子序列。
        由于最少需要两个数，所以初始子序列为 [1, 2]。

        如果子序列的和等于 tsum，则将这个子序列加入结果列表；
        如果子序列的和小于 tsum，我们要增大子序列的和：
            * 子序列数量不变，增大 small 和 big，比如 [1, 2] 变为 [2, 3]
            * 子序列数量加一，增大 big，比如 [1, 2] 变为 [1, 2, 3]
            * 这里采取第二种做法。因为返回的顺序 [1, 2] 在 [2, 3] 前面
        否则，要减小子序列的和：
            * 子序列数量不变，减小 small 和 big
            * 子序列数量减少：
                * 如果子序列数量为 2，那么说明不能减少
                * 否则，
                    * 删除 small，比如 [1, 2, 3] 删除 1 变成 [2, 3]
                    * 删除 big，比如 [1, 2, 3] 删除 3 变成 [1, 2]
                    * 这里选择删除 small，因为 small 更小

        算法3：
        假设目标序列的长度为 n：
            ① n 为奇数：序列中间的值是 xm，序列可以表示为 [... xm - 1, xm, xm + 1, ...]，xm 左右两边的数字一样多，并且可以相互抵消非 xm 部分，所以序列的平均值是 xm。
                另外 xm == S / n，因为 S 可以被 n 整除，所以 S % n == 0
            ② n 为偶数：序列可以表示为 [... x(m) - 1, x(m), x(m+1), x(m+1) + 1...]，x(m)、x(m+1) 两边的数字一样多，并且可以相互抵消非 x(m)、x(m+1) 的部分，
                所以平均值是 (x(m) + x(m+1)) / 2。
                (xm + xm+1) / 2 = S / n，而 xm+1 = xm + 1，所以 (2xm + 1) / 2 = S / n => xm + 0.5 = S / n
                所以 nxm + 0.5n = S，所以 S % n = 0.5n。余数的定义为：被除数 - 除数 * 整除时的商。
            ③ 第一个数为 S / n - (n - 1) / 2。证明：
                    a1 + an = 2 * s / n - ① -- 等差数列求和
                    an = a1 + n - 1 - ② -- 首项和末项的关系
                    将 ② 代入 ①：2a1 + n - 1 = 2 * s / n，a1 = (2s / n + 1 -n) / 2 = s / n + (1 - n) / 2

            ④ n 的最大长度。由于只能是正数，最小的正数为 1，第一个数最小时 n 最大。根据等差数列求和公式：S = (1 + 1 + n - 1) * n / 2
            => 2S = n * (1 + n) => 2S > n^2 => n < 根号(2S) => n <= int(根号(2S))

            根据④可以确认 n 的范围是 [2,  根号(2S))
            根据①、②可以确认所有的 n
            根据③可以由 n、S 计算出 a1 和 an，从而得到列表

        复杂度分析：
        时间复杂度：O(根号n)
        空间复杂度：O(1)

        来自 https://www.nowcoder.com/questionTerminal/c451a3fd84b64cb19485dad758a55ebe
        """
        result_list = []
        # Python2 的除法（/ 操作符）对于整数是整除，所以这里将其变为 float。牛客网的问题
        # 导致 from __future__ import division 不能正常工作
        tsum = float(tsum)
        n = int(math.sqrt(2 * tsum))
        while n >= 2:
            if (n % 2 == 1 and tsum % n == 0) or (n % 2 == 0 and tsum % n == 0.5 * n):
                first_num = int(tsum / n + (1 - n) / 2)
                result = list(range(first_num, first_num + n))
                result_list.append(result)
            n -= 1
        return result_list
