#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#


# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def solveNQueens(self, n: int) -> list[list[str]]:
        def backtrack(board, row, colLength):
            if row == colLength:  # reach the last row
                self.res.append(list())
                for row in board:
                    item = "".join(row)
                    self.res[-1].append(item)

                return
            for col in range(colLength):
                if isValid(board, row, col):
                    # print(row, col)
                    # if there is not valid col, it won't enter the next row!
                    board[row][col] = "Q"
                    backtrack(board, row + 1, colLength)
                    board[row][col] = "."

        def isValid(board, row, col):
            length = len(board)
            # col check
            for curRow in range(length):
                if board[curRow][col] == "Q":
                    return False
            # row check
            for curCol in range(length):
                if board[row][curCol] == "Q":
                    return False
            # '\' main diagonal check: left-up
            diagonalCol, diagonalRow = col - 1, row - 1
            while (0 <= diagonalCol < length) and (0 <= diagonalRow < length):
                if board[diagonalRow][diagonalCol] == "Q":
                    return False
                diagonalRow -= 1
                diagonalCol -= 1
                # if not (0 <= diagonalCol < length) or not (0 <= diagonalRow < length):
                #     break
            # '\' main diagonal check: right-down
            diagonalCol, diagonalRow = col + 1, row + 1
            while (0 <= diagonalCol < length) and (0 <= diagonalRow < length):
                if board[diagonalRow][diagonalCol] == "Q":
                    return False
                diagonalRow += 1
                diagonalCol += 1
            # '/' secondary diagonal check: right-up
            diagonalCol, diagonalRow = col + 1, row - 1
            while (0 <= diagonalCol < length) and (0 <= diagonalRow < length):
                if board[diagonalRow][diagonalCol] == "Q":
                    return False
                diagonalRow -= 1
                diagonalCol += 1
            # '/' secondary diagonal check: left-down
            diagonalCol, diagonalRow = col - 1, row + 1
            while (0 <= diagonalCol < length) and (0 <= diagonalRow < length):
                if board[diagonalRow][diagonalCol] == "Q":
                    return False
                diagonalRow += 1
                diagonalCol -= 1
            return True

        board = [["."] * n for _ in range(n)]
        # print(board)
        backtrack(board, 0, n)
        # print(self.res)
        return self.res


# s1 = Solution()
# s1.solveNQueens(4)

# @lc code=end
