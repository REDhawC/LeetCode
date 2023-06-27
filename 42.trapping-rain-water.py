#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        # init leftMax
        leftMax[0] = height[0]
        # loop to make leftMax
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax[-1] = height[-1]
        # loop to make rightMax
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        # calculate the water val and add it to sum
        for i in range(1, len(height)):
            water = min(rightMax[i], leftMax[i]) - height[i]
            sum += water
        return sum


#   很精巧，但是实在太抽象了

# stack = []
# sum = 0
# current = 0
# while current < len(height):
#     while (len(stack) != 0) and (height[current] > height[stack[-1]]):
#         h = height[stack[-1]]
#         stack.pop()
#         if len(stack) == 0:
#             break
#         distance = current - stack[-1] - 1
#         minVal = min(height[stack[-1]], height[current])
#         water = (minVal - h) * distance
#         sum += water
#     stack.append(current)
#     current += 1
# return sum


# @lc code=end
