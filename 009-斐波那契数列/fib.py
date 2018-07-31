# -*- coding:utf-8 -*-
class Solution:
    """
    在数学上，费波那契数列是以递归的方法来定义：

    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2)

    算法分析及证明

    使用递归的算法。

    循环条件：当 n > 1 时，F(n) = F(n-1) + F(n-2)
    终止条件：当 n == 0 或 n == 1 时，F(0) = 0，F(1) = 1
    可以看出上述条件符合斐波那契的定义，所以证明通过。

    复杂度分析：

    时间复杂度：令 T(n-2) 约等于 T(n-1)，那么 T(n) = 2T(n-1) = 2^2T(n-2) = ... = 2^nT(n-n)
    由于 T(0) 是一个操作单位，所以时间复杂度为 O(2^n)。
    
    空间复杂度：O(1)

    优化

    我们可以看到上面有重复的计算，比如计算 F(n-1) 的过程中，F(n-2) 已经计算过了，所以我们通过缓存来避免重复计算。
    
    复杂度分析：
    
    时间复杂度：由于计算 F(n-1) 的过程中，F(n-2) 已经计算过了，所以 T(n) = T(n-1) + 1，这里的 1 是从 cache 中
    读取 F(n-2) 的操作数。所以 T(n) = T(n-1) + 1 = T(n-2) + 2 = ... = T(n-n) + n，
    （T(n-1) + 1 = T(n-2) + 2 是由于 T(n-1) = T(n-2) + 1），由于 T(n-n) = T(0) = 1，所以时间复杂度为 O(n + 1)，也就是 O(n)。
    
    空间复杂度：缓存中有 0 ~ n 一共 n + 1 个数，所以为 O(n)。
    """

    def __init__(self):
        self.cache = {
            0: 0,
            1: 1
        }

    def Fibonacci(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            result = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            self.cache[n] = result
            return result
