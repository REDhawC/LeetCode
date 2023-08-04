#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#


# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishmentNums = set()

        def backtracking(idx):
            nonlocal baseNum, strSquare, path, flag
            if idx == len(strSquare):
                # print("test:", path)
                sum_Check = 0
                for numStr in path:
                    num = int(numStr)
                    sum_Check += num
                if sum_Check == int(baseNum):
                    # print("pass:", strSquare, path)
                    flag = 0
                    punishmentNums.add(int(strSquare))
                    return

            for i in range(idx, len(strSquare)):
                if flag:
                    curStr = strSquare[idx : i + 1]
                    if curStr[0] == "0" and len(curStr) > 1:
                        continue
                    path.append(curStr)
                    # print(baseNum, path)
                    backtracking(i + 1)
                    path.pop()

        for i in range(1, n + 1):
            flag = 1
            baseNum = i
            strSquare = str(i**2)
            path = []
            backtracking(0)

        sumList = list(punishmentNums)
        return sum(sumList)


Solution.punishmentNumber(Solution, 91)

# @lc code=end
