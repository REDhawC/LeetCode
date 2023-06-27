#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arrays = []
        for i in range(numRows):
            arrays.append(list())
        print(arrays)
        if numRows == 1:
            block_Num = 1
        else:
            block_Num = numRows + (numRows - 2)
        index = 0
        while index < len(s):
            letter = s[index]
            blockIndex = index % block_Num
            rowIndex = blockIndex - numRows
            if rowIndex >= 0:
                rowIndex = -rowIndex - 2
            arrays[rowIndex].append(letter)
            index += 1
        ans = ""
        for arr in arrays:
            ans += "".join(arr)
        # print(ans)
        return ans


# Solution.convert(Solution, "A", 1)

# @lc code=end
