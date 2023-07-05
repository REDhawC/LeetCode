#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        ans = ""
        stack = []
        for i in path:
            if i == "":
                continue
            elif not i.count(".") == len(i) or (i.count(".") == len(i) and len(i) > 2):
                # elif (i.count(".") > 0 and len(i) > 2) or i.count(".") == 0:
                stack.append("/" + i)
            elif i == "..":
                if len(stack) != 0:
                    stack.pop()
        if len(stack) == 0:
            stack.append("/")
        ans = "".join(stack)
        print(ans)
        return ans


# s = "/home//foo/"
# Solution.simplifyPath(Solution, s)


# @lc code=end
