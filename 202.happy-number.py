#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        savedNums = set()
        while True:
            sum = 0
            happyList = list(str(n))
            for i in happyList:
                sum += int(i) ** 2
            if sum in savedNums:
                return False
            if sum == 1:
                return True
            n = sum
            savedNums.add(sum)


strs = 19
Solution.isHappy(Solution, strs)

# @lc code=end
