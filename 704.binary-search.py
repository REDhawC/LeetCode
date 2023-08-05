#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def lowerBound(numList, target):
            left = 0
            right = len(numList) - 1
            while left <= right:
                mid = (left + right) // 2
                if numList[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        targetIndex = lowerBound(nums, target)
        if targetIndex == len(nums) or nums[targetIndex] != target:
            return -1
        return targetIndex


# @lc code=end
