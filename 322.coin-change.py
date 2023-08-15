#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if len(coins) == 1 and amount % coins[0] != 0:
            return -1

        dpTable = [[float("inf")] * (amount + 1) for _ in range(len(coins) + 1)]
        dpTable[0][0] = 0  # when i=0 c=0, ans=0
        for coinIdx, coinVal in enumerate(coins):
            for totalVal in range(amount + 1):
                newCapacity = totalVal - coinVal
                if newCapacity < 0:
                    dpTable[coinIdx + 1][totalVal] = dpTable[coinIdx][totalVal]
                else:
                    dpTable[coinIdx + 1][totalVal] = min(
                        dpTable[coinIdx][totalVal],
                        dpTable[coinIdx + 1][newCapacity] + 1,
                    )

        if dpTable[len(coins)][amount] == float("inf"):
            return -1
        return dpTable[len(coins)][amount]


# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         dpTable = [float("inf") for _ in range(amount + 1)]
#         dpTable[0] = 0
#         for totalVal in range(1, amount + 1):
#             for coinVal in coins:
#                 son = totalVal - coinVal
#                 if son < 0:
#                     continue
#                 dpTable[totalVal] = min(dpTable[totalVal], 1 + dpTable[son])

#         if dpTable[amount] == float("inf"):
#             return -1
#         return dpTable[amount]


# @lc code=end
