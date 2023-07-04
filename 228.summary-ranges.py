#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        index = 0
        while index < len(nums):
            start = nums[index]
            end = nums[index]
            temp = [start, end]
            while index != len(nums) - 1 and nums[index + 1] == nums[index] + 1:
                index += 1
            temp[1] = nums[index]
            ans.append(temp)
            index += 1

        index = 0
        while index < len(ans):
            if ans[index][0] != ans[index][1]:
                ans[index] = f"{ans[index][0]}->{ans[index][1]}"
            else:
                ans[index] = f"{ans[index][0]}"
            index += 1
        return ans


m = [0, 1, 2, 4, 5, 7]
Solution.summaryRanges(Solution, m)

# @lc code=end
