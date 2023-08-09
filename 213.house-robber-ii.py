#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            length = len(nums)
            if length == 0:
                return 0
            if length == 1:
                return nums[0]
            # construct the first 2 digits
            dpTable = [0] * length
            dpTable[0] = nums[0]
            dpTable[1] = max(nums[0], nums[1])

            for i in range(2, length):
                dpTable[i] = max(dpTable[i - 2] + nums[i], dpTable[i - 1])

            return dpTable[length - 1]

        if len(nums) == 1:
            return nums[0]
        # seperate the cases into nums[:-1] / nums[1:]
        # throw away the first one or the last one
        return max(my_rob(nums[:-1]), my_rob(nums[1:]))

    # def rob(self, nums: list[int]) -> int:
    #     length = len(nums)
    #     if length == 1:
    #         return nums[0]
    #     dpTable = [(0, 0)] * (length)
    #     dpTable[0] = (nums[0], 1)
    #     dpTable[1] = (nums[1], 0) if nums[0] <= nums[1] else (nums[0], 1)
    #     for i in range(2, length):
    #         if i == length - 1:
    #             if dpTable[i - 2][1] == 1:
    #                 if dpTable[i - 2][0] + nums[i] - dpTable[0][0] > dpTable[i - 1][0]:
    #                     dpTable[i] = (
    #                         dpTable[i - 2][0] + nums[i] - dpTable[0][0],
    #                         dpTable[i - 2][1],
    #                     )

    #                 else:
    #                     dpTable[i] = (dpTable[i - 1][0], dpTable[i - 1][1])
    #                 break

    #         if dpTable[i - 2][0] + nums[i] > dpTable[i - 1][0]:
    #             dpTable[i] = (dpTable[i - 2][0] + nums[i], dpTable[i - 2][1])
    #         else:
    #             dpTable[i] = (dpTable[i - 1][0], dpTable[i - 1][1])
    #     return dpTable[length - 1][0]


# Solution.rob(Solution, [2, 2, 4, 3, 2, 5])
# @lc code=end
