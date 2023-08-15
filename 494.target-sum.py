#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        newTarget = target + sum(nums)
        if newTarget % 2 != 0 or newTarget < 0:
            return 0
        newTarget = newTarget // 2
        length = len(nums)
        dpTable = [[0] * (newTarget + 1) for _ in range(length + 1)]
        dpTable[0][0] = 1
        for i, val in enumerate(nums):
            for c in range(newTarget + 1):
                if val > c:
                    dpTable[i + 1][c] = dpTable[i][c]
                else:
                    dpTable[i + 1][c] = dpTable[i][c] + dpTable[i][c - val]

        return dpTable[length][newTarget]


# class Solution:
#     def findTargetSumWays(self, nums: list[int], target: int) -> int:
#         # from functools import lru_cache
#         memo = {}
#         length = len(nums) - 1

#         # @lru_cache(None)
#         def DP(idx, curSum):
#             if (idx, curSum) in memo:
#                 return memo[(idx, curSum)]
#             if idx < 0:
#                 if curSum == target:
#                     return 1
#                 else:
#                     return 0
#             positive = DP(idx - 1, curSum + nums[idx])
#             negative = DP(idx - 1, curSum - nums[idx])
#             memo[(idx, curSum)] = positive + negative
#             return memo[(idx, curSum)]

#         return DP(length, 0)


# @lc code=end
