#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dpTable = [float("inf") for _ in range(amount + 1)]
        dpTable[0] = 0
        for totalVal in range(1, amount + 1):
            for coinVal in coins:
                son = totalVal - coinVal
                if son < 0:
                    continue
                dpTable[totalVal] = min(dpTable[totalVal], 1 + dpTable[son])

        if dpTable[amount] == float("inf"):
            return -1
        return dpTable[amount]


# @lc code=end
