#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        sort_Func = lambda x: x[0]
        points.sort(key=sort_Func)
        arrows = 0
        index = 0
        while index < len(points) - 1:
            if points[index + 1][0] <= points[index][1]:
                temp = points[index]
                while index < len(points) - 1 and points[index + 1][0] <= temp[1]:
                    index += 1
                arrows += 1
            else:
                arrows += 1
                index += 1
        return arrows


s = [[1, 2], [3, 4], [5, 6], [7, 8]]
Solution.findMinArrowShots(Solution, s)


# @lc code=end
