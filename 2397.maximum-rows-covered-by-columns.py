#
# @lc app=leetcode id=2397 lang=python3
#
# [2397] Maximum Rows Covered by Columns
#


# @lc code=start
class Solution:
    def maximumRows(self, matrix: list[list[int]], numSelect: int) -> int:
        # if numSelect == 1:
        #     return len(matrix)

        rowNum = len(matrix)
        colNum = len(matrix[0])

        maxRow = 0

        def backtracking(idx, selectPath):
            nonlocal maxRow

            if idx == colNum:
                if len(selectPath) == numSelect:
                    curRow = 0
                    for row in range(rowNum):
                        flag = 1
                        for col in range(colNum):
                            if matrix[row][col] == 1 and col not in selectPath:
                                flag = 0
                        curRow += flag == 1

                    if curRow > maxRow:
                        maxRow = max(curRow, maxRow)
                return

            selectPath.append(idx)
            backtracking(idx + 1, selectPath)
            selectPath.pop()

            backtracking(idx + 1, selectPath)

        backtracking(0, [])
        return maxRow


# Solution.maximumRows(Solution, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2)

# @lc code=end
