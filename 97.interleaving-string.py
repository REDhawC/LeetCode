#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        idx1, idx2 = 0, 0
        length1, length2 = len(s1), len(s2)
        flag = True

        def backTracking(i):
            if i > len(s3):
                flag = True
                return
            curChar = s3[i]
            curS1 = s1[idx1] if idx1 < length1 else ""
            curS2 = s2[idx2] if idx2 < length2 else ""
            if curS1 == curChar and idx1 < length1:
                print("1:", curS1, idx1)
                idx1 += 1
            elif curS2 == curChar and idx2 < length2:
                print("2:", curS2, idx2)
                idx2 += 1

        return flag


# @lc code=end
