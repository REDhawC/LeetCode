#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        farestIndex = 0
        if len(nums) == 1:
            return True
        while index < len(nums) - 1:
            farestIndex = max(farestIndex, nums[index] + index)
            # print(farestIndex)
            if farestIndex <= index:
                return False
            if farestIndex >= len(nums) - 1:
                return True
            index += 1
        return False


# @lc code=end
