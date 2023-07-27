#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def dfs(tempList, minNum):
            if len(tempList) == k:
                res.append(tempList.copy())
                return
            for i in range(minNum, n + 1):
                tempList.append(i)
                dfs(tempList, i + 1)
                tempList.pop()

        dfs([], 1)

        return res


# @lc code=end
