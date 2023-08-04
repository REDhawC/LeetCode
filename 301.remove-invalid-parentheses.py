#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        path = s
        res = set()
        maxLength = -1
        length = len(s)

        def isValid(path):
            stack = []
            for i in path:
                if i == "(":
                    stack.append(i)
                if i == ")":
                    if len(stack) == 0:
                        return False
                    stack.pop()
            if len(stack) == 0:
                return True

        def backtracking(idx):
            nonlocal path, maxLength
            if len(path) < maxLength:
                return
            if isValid(path):
                if len(path) < maxLength:
                    return
                maxLength = max(maxLength, len(path))
                res.add(path)
                return

            for i in range(idx, length):
                if not s[i].isalpha():
                    temp = path
                    path = s[:i] + s[i + 1 :]
                    backtracking(i + 1)
                    path = temp

        backtracking(0)
        return list(res)


Solution.removeInvalidParentheses(Solution, ")(")


# @lc code=end
