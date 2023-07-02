#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for row in range(size):
            for col in range(row):
                # swap catercorner items
                # formula: n'th row swap the first n-1 items
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        import math

        for row in matrix:
            # row hrizontally reverse order
            for i in range(math.ceil(len(row) / 2)):
                row[i], row[-(i + 1)] = row[-(i + 1)], row[i]
            # row.reverse()


# m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# Solution.rotate(Solution, m)
# print(m)


# @lc code=end
