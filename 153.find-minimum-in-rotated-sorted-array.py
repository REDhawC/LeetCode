#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start


# your binary search skills need to be improved!
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid

            else:
                left = mid + 1

        return nums[left]


# Solution.findMin(Solution, [4, 5, 6, 7, 0, 1, 2])
# @lc code=end
