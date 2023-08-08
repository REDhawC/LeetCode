#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dpTable = [-1] * (n + 1)
        dpTable[0], dpTable[1] = 0, 1
        for i in range(2, n + 1):
            dpTable[i] = dpTable[i - 1] + dpTable[i - 2]
        return dpTable[n]


# @lc code=end
