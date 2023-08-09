#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#


# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = 0
        dpTable = [0] * (high + 1)
        dpTable[0] = 1  # 技巧！DP中空字符串的情况为1
        MOD = 10**9 + 7
        for i in range(1, high + 1):
            if i >= zero:
                dpTable[i] = dpTable[i - zero] + dpTable[i]
            if i >= one:
                dpTable[i] = dpTable[i - one] + dpTable[i]

        for i in range(low, high + 1):
            res += dpTable[i]

        return res % MOD


# @lc code=end
