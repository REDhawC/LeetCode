#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers, target):
        ans = [0] * 2
        slow, fast = 0, len(numbers) - 1
        while slow < fast:
            if numbers[slow] + numbers[fast] < target:
                # it means slow is to small, wo should increase it
                slow += 1
            elif numbers[slow] + numbers[fast] == target:
                # get the target
                ans[0], ans[1] = slow + 1, fast + 1
                return ans
            else:
                # it means fast is to big, we should reduce it.
                fast -= 1


# nums = [2, 3, 4]
# tar = 6

# Solution.twoSum(Solution, nums, tar)
# @lc code=end
