#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length = len(nums)
        dpTable = [1] * length
        # dpTable[0] = 1
        curMax = 1
        for fast in range(1, length):
            for prev in range(fast, -1, -1):
                if nums[fast] > nums[prev]:
                    dpTable[fast] = max(dpTable[fast], dpTable[prev] + 1)
                    if dpTable[fast] > curMax:
                        curMax = dpTable[fast]
                        break

        return curMax


# Solution.lengthOfLIS(Solution, [10, 9, 2, 5, 3, 7, 101, 18])

# @lc code=end
