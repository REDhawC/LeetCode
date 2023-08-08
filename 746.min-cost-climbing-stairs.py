#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc code=start
# class Solution:
#     def minCostClimbingStairs(self, cost: list[int]) -> int:
#         cost.append(0)
#         globalMinCost = 10**6
#         length = len(cost)
#         costHashmap = [-1] * (length)

#         def dfs(step, curCost):
#             nonlocal globalMinCost
#             if step > length - 1:
#                 return
#             if step == length - 1:
#                 globalMinCost = min(curCost, globalMinCost)
#                 return curCost
#             if costHashmap[step] != -1:
#                 if curCost > costHashmap[step]:
#                     return 10**6
#             cost_Path1, cost_path2 = 10**6, 10**6
#             if step + 2 <= length - 1:
#                 cost_path2 = dfs(step + 2, curCost + cost[step + 2])

#             if step + 1 <= length - 1:
#                 cost_Path1 = dfs(step + 1, curCost + cost[step + 1])

#             curMinCost = min(cost_Path1, cost_path2)
#             costHashmap[step] = curMinCost
#             return curMinCost

#         dfs(-1, 0)
#         return globalMinCost


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dpTable = [0] * (len(cost) + 2)
        for step in range(2, len(cost) + 1):
            path1 = dpTable[step - 1] + cost[step - 1]
            path2 = dpTable[step - 2] + cost[step - 2]
            dpTable[step] = min(path1, path2)
        return dpTable[len(cost)]

        # length = len(cost)
        # dp = [0] * length

        # # Base cases
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # # Compute the minimum cost for each step
        # for i in range(2, length):
        #     dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        # # Return the minimum cost to reach the top
        # return min(dp[length - 1], dp[length - 2])


# Solution.minCostClimbingStairs(Solution, [10, 15, 20])

# @lc code=end
