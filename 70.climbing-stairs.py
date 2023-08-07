#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        def backtracking(step, pathNum):
            nonlocal res
            if step > n:
                return 0
            if step == n:
                res += 1
                return 1
            temp = pathNum
            if step + 1 <= n:
                pathNum += backtracking(step + 1, pathNum)
                print(pathNum)
                pathNum = temp
            if step + 2 <= n:
                pathNum += backtracking(step + 2, pathNum)
                print(pathNum)

        backtracking(0, 0)
        return res


Solution.climbStairs(Solution, 3)


# @lc code=end
