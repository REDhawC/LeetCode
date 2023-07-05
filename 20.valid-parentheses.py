#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "{": "}", "[": "]"}
        stack = []
        if len(s) % 2 == 1:
            return False
        for index in range(len(s)):
            if s[index] in hashmap:
                stack.append(s[index])
            else:
                if len(stack) == 0:
                    return False
                if hashmap[stack[-1]] != s[index]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


s = "()"
Solution.isValid(Solution, s)


# @lc code=end
