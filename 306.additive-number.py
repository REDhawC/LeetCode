#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#


# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = False

        # if num[0] == "0":
        #     return res

        path = []

        def backtracking(idx):
            nonlocal res
            # if idx == len(num):
            # print(path)
            if len(path) > 2:
                # print("test:", path)
                flag = 1
                for i in range(2, len(path)):
                    num1, num2, num3 = (
                        float(path[i - 2]),
                        float(path[i - 1]),
                        float(path[i]),
                    )
                    if num3 != num1 + num2:
                        flag = 0
                        return

                if flag and idx == len(num):
                    # print("pass:", path)
                    res = True
                    return

            for i in range(idx, len(num)):
                curNumStr = num[idx : i + 1]
                if len(curNumStr) > 1 and curNumStr[0] == "0":
                    continue
                path.append(curNumStr)
                # print(path)
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        # print(res)
        return res


# @lc code=end
