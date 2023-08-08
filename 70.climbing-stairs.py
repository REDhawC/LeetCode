#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        pathNums = [-1] * (n + 1)

        def backtracking(step, pathNum):
            nonlocal res
            if step > n:
                return 0
            if step == n:
                res += 1
                return 1

            if pathNums[step] != -1:
                res += pathNums[step]
                return pathNums[step]

            path1, path2 = 0, 0
            if step + 1 <= n:
                path1 = backtracking(step + 1, pathNum)
            if step + 2 <= n:
                path2 = backtracking(step + 2, pathNum)
            pathNum = path1 + path2

            pathNums[step] = pathNum
            return pathNum

        backtracking(0, 0)
        return res


# Solution.climbStairs(Solution, 4)


# @lc code=end
