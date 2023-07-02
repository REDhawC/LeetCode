#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        _0_col_index = []
        _0_row_index = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                curVal = matrix[row][col]
                if curVal == 0:
                    # mark 0 cols and rows
                    if not col in _0_col_index:
                        _0_col_index.append(col)
                    if not row in _0_row_index:
                        _0_row_index.append(row)
            if len(_0_col_index) == len(matrix[0]):
                # if the 0 cols are already full , break to save time
                break

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # set the recorded rows and cols  to 0
                if col in _0_col_index:
                    matrix[row][col] = 0
                if row in _0_row_index:
                    matrix[row] = [0] * len(matrix[0])


# @lc code=end
