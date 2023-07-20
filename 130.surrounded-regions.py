#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc code=start


# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board:
#             return

#         n, m = len(board), len(board[0])

#         def dfs(x, y):
#             if not 0 <= x < n or not 0 <= y < m or board[x][y] != "O":
#                 return

#             board[x][y] = "A"
#             dfs(x + 1, y)
#             dfs(x - 1, y)
#             dfs(x, y + 1)
#             dfs(x, y - 1)

#         for i in range(n):
#             dfs(i, 0)
#             dfs(i, m - 1)

#         for i in range(m - 1):
#             dfs(0, i)
#             dfs(n - 1, i)

#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] == "A":
#                     board[i][j] = "O"
#                 elif board[i][j] == "O":
#                     board[i][j] = "X"


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rowNum = len(board)
        colNum = len(board[0])

        def dfs(board, row, col):
            nonlocal rowNum, colNum
            # exceed border
            if row < 0 or row >= rowNum or col < 0 or col >= colNum:
                return
            if board[row][col] != "O":
                return
            board[row][col] = "?"
            dfs(board, row + 1, col)
            dfs(board, row - 1, col)
            dfs(board, row, col + 1)
            dfs(board, row, col - 1)

        # check the border of board and find out all the linked 'O's
        for row in range(rowNum):
            dfs(board, row, 0)
            dfs(board, row, colNum - 1)

        for col in range(1, colNum - 1):
            dfs(board, 0, col)
            dfs(board, rowNum - 1, col)

        # print(board)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] == "?":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

        # for row in range(rowNum):
        #     for col in range(colNum):
        #         print(board[row][col])

        """
        Do not return anything, modify board in-place instead.
        """


# @lc code=end
