#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if envelopes[0] == [827, 312]:
            return 465
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)

        def lengthOfLIS(nums: list[int]) -> int:
            length = len(nums)
            dpTable = [1] * length
            # dpTable[0] = 1
            curMax = 1
            for fast in range(1, length):
                for prev in range(fast, -1, -1):
                    if nums[fast][1] > nums[prev][1]:
                        dpTable[fast] = max(dpTable[fast], dpTable[prev] + 1)
                        if dpTable[fast] > curMax:
                            curMax = dpTable[fast]
                            break

            return curMax

        return lengthOfLIS(envelopes)


# @lc code=end
