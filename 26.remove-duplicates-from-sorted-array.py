#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                nums.remove(nums[fast])
            else:
                fast += 1
                slow += 1
        return fast


# @lc code=end
