#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lowerBound(numList, target):  # >=
            left = 0
            right = len(numList) - 1
            while left <= right:
                mid = (left + right) // 2
                if numList[mid] < target:
                    left = mid + 1
                elif numList[mid] > target:
                    right = mid - 1
                elif numList[mid] == target:
                    right = mid - 1
            return left

        start = lowerBound(nums, target)  # >=
        if len(nums) == 0 or start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lowerBound(nums, target + 1) - 1  # <=
        return [start, end]


# @lc code=end
