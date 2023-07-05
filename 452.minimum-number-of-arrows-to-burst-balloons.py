#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrows = 1
        # at least 1 arrow!
        temp = points[0]
        # set current balloon as temp for further compare
        for i in range(1, len(points)):
            if points[i][0] > temp[1]:
                # exceed range,add one arrow.
                arrows += 1
                temp = points[i]
            else:
                # within range, save one arrow and narrow down the range.
                temp[0] = max(temp[0], points[i][0])
                temp[1] = min(temp[1], points[i][1])
        return arrows


s = [[1, 2], [3, 4], [5, 6], [7, 8]]
Solution.findMinArrowShots(Solution, s)


# @lc code=end
