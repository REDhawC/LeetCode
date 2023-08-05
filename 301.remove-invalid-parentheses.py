#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        from collections import deque

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

        queue = deque()
        visited = set()
        path = s
        res = list()
        queue.append(s)
        step = 0
        flag = 1
        while queue and flag:
            step += 1
            size = len(queue)
            for item in range(size):
                curStr = queue.popleft()
                if isValid(curStr):
                    res.append(curStr)
                    break
                for i in range(len(curStr)):
                    if not curStr[i].isalpha():
                        path = curStr[:i] + curStr[i + 1 :]
                        if path not in visited:
                            visited.add(path)
                            queue.append(path)
                            if isValid(path):
                                flag = 0
                                res.append(path)
        return res

        # def backtracking(idx):
        #     nonlocal path, maxLength
        #     if len(path) < maxLength:
        #         return
        #     if isValid(path):
        #         if len(path) < maxLength:
        #             return
        #         maxLength = max(maxLength, len(path))
        #         res.add(path)
        #         print("pass:", len(path), path)
        #         return

        #     i = 0
        #     while i < len(path):
        #         # print(path)
        #         if not path[i].isalpha():
        #             temp = path
        #             path = path[:i] + path[i + 1 :]
        #             print(i, ":", path)
        #             backtracking(i + 1)
        #             path = temp
        #         i += 1
        #     # for i in range(idx, length):
        #     #     if not s[i].isalpha():
        #     #         temp = path
        #     #         path = s[:i] + s[i + 1 :]
        #     #         backtracking(i + 1)
        #     #         path = temp

        # backtracking(0)
        # return list(res)


# Solution.removeInvalidParentheses(Solution, ")(")


# @lc code=end
