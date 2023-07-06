#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#


# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        def simpleCalculate(exp):
            numStack = []
            operators = []
            if exp[0] in "+-":
                # add 0 when having less than 2 nums to prevent bug
                numStack = [0]
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
                        else:
                            result = int(firstNum) - int(secondNum)
                        numStack.append(str(result))
            if len(numStack) != 0 and len(operators) != 0:
                return operators[0] + numStack[0]
            return numStack[0]

        if "-" not in s and "+" not in s:
            if "(" in s and ")" in s:
                s = s.replace("(", "")
                s = s.replace(")", "")
            return int(s)
        s = "(" + s + ")"
        stack = []
        exp = []
        num = ""
        for i in s:
            if i == " ":
                continue
            elif i == "(":
                stack.append(i)
            elif i.isdigit():
                num += i
            # make sure we don't miss 2 or more digits-number
            else:  # encounter ')'
                stack.append(num)
                num = ""
                if i == "+" or i == "-":
                    stack.append(i)
                else:
                    curVal = stack.pop()
                    while curVal != "(":
                        # if we meet '(', this calculate section is ending.
                        exp.insert(0, curVal)
                        curVal = stack.pop()
                    # pass the exp to the inner cal func.
                    stack.append(simpleCalculate(exp))
                    exp = []
        return int(stack[0])


s = "1-11"

Solution.calculate(Solution, s)


# @lc code=end
