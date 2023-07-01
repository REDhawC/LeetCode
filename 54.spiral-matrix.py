#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        hashmap = [[0] * (colNum + 2) for i in range(rowNum)]
        # init hashmap to save inaccessible locations
        hashmap.insert(0, [1] * (colNum + 2))
        hashmap.append([1] * (colNum + 2))
        for i in range(len(hashmap)):
            hashmap[i][0], hashmap[i][-1] = 1, 1
        # set the boarder as inaccessible -> 1
        ans = []
        row = 1
        col = 1
        direction = "right"
        flag = (
            hashmap[row - 1][col] != 1
            or hashmap[row + 1][col] != 1
            or hashmap[row][col + 1] != 1
            or hashmap[row][col - 1] != 1
        )
        # if 1 of the 4 directions is accessible, we can keep going.
        if not flag and len(matrix[0]) == 1:
            return matrix[0]
        # special case as [[1]]
        while flag:
            matrixRow = row - 1
            matrixCol = col - 1
            ans.append(matrix[matrixRow][matrixCol])
            hashmap[row][col] = 1
            # check if the next location is accessible
            flag = (
                hashmap[row - 1][col] != 1
                or hashmap[row + 1][col] != 1
                or hashmap[row][col + 1] != 1
                or hashmap[row][col - 1] != 1
            )
            if flag:
                if direction == "right":
                    if hashmap[row][col + 1] == 1:
                        direction = "down"
                    else:
                        col += 1
                if direction == "down":
                    if hashmap[row + 1][col] == 1:
                        direction = "left"
                    else:
                        row += 1
                if direction == "left":
                    if hashmap[row][col - 1] == 1:
                        direction = "up"
                    else:
                        col -= 1
                if direction == "up":
                    if hashmap[row - 1][col] == 1:
                        direction = "right"
                        col += 1
                        # remember to col+=1 here
                    else:
                        row -= 1
        # print(ans)
        return ans


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Solution.spiralOrder(Solution, matrix)


# @lc code=end
