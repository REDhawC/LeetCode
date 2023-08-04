#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        path = []
        res = []

        def backtracking(maxNum, distance):
            remainingNum = k - len(path)
            if (
                distance < 0  # impossible Case1: exceed target
                or distance - (maxNum + maxNum - remainingNum + 1) * remainingNum / 2
                > 0  # impossible Case2: the largest sum cannot reach target,
                # 通过等差数列求和算出最大的一组数进行比较
            ):
                return
            if len(path) == k:
                if distance == 0:
                    res.append(path.copy())
                return

            for i in range(maxNum, 0, -1):
                path.append(i)
                # print(path)
                backtracking(i - 1, distance - i)
                path.pop()

        backtracking(9, n)

        return res


# @lc code=end
