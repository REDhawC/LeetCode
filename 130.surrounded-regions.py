#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc code=start
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rowNum = len(board)
        colNum = len(board[0])
        flag = 1

        def dfsSetFlag(board, row, col):
            nonlocal rowNum, colNum, flag
            # exceed border
            if row < 0 or row >= rowNum or col < 0 or col >= colNum:
                flag = 0
                return
            if board[row][col] != "O":
                return
            board[row][col] = "?"
            dfsSetFlag(board, row + 1, col)
            dfsSetFlag(board, row - 1, col)
            dfsSetFlag(board, row, col + 1)
            dfsSetFlag(board, row, col - 1)

        def dfsSetOToX(board, row, col):
            nonlocal rowNum, colNum, flag
            # exceed border
            if not (row >= 0 and row < rowNum) and not (col >= 0 and col < colNum):
                return
            if board[row][col] != "?":
                return
            board[row][col] = "X"
            dfsSetOToX(board, row + 1, col)
            dfsSetOToX(board, row - 1, col)
            dfsSetOToX(board, row, col + 1)
            dfsSetOToX(board, row, col - 1)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] == "O":
                    # print(row, col)
                    dfsSetFlag(board, row, col)
                    if flag:
                        dfsSetOToX(board, row, col)
                    else:
                        board[row][col] = "O"
                        flag = 1
                if board[row][col] == "?":
                    board[row][col] = "O"

        # for row in range(rowNum):
        #     for col in range(colNum):
        #         print(board[row][col])

        """
        Do not return anything, modify board in-place instead.
        """


# @lc code=end
