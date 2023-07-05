#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        def simpleCalculate(exp):
            exp = exp.split(" ")[1:]
            numStack = []
            operators = []
            for i in exp:
                if i in "+-":
                    operators.append(i)
                else:
                    if len(numStack) == 0:
                        numStack.append(i)
                    else:
                        secondNum = i
                        firstNum = numStack.pop()
                        operator = operators.pop()
                        if operator == "+":
                            result = int(firstNum) + int(secondNum)
                            numStack.append(str(result))
                        else:
                            result = int(firstNum) - int(secondNum)
                            numStack.append(str(result))
            return numStack[0]

        s = "(" + s + ")"
        stack = []
        exp = ""
        for i in s:
            if i == " ":
                continue
            elif i != ")":
                stack.append(i)
            else:
                curVal = stack.pop()
                while curVal != "(":
                    exp = f" {curVal}{exp}"
                    curVal = stack.pop()
                stack.append(simpleCalculate(exp))
                exp = ""
        return int(stack[0])


# s = "(1+(4+5+2)-3)+(6+8)"

# Solution.calculate(Solution, s)


# @lc code=end
