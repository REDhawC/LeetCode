#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#


# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        length1 = len(s1)
        length2 = len(s2)
        dpTable = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(1, length1 + 1):
            dpTable[i][0] = dpTable[i - 1][0] + ord(s1[i - 1])
        for j in range(1, length2 + 1):
            dpTable[0][j] = dpTable[0][j - 1] + ord(s2[j - 1])

        # print(dpTable)

        for idx1, char1 in enumerate(s1):
            for idx2, char2 in enumerate(s2):
                if char1 == char2:
                    dpTable[idx1 + 1][idx2 + 1] = dpTable[idx1][idx2]
                else:
                    dpTable[idx1 + 1][idx2 + 1] = min(
                        dpTable[idx1][idx2 + 1] + ord(char1),
                        dpTable[idx1 + 1][idx2] + ord(char2),
                    )

        return dpTable[length1][length2]


# @lc code=end
