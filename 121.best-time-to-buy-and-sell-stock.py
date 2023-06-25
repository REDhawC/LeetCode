#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 10**4 + 1
        for i in prices:
            maxProfit = max(maxProfit, i - minPrice)
            # new price - former minPrice,
            # prevent old high price - new low price[impossible]
            minPrice = min(i, minPrice)
            # minPrice是历史最低点,局部最低,解决了时间的逻辑问题

        return maxProfit


# @lc code=end
