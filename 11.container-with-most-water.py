#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set up two pointers
        maxWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # calculate the space
            currentWater = min(height[left], height[right]) * (right - left)
            # find the shorter one and move it to inner place
            maxWater = max(maxWater, currentWater)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater


# @lc code=end
