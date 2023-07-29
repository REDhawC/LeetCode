#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rowLength = len(board)
        colLength = len(board[0])
        wordLength = len(word)
        visited = [[False] * colLength for row in range(rowLength)]
        found = False

        if wordLength > rowLength * colLength:
            return False

        def backtrack(pos, path, idx):
            nonlocal found

            if found:
                return

            if len(path) == wordLength:
                if path == word:
                    # if path.upper() == word or path.lower() == word or path == word:
                    # print(pos, path)
                    found = True
                    return

            row = pos[0]
            col = pos[1]
            for choice in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if not (0 <= choice[0] < rowLength and 0 <= choice[1] < colLength):
                    continue

                if not visited[choice[0]][choice[1]]:
                    if idx + 1 < wordLength:
                        if board[choice[0]][choice[1]] == word[idx + 1]:
                            visited[choice[0]][choice[1]] = True
                            backtrack(
                                choice, path + board[choice[0]][choice[1]], idx + 1
                            )
                            visited[choice[0]][choice[1]] = False

        for row in range(rowLength):
            for col in range(colLength):
                if board[row][col] == word[0]:
                    visited[row][col] = True
                    backtrack((row, col), word[0], 0)
                    visited[row][col] = False

        return found


# @lc code=end
