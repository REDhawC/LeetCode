#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        index = 0
        ans = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                # the smallest = the start num of a sequence
                curInt = num
                next = curInt + 1
                count = 1
                while next in nums:
                    count += 1
                    next += 1
                ans = max(count, ans)
            index += 1
        return ans


# Solution.longestConsecutive(Solution, m)
# @lc code=end
