#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # matrix
        L, R, answer = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        L[0] = 1
        R[-1] = 1
        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            answer[i] = L[i] * R[i]
        # print(L, R, answer)
        return answer


# @lc code=end
