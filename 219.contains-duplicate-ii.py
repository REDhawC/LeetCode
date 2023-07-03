#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        hashmap = {}
        for index in range(len(nums)):
            curVal = nums[index]
            if curVal not in hashmap:
                hashmap[curVal] = index
            else:
                if abs(index - hashmap[curVal]) <= k:
                    return True
                else:
                    hashmap[curVal] = index
        return False


# nums = [1, 2, 3, 1]
# k = 3
# Solution.containsNearbyDuplicate(Solution, nums, k)
# @lc code=end
