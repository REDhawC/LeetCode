#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#


# @lc code=start
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        def lowerBound(numList):
            left = 0
            right = len(numList) - 2
            while left <= right:
                mid = (left + right) // 2
                if numList[mid] > numList[mid + 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        return lowerBound(nums)


# @lc code=end
