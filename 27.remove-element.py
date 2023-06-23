#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
# 提交方式很诡异, 要求在原位处理nums列表,把非val数都放到列表的前面slow个里面,
# 或者把非val数全部移除
# return的是非val数的数量.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        return slow

    # 72;29

    # def removeElement(self, nums, val: int) -> int:
    #     count = 0
    #     lenNums = len(nums)
    #     while val in nums:
    #         count += 1
    #         nums.remove(val)
    #     return lenNums - count
    # 76;29


# @lc code=end
