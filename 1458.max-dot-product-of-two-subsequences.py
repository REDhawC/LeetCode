#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#


# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)
        dpTable = [[float("-inf")] * (length2 + 1) for _ in range(length1 + 1)]

        for i, num_i in enumerate(nums1):
            for j, num_j in enumerate(nums2):
                curDotProduct = num_i * num_j
                dpTable[i + 1][j + 1] = max(
                    dpTable[i][j + 1],
                    dpTable[i + 1][j],
                    curDotProduct,  # 当dpTable[i][j]为负数的时候，直接加上目前的点差
                    dpTable[i][j] + curDotProduct,
                    dpTable[i][j],
                )

        ans = dpTable[length1][length2]
        return ans


# @lc code=end
