#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        visited = length * [-1]

        def dfs(idx):
            if idx > length - 1:
                return 0
            if visited[idx] != -1:
                return visited[idx]
            res = max(dfs(idx + 1), dfs(idx + 2) + nums[idx])
            visited[idx] = res
            return res

        return dfs(0)


# @lc code=end
