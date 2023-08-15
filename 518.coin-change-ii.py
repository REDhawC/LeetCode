#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        length = len(coins)
        dpTable = [[0] * (amount + 1) for _ in range(length + 1)]
        dpTable[0][0] = 1
        for idx, val in enumerate(coins):
            for c in range(amount + 1):
                if val > c:
                    dpTable[idx + 1][c] = dpTable[idx][c]
                else:
                    dpTable[idx + 1][c] = dpTable[idx][c] + dpTable[idx + 1][c - val]

        return dpTable[length][amount]


# @lc code=end
