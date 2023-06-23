#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        fast = 1
        slow = 0
        count = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                if count > len(nums) / 2:
                    break
                else:
                    count = 1
            else:
                count += 1
            fast += 1
            slow += 1
        return nums[slow]


# @lc code=end
