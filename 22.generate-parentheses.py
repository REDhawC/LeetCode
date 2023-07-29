#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        usage = {}
        usage["("] = n
        usage[")"] = n

        def isValid(path):  # O(N)
            stack = list()
            for i in path:
                if i == ")":
                    if len(stack) == 0:
                        return False
                    else:
                        stack.pop()
                else:  # encounter "("
                    stack.append(i)
            return len(stack) == 0

        def backtrack(path, choices):
            if "(" not in path and len(path) > 0:
                # save some time 剪枝操作的时间复杂度可以忽略!
                return
            if len(path) == n * 2 and isValid(path):
                # O(N) * O(2**(2N)) = O(2**(2N)*N) -> 2的2n次方 * n
                print(path)
                res.append(path)
                return
            for choice in choices:
                if usage[choice] != 0:
                    usage[choice] -= 1
                    backtrack(path + choice, choices)
                    usage[choice] += 1

        backtrack("", ["(", ")"])
        return res


# @lc code=end
