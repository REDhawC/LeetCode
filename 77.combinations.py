#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        tempList = []

        def dfs(minNum):
            remainingNum = k - len(tempList)
            if n + 1 - minNum < remainingNum:
                # if remaining options cannot fulfill,
                return
            if len(tempList) == k:
                # having enough digits, stop iteration.
                res.append(tempList.copy())
                return
            for i in range(minNum, n + 1):  # decreasing
                tempList.append(i)
                # print(tempList)
                dfs(i + 1)
                tempList.pop()

        dfs(1)

        return res


# class Solution:
#     def combine(self, n: int, k: int) -> list[list[int]]:
#         res = []
#         tempList = []

#         def dfs(maxNum):
#             remainingNum = k - len(tempList)
#             if maxNum < remainingNum:
#                 return
#             if len(tempList) == k:
#                 res.append(tempList.copy())
#                 return
#             for i in range(maxNum, 0, -1):  # decreasing
#                 tempList.append(i)
#                 dfs(i - 1)
#                 tempList.pop()

#         dfs(n)

#         return res


# @lc code=end
