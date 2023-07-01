#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board) -> bool:
        hashmap_row = [[0] * 9 for i in range(9)]
        hashmap_column = [[0] * 9 for i in range(9)]
        hashmap_box = [[0] * 9 for i in range(9)]
        # init hashmaps
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    # '.' means 'Null'
                    continue
                else:
                    # convert value to int
                    curVal = int(board[row][column]) - 1
                    # use the formula below to calculate box index
                    box = column // 3 + row // 3 * 3
                    if (
                        # inside the 3 hashmap, check if the curVal already exists seperately
                        hashmap_row[row][curVal] > 0
                        or hashmap_column[column][curVal] > 0
                        or hashmap_box[box][curVal] > 0
                    ):  # place already taken
                        return False
                    # if it doesn't exist, we can add 1 to take a place.
                    hashmap_row[row][curVal] += 1
                    hashmap_column[column][curVal] += 1
                    hashmap_box[box][curVal] += 1
        return True


b = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
Solution.isValidSudoku(Solution, b)

# @lc code=end
