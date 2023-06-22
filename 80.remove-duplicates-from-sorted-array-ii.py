#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 2
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                nums.remove(nums[slow])
            else:
                slow += 1
                fast += 1
        return len(nums)
        # dic1 = {}
        # for i in nums:
        #     if i in dic1.keys():
        #         dic1[i] += 1
        #     else:
        #         dic1[i] = 1
        # for k in dic1:
        #     while dic1[k] > 2:
        #         nums.remove(k)
        #         dic1[k] -= 1
        # return len(nums)


# @lc code=end
