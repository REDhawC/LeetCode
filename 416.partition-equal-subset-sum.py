#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#


# @lc code=start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        dpTable = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dpTable[0][0] = True

        for i, val in enumerate(nums):
            for c in range(target + 1):
                if c < val:
                    dpTable[i + 1][c] = dpTable[i][c]
                else:
                    dpTable[i + 1][c] = dpTable[i][c] or dpTable[i][c - val]

        return dpTable[len(nums)][target]


# Solution.canPartition(Solution, [1, 5, 11, 5])


# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#         from functools import lru_cache

#         memo = {}
#         totalSum = sum(nums)
#         flag = 0

#         @lru_cache(None)
#         def DP(idx, curSum):
#             nonlocal flag

#             if (idx, curSum) in memo:
#                 return memo[(idx, curSum)]
#             if idx < 0:
#                 # print(idx, curSum)
#                 if curSum == totalSum - curSum:
#                     # print("pass:", idx, curSum)
#                     flag = 1
#                 return
#             DP(idx - 1, curSum)
#             DP(idx - 1, curSum + nums[idx])
#             return

#         DP(len(nums) - 1, 0)

#         return flag


# @lc code=end
