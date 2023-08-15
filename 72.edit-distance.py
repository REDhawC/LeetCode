#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        dpTable = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        dpTable[0] = list(range(length2 + 1))
        # when one of the text is '',
        # the distance is the length of the other text.
        for i in range(length1 + 1):
            dpTable[i][0] = i
        for idx1, s1 in enumerate(word1):
            for idx2, s2 in enumerate(word2):
                if s1 == s2:
                    dpTable[idx1 + 1][idx2 + 1] = dpTable[idx1][idx2]
                else:
                    dpTable[idx1 + 1][idx2 + 1] = (
                        min(
                            dpTable[idx1 + 1][idx2],
                            dpTable[idx1][idx2 + 1],
                            dpTable[idx1][idx2],
                        )
                        + 1  # operation num +1
                    )
        return dpTable[length1][length2]


# @lc code=end
