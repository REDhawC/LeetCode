#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            n = str(n)
            sum = 0
            for i in n:
                sum += int(i) ** 2
            return sum

        slow, fast = n, getNext(getNext(n))
        while slow != fast and fast != 1:
            slow = getNext(slow)
            fast = getNext(getNext(fast))  # one step faster
        return fast == 1

    # #method1: using set to save sums
    # def isHappy(self, n: int) -> bool:
    #     savedNums = set()
    #     while True:
    #         sum = 0
    #         happyList = list(str(n))
    #         for i in happyList:
    #             sum += int(i) ** 2
    #         if sum in savedNums:
    #             return False
    #         if sum == 1:
    #             return True
    #         n = sum
    #         savedNums.add(sum)


strs = 19
Solution.isHappy(Solution, strs)

# @lc code=end
