#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start
# class Solution:
#     def findTargetSumWays(self, nums: list[int], target: int) -> int:
#         from functools import lru_cache

#         numsSum = sum(nums)
#         newTarget = numsSum + target
#         if newTarget < 0 or (numsSum + target) % 2 != 0:
#             return 0
#         newTarget = newTarget // 2
#         length = len(nums)

#         @lru_cache(None)
#         def dfs(idx, capacity):
#             if idx < 0:
#                 if capacity == 0:
#                     return 1
#                 else:
#                     return 0

#             if capacity < nums[idx]:
#                 return dfs(idx - 1, capacity)
#             else:
#                 return dfs(idx - 1, capacity) + dfs(idx - 1, capacity - nums[idx])

#         return dfs(length - 1, newTarget)


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        length = len(nums) - 1
        target = target + sum(nums)
        if target % 2 != 0 or target < 0:
            return 0
        newTarget = target // 2

        def dp(idx, capacity):
            if (idx, capacity) in memo:
                return memo[(idx, capacity)]
            if idx < 0:
                if capacity <= 0:
                    return 1
            else:
                return 0
            # if nums[idx] > capacity:
            #     memo[(idx, capacity)] = dp(idx - 1, capacity)
            #     return memo[(idx, capacity)]
            # else:
            memo[(idx, capacity)] = dp(idx - 1, capacity) + dp(
                idx - 1, capacity - nums[idx]
            )
            return memo[(idx, capacity)]

        return dp(length, newTarget)


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # 输出结果

# @lc code=end
