#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#


# @lc code=start
# ???? 怎么优化,会重复吗????
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # visited = set()
        res = 0
        zeroStr = "0" * zero
        oneStr = "1" * one

        def backtracking(curStr):
            nonlocal res
            if len(curStr) > high:
                return
            if low <= len(curStr) < high:
                res += 1
            if len(curStr) == high:
                res += 1
                return
            #
            backtracking(curStr + zeroStr)
            backtracking(curStr + oneStr)

        backtracking("")
        return res


# @lc code=end
