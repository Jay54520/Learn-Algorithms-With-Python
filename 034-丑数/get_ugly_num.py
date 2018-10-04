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

        令 ugly_nums 是从小到大的不重复丑数列表。根据题意，ugly_nums 初始为 [1]。
        由于丑数的质因子是 2、3、5，所以 ugly_nums 中的任意丑数（除了第一个），一定等于
        之前的某一个丑数乘以 2 或 3 或 5。

        第一个丑数是 1，第二个丑数只能是 min(2*1, 3*1, 5*1, 2*2, 3*2, 5*2)，所以是 2，这时 ugly_nums = [1, 2]。由于这时
        2 已经加入了ugly_nums，所以为了避免重复，将 factor_of_2 指向下一个丑数，也就是 2。

        第三个丑数可能是min(2*2, 3*1, 5*1, 3*2, 5*2)，丑数只会出现在前三种情况中，因为前三种
        情况是 (2 * factor_of_2, 3 * factor_of_3, 5 * factor_of_5)，而这些 factors 都是
        各自对应的最小 factor。 下一个丑数是 3，这时 ugly_nums = [1, 2, 3]，
        由于 3 已经加入了 ugly_nums，所以将 factor_of_3 指向 1 的下一个丑数，还是 2。

        第四个丑数可能是min(2*2, 3*2, 5*1)，所以是 4，这时 ugly_nums = [1, 2, 3, 4]，
        由于 3 已经加入了 ugly_nums，所以将 factor_of_2 指向 factor_of_2 的下一个丑数，是 3。

        min(2*3, 3*2, 5*1)，ugly_nums = [1,2,3,4,5], factor_of_5 指向 2

        min(2*3, 3*2, 5*2)，ugly_nums = [1,2,3,4,5,6], factor_of_2 和 factor_of_3 都要
        右移。

        min(2*4, 3*3, 5*2)，ugly_nums = [1,2,3,4,5,6, 8], factor_of_2 右移。

        min(2*5, 3*3, 5*2)，ugly_nums = [1,2,3,4,5,6, 8, 9], factor_of_3 右移。

        min(2*5, 3*4, 5*2)，ugly_nums = [1,2,3,4,5,6, 8, 9], factor_of_2 和 factor_of_5 都要右移。

        截止目前，相等的丑数都是在同一轮次出现。如果相等的丑数不在一轮中出现，那么对于这个丑数，必然会
        两次加入 ugly_nums，和假设 ugly_nums 是从小到大的不重复丑数列表冲突，所以不成立。所以相等
        的丑数一定会在同一轮中出现。

        复杂度：
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if index < 1:
            return 0
        ugly_nums = [1]
        factor_of_2, factor_of_3, factor_of_5 = 0, 0, 0
        while len(ugly_nums) < index:
            product_of_2 = 2 * ugly_nums[factor_of_2]
            product_of_3 = 3 * ugly_nums[factor_of_3]
            product_of_5 = 5 * ugly_nums[factor_of_5]
            ugly_num = min(product_of_2, product_of_3, product_of_5)
            ugly_nums.append(ugly_num)
            if ugly_num == product_of_2:
                factor_of_2 += 1
            if ugly_num == product_of_3:
                factor_of_3 += 1
            if ugly_num == product_of_5:
                factor_of_5 += 1

        return ugly_nums[index - 1]