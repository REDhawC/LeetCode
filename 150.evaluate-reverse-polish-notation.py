#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        import math

        stack = []
        for i in tokens:
            if i in "+-*/":
                secondNum = stack.pop()
                firstNum = stack.pop()
                result = eval(firstNum + i + secondNum)
                if i == "/":
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                stack.append(str(result))
            else:
                stack.append(i)
        return int(stack[0])


# s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Solution.evalRPN(Solution, s)

# @lc code=end
