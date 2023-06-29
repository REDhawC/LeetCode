#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        left = 0
        right = 0
        min_Len = 10**5 + 1
        # the max value given
        windowSum = 0
        while right < len(nums):
            windowSum += nums[right]
            # if windowSum >= target:
            #     min_Len = min(min_Len, right - left + 1)
            while windowSum >= target:
                min_Len = min(min_Len, right - left + 1)
                windowSum -= nums[left]
                left += 1
            right += 1
        if min_Len == 10**5 + 1:
            # still equals to the initiate value,
            # means we cannot get 1 solution
            return 0
        return min_Len


t = 7
l = [2, 3, 1, 2, 4, 3]

Solution.minSubArrayLen(Solution, t, l)


# @lc code=end
