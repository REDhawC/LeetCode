#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rowNum = len(grid)
        colNum = len(grid[0])

        def dfs(grid, row, col):
            nonlocal rowNum, colNum
            # print("val:", grid[row][col])
            if row < 0 or row >= rowNum or col < 0 or col >= colNum:
                # print(1)
                return
            if grid[row][col] != "1":
                # print(2)
                return
            grid[row][col] = 2
            # print(grid[row][col])
            # 2 represents DFS has been to this block
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        print(rowNum, colNum)
        islandsNum = 0
        for row in range(rowNum):
            for col in range(colNum):
                # print(grid[row][col])
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    islandsNum += 1

        for row in range(rowNum):
            for col in range(colNum):
                print(grid[row][col])

        return islandsNum


# @lc code=end
