#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#


# @lc code=start


# class Solution:
#     def numSquares(self, n: int) -> int:
#         import math

#         dpTable = [[float("inf")] * (n + 1) for _ in range(n + 1)]
#         dpTable[0][0] = 0

#         for i in range(1, int(math.sqrt(n)) + 1):
#             square = i * i
#             for j in range(n + 1):
#                 if square > j:
#                     dpTable[i][j] = dpTable[i - 1][j]
#                 else:
#                     dpTable[i][j] = min(dpTable[i - 1][j], dpTable[i][j - square] + 1)

#         return dpTable[int(math.sqrt(n))][n]


class Solution:
    def numSquares(self, n: int) -> int:
        m = int(n**0.5)
        perfectNums = [ch**2 for ch in range(1, m + 1)]
        dpTable = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dpTable[0][0] = 0

        for i, val in enumerate(perfectNums):
            for c in range(n + 1):
                if val > c:
                    dpTable[i + 1][c] = dpTable[i][c]
                else:
                    dpTable[i + 1][c] = min(dpTable[i][c], dpTable[i + 1][c - val] + 1)

        return dpTable[m][n] if dpTable[m][n] != float("inf") else -1


Solution.numSquares(Solution, 12)

# @lc code=end
