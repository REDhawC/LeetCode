#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
class Solution:
    # 画线图分析可知,抓住所有的上升波段即可
    def maxProfit(self, prices: List[int]) -> int:
        # buy today and sell tomorraw
        # at all rising periods
        profit = 0
        for day in range(len(prices) - 1):
            if prices[day] < prices[day + 1]:
                profit += prices[day + 1] - prices[day]
        return profit


# @lc code=end
