#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        dpTable = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for idx, s1 in enumerate(text1):
            for c, s2 in enumerate(text2):
                if s1 == s2:
                    dpTable[idx + 1][c + 1] = dpTable[idx][c] + 1
                else:
                    dpTable[idx + 1][c + 1] = max(
                        dpTable[idx][c + 1], dpTable[idx + 1][c]
                    )

        return dpTable[length1][length2]


# @lc code=end
