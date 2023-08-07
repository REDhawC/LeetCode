#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rowsNum = len(matrix)
        colsNum = len(matrix[0])
        left = 0
        right = rowsNum * colsNum - 1
        while left <= right:
            mid = (left + right) // 2
            midPos = [mid // colsNum, mid % colsNum]
            if matrix[midPos[0]][midPos[1]] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left == rowsNum * colsNum:
            return False
        return matrix[left // colsNum][left % colsNum] == target


# @lc code=end
