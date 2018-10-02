# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        """
        把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
        习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

        质因子：如果一个数 m 能整除给定的正整数 n，并且 m 是指数，那么 m 是 n 的质因子
        质数：在大于1的自然数中，除了1和它本身不再有其他因数
        因数：整数a除以整数b(b≠0) 的商正好是整数而没有余数，我们就说b是a的因数。0不是0的因数

        算法1：
        ugly_num = 2 ^ x * 3 ^ y * 5 ^ z(x, y, z 都是自然数)

        给定一个自然数 x，可知：2 ^ x < 3 ^ x < 5 ^x，所以加一之后，优先给前面的质因子加 1，然后
        才是后面的质因子。

        (0, 0, 0),
            + 1：
                (1, 0, 0), # 给 2 加一，因为 2 < 3 < 5
                (0, 1, 0), # 给 3 加一，因为 3 < 5
                (0, 0, 1), # 给 5 加一
            + 2：
                从 + 1 中最小的丑数 (1, 0, 0) 加起，(1, 0, 0) 对应 2 * 2 ^ x * 3 ^ y * 5  ^ z

        现在有两种选择：
            1. 在上面
            2. 给 3 加一

        ...
        这个思路太复杂了，所以换一种思路。

        算法2：

        参考 https://www.nowcoder.com/questionTerminal/6aa9e04fc3794f68acf8778237ba065b #青儿

        1 (0, 0, 0)
        2 * 1, 3 * 1, 5 * 1 -> 1, 2 (1, 0, 0)
        2 * 2, 3 * 1, 5 * 1 -> 1, 2, 3 (1, 1, 0)
        2 * 2, 3 * 2, 5 * 1 -> 1, 2, 3, 4  (2, 1, 0)

        “比较3个数：用于乘2的最小的数、用于乘3的最小的数，用于乘5的最小的”

        不知道如何证明。

        复杂度：
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if index < 1:
            return 0
        ugly_nums = [1]
        x, y, z = 0, 0, 0
        while len(ugly_nums) < index:
            x_product = 2 * ugly_nums[x]
            y_product = 3 * ugly_nums[y]
            z_product = 5 * ugly_nums[z]
            ugly_num = min(x_product, y_product, z_product)
            ugly_nums.append(ugly_num)
            if ugly_num == x_product:
                x += 1
            if ugly_num == y_product:
                y += 1
            if ugly_num == z_product:
                z += 1

        return ugly_nums[index - 1]