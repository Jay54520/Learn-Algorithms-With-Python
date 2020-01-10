class Solution:
    """
    题目描述
    一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

    1 floor: 1 way, jumps once
    2 floors:
    * jumps 1 floor, remaining 1 floor: f(1)
    * jumps 2 floors, remaining 0 floor: f(0). We assume f(0) is 1 although there's no zero floor
    3 floors:
    * jumps 1 floor, remaining 2 floor: f(2)
    * jumps 2 floors, remaining 1 floor: f(1).
    * jumps 2 floors, remaining 1 floor: f(0).

    f(n) = f(n-1) + f(n-2) + ... + f(0)
    because f(n-1) = f(n-2) + ... + f(0)
    so f(n) = f(n-1) + f(n-1) = 2 * f(n-1) = 2^2 * f(n-2), end when f(1) = 1.
    because f(1) is 1, so the number of 2 starting with (n-1) is [(n-1)-2+1]=n-2, so f(n) = 2 * 2 ^ (n-2) = 2^(n-1)
    (simple way by illustrating a example: let n = 3, 2 * f(2) = 2 * 2 * f(1) = 2^2)

    So the formula is

    1 (n <= 1)
    f(n) = 2^(n-1)
    """
    def jumpFloor(self, number):
        pass