#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        if n == 2:
            return False
        while sum != 1:
            happyList = list(str(n))
            sum = 0
            for i in happyList:
                sum += int(i) ** 2
            n = sum
        return True


# strs = 19
# Solution.isHappy(Solution, strs)

# @lc code=end
