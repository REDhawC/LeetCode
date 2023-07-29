#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def isValid(s):
            fast = 0
            slow = len(s) - 1
            while fast <= slow:
                if s[fast] != s[slow]:
                    return False
                fast += 1
                slow -= 1
            return True

        def backtrack(s, subStrs):
            print(subStrs)
            if subStrs:
                for sub in subStrs:
                    if not isValid(sub):
                        return
                res.append(subStrs)

            for subIdx in range(len(subStrs)):
                for idx in range(len(sub) - 1):
                    newSubStrs = (
                        subStrs[:subIdx]
                        + [sub[:idx]]
                        + [sub[idx:]]
                        + subStrs[subIdx + 1 :]
                    )
                    print(newSubStrs)
                    backtrack(s, newSubStrs)

        backtrack(s, [s])


# @lc code=end
