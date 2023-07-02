#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#


# @lc code=start
class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy

        # set up a temp board with boarders
        tempBoard = copy.deepcopy(board)
        rowNum = len(board)
        colNum = len(board[0])
        for row in range(rowNum):
            tempBoard[row].insert(0, "x")
            tempBoard[row].append("x")
        tempBoard.append(["x"] * (colNum + 2))
        tempBoard.insert(0, ["x"] * (colNum + 2))
        # print(tempBoard)

        def checkNeighborsAndGetNext(row, col):
            curVal = tempBoard[row][col]
            neighbors = []
            # search for neighbors
            neighbors.append(tempBoard[row - 1][col - 1])
            neighbors.append(tempBoard[row - 1][col])
            neighbors.append(tempBoard[row - 1][col + 1])
            neighbors.append(tempBoard[row][col - 1])
            neighbors.append(tempBoard[row][col + 1])
            neighbors.append(tempBoard[row + 1][col - 1])
            neighbors.append(tempBoard[row + 1][col])
            neighbors.append(tempBoard[row + 1][col + 1])
            count = 0
            for neighbor in neighbors:
                # sum up the 1s
                if neighbor == 1:
                    count += 1
            if curVal == 1:
                if count == 2 or count == 3:
                    return 1
                else:
                    return 0
            else:  # curVal==0
                if count == 3:
                    return 1
                else:
                    return 0

        # start updating
        for row in range(1, rowNum + 1):
            for col in range(1, colNum + 1):
                board[row - 1][col - 1] = checkNeighborsAndGetNext(row, col)

        # print(board)


# b = [[1, 1], [1, 0]]
# Solution.gameOfLife(Solution, b)


# @lc code=end
