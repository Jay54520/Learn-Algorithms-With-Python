# -*- coding:utf-8 -*-
class Solution:

    def Permutation(self, ss):
        """
        输入一个字符串,按字典序打印出该字符串中字符的所有排列。
        例如输入字符串abc,则打印出由字符a,b,c所能排列出来的
        所有字符串abc,acb,bac,bca,cab和cba。

        输入描述:
        输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

        算法及证明

        先忽略字典序以及重复字符的条件，因为这两个条件可以在后面加上而不影响代码架构。

        如果字符串为空，自然返回空列表；
        如果只有一个字符，那么它的全排列就是它本身。
        如果有多个字符，那么全排列为每个字符加上其他字符的全排列。

        推导出递归的写法为：

        终止条件：只有一个字符，将其添加到 tmp_result，然后添加到 results 中；
        循环：遍历输入字符串，将当前字符加入 tmp_result，然后求 tmp_result 与
        其他字符的全排列。每次求完后要恢复 tmp_result，避免上次的影响这次的结果。

        加入字典序条件：将输入按照字典序排序即可。因为这里是遍历字符串，所以结果
        的顺序会和字符串的顺序相同。

        可能存在重复字符：不加入已经存在的结果

        复杂度分析：

        时间复杂度：排序字符串 O(nlogn)、排列组合为 T(n) = T(n - 1) * n = T(n-2) * n * (n - 1)
        = ... = n * (n - 1) * ... * 1 = n!，所以为 O(n!)
        空间复杂度：集合 —— O(n)，所以为 O(n)
        
        abcd bacd 中都要求 cd 的排列组合，有重复计算，所以可以通过缓存计算结果来
        减少时间复杂度。
        缓存后由于之前的已经计算过了，只要直接读取，所以 T(n) = n + T(n - 1) = n + (n - 1) + T(n - 2)
        = ... = n + (n - 1) + ... + 1 = O(n ^ 2)
        空间复杂度变为 O(n!)，所以的排列组合数。
        """
        results = []
        if not ss:
            return results

        ss = list(sorted(ss))
        self.permutation(ss, [], results)
        return results

    def permutation(self, ss, tmp_result, results):
        if len(ss) == 1:
            tmp_result += ss
            result = ''.join(tmp_result)
            if result not in results:
                results.append(result)
        else:
            length = len(tmp_result)
            for index, s in enumerate(ss):
                tmp_result = tmp_result[:length] + [s]
                self.permutation(ss[:index] + ss[index+1:], tmp_result, results)

