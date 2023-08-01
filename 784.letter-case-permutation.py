#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#


# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        alphaPos = []
        res = []
        path = s

        for idx in range(len(s)):
            if s[idx].isalpha():
                alphaPos.append(idx)

        maxTimes = len(alphaPos)
        print(alphaPos)

        def backtrack(times):
            nonlocal path

            if times == maxTimes:
                print(path)
                res.append(path)
                return

            pos = alphaPos[times]
            # choose upper
            Upper = path[pos].upper()
            Lower = path[pos].lower()
            path = path[:pos] + Upper + path[pos + 1 :]
            backtrack(times + 1)
            # choose lower
            path = path[:pos] + Lower + path[pos + 1 :]
            backtrack(times + 1)

        backtrack(0)

        return res


# Solution.letterCasePermutation(Solution, "a1b2")

# @lc code=end
